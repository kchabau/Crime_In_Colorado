# Import libraries
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd 
import numpy as np 
from datetime import datetime
from credentials.creds import cursor, conn # import connections to database 
import os 
import sys


# ETL 

print(f'<------------------ Extraction Started ------------------->\n')
# Stage 1. Extract 
def extract():
    # Get current working directory
    pwd = os.getcwd()
    file_name = 'Crimes_in_Colorado_20250512.csv'

    # Load CSV into dataframe
    original = pd.read_csv(f'{pwd}/Dataset/{file_name}')

    # Create copy
    df = original.copy()

    # Create array for columns
    columns_array = []
    # Append column to list of columns
    for col in df.columns:
        columns_array.append(col)

    
    # Globalize string and numeric columns so that we can use it in our imputation later on
    global string_columns
    global numeric_columns
    # Separate into string and numeric columns
    string_columns = ['pub_agency_name', 'county_name', 'incident_date', 'offense_name', 'crime_against', 'offense_category_name', 'offense_group']
    numeric_columns = ['age_num', 'incident_hour']
    
    return df, 'Dataframe Extracted'

# Run the extract and save to new_df variable
new_df, message = extract()
print(message)
print(f'<------------------ Extraction Complete ------------------->\n')


print(f'<------------------ Multiple Imputation Started ------------------->\n')
# Step 2. Apply Multiple Imputation For Handling Missing Data
def multiple_imp(new_df):
    # Use Multiple Imputation as a technique for filling in the missing date 
    # We will first have to split the data set into two 

    half_of_data = int(len(new_df) / 2) # use int to get a whole number

    first_half = new_df[numeric_columns].iloc[:half_of_data]
    second_half = new_df[numeric_columns].iloc[half_of_data:]
    # Inspect missing data before imputation
    print("First half missing, before imputation:\n", first_half.isnull().sum())
    print("Second half missing, before imputation:\n", second_half.isnull().sum())


    # Create IterativeImputer model to predict missing values
    imp = IterativeImputer(max_iter=10, random_state=0)


    # Fit the model to the second_half of dataset 
    # We can do this vice versa and expand on the framework, by going through another option
    # of fitting the model to the first half of the data, before transforming on the entire dataset
    imp.fit(first_half)

    # Transform on the first_half of model
    imputed_1_0 = pd.DataFrame(np.round(imp.transform(first_half), 1), columns=numeric_columns)
    # Transform on the second_half of data
    imputed_2_0 = pd.DataFrame(np.round(imp.transform(second_half), 1), columns=numeric_columns)

    print("Imputed First Half missing:\n", imputed_1_0.isnull().sum())
    print("Imputed Second Half missing:\n", imputed_2_0.isnull().sum())

    imputations_renamed = {
        'age_num': 'age_num_imputed',
        'incident_hour': 'incident_hour_imputed'
    }

    imputed_1_0 = imputed_1_0.rename(columns=imputations_renamed)
    imputed_2_0 = imputed_2_0.rename(columns=imputations_renamed)

    # Concatenate both imputed halves back together
    imputed_full = pd.concat([imputed_1_0, imputed_2_0], axis=0).reset_index(drop=True)

    # Reset index on original df to match imputed_full
    new_df = new_df.reset_index(drop=True)

    # Now concat with original df
    final_df = pd.concat([new_df, imputed_full], axis=1)

    # Drop original (non-imputed) columns
    imputed_df = final_df.drop(['age_num', 'incident_hour'], axis=1)
    print(f'Length of the Imputed DataFrame: {len(imputed_df)}')


    # Wonderful, this is our complete dataset which we will actually be working with and using to import into our SQL but we still have some data cleaning to do 
    return imputed_df, "Imputation Complete"

# Provide the multiple imp function the new_df to retrieve the imputed df 
imputed_df, message = multiple_imp(new_df)
print(message)
print(f'<------------------ Multiple Imputation Complete ------------------->\n')



print(f'<------------------ Transformation Started ------------------->\n')
# Step 3. Transformation
def transform(imputed_df):

    # Convert Date columns
    # We need to convert them into a format that is digestible for SQL database 
    # YYYY-MM-DD

    # Convert incident date to string 
    imputed_df['incident_date'] = imputed_df['incident_date'].astype(str)

    # Extract year, month, and day into separate columns
    imputed_df['month'] = imputed_df['incident_date'].str[:2]
    imputed_df['day'] = imputed_df['incident_date'].str[3:5]
    imputed_df['year'] = imputed_df['incident_date'].str[6:10]
    imputed_df['incident_date_converted'] = imputed_df['year'] + '-' + imputed_df['month'] + '-' + imputed_df['day']

    # Create a new copy of the dataframe in case we need to adjust original data
    columns_to_drop = ['incident_date', 'month', 'day', 'year']

    dropped_columns = imputed_df.copy().drop(columns=columns_to_drop)

    # Remove any duplicate rows (there should be none)
    transformed_df = dropped_columns.drop_duplicates()
    print(f'Length of the Transformed DataFrame: {len(transformed_df)}')

    return transformed_df, "Transformation Complete"

transformed_df, message = transform(imputed_df)
print(message)
print(f'<------------------ Transformation Complete ------------------->\n')


# Link to resource used for this section: https://www.youtube.com/watch?v=wqBFgaMgFQA&t=1152s
# We need to convert these data types to something that would be digestible by SQL.
# So we will create a dictionary of values of the Python-SQL Datatypes

replacements = {
    'object': 'varchar',
    'float64': 'float',
    'int64': 'int',
    'datetime64': 'timestamp',
    'timedelta64[ns]': 'varchar'
}

print(f'<------------------ Loading Started ------------------->\n')
# Step 4. Load (into MySQL)
def database_load(transformed_df):
    # Create a format that generates "column_name data_type" for each column
    col_string = ", ".join( # This is intended to be used more for PostgreSQL bulk loads
        "{} {}".format(n, d) for n, d in zip(transformed_df.columns, transformed_df.dtypes.replace(replacements)) # This section was ultimately not used, just for show (At least not here; please inspect Juunyper Notebook)
    )
    
    columns = ['pub_agency_name', 'county_name', 'offense_name', 'crime_against',
                'offense_category_name', 'offense_group', 'incident_date_converted',
                  'age_num_imputed', 'incident_hour_imputed']

    final_df = transformed_df[columns]


    # Drop table with the same name 
    cursor.execute("DROP TABLE IF EXISTS crimes_in_colorado;")
    print('Dropped table with same name (in case, necessary)')

    # Create table
    cursor.execute("""
        CREATE TABLE crimes_in_colorado (
            pub_agency_name VARCHAR(255),
            county_name VARCHAR(255),
            offense_name VARCHAR(255),
            crime_against VARCHAR(255),
            offense_category_name VARCHAR(255),
            offense_group VARCHAR(255),
            incident_date_converted VARCHAR(255),
            age_num_imputed FLOAT,
            incident_hour_imputed FLOAT
        )
    """)
    print('New Table Created')

    # Save DataFrame to CSV
    final_df.to_csv('crimes.csv', header=final_df.columns, index=False, encoding='utf-8')

    # Load into MySQL
    load_sql = """
        LOAD DATA LOCAL INFILE 'crimes.csv'
        INTO TABLE crimes_in_colorado
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
    """
    cursor.execute(load_sql)
    conn.commit()

    cursor.close()
    print('Table import to DB completed')


database_load(transformed_df)
print(f'<------------------ Loading Complete ------------------->\n')