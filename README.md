# Colorado Crime Data ETL and Analysis Project

![tableau_screenshot_1](/Assets/tableau_screenshot_1.png)

## 📊 Overview

This project focuses on building an end-to-end ETL (Extract, Transform, Load) pipeline using Python to process real-world crime data from the state of Colorado. The dataset, sourced from the [Colorado Public Safety Data Portal](https://data.colorado.gov/Public-Safety/Crimes-in-Colorado/j6g4-gayk/about_data), includes approximately **3.5 million** records of reported crimes.

My primary objective was to sharpen my technical skills—particularly in data engineering and analysis—while gaining a deeper understanding of the state I've lived in for many years. This intersection of personal curiosity and professional development inspired the project.

Here is a link to the [Tableau Dashboard](https://public.tableau.com/app/profile/kevin.chabau/viz/CrimesinColorado/Dashboard1).

To read more about the results, please refer to the [Results folder](/Results/) containing more information about the dataset.

---

## 🔧 Tools & Technologies

- **Python**: ETL scripting with libraries such as `pandas`, `numpy`, `os`, and `sklearn`
- **MySQL**: Database design and data storage
- **SQL**: Querying and future data analysis
- **MySQL Connector**: Remote database connection for automated inserts
- **Excel/CSV**: Data preview and exploratory analysis
- **Visual Studio Code**: Development environment

---

## ⚙️ ETL Process

### 1. **Extract**
- Downloaded a CSV file (~3.5M records) containing statewide crime data.
- Loaded into Python using `pandas` for initial exploration and profiling.

### 2. **Transform**
- **Data Cleaning**:
  - Checked for null values, corrected data types, dropped duplicates.
  - Generated descriptive statistics for numeric and categorical fields.

- **Missing Value Imputation**:
  - Used **Multiple Imputation** via `IterativeImputer` from `sklearn` to intelligently estimate missing values for numeric columns like:
    - `age_num`
    - `incident_hour`
  - This method uses predictive modeling to estimate missing values based on other features—enhancing data quality and completeness.

- **Standardization**:
  - Converted categorical and timestamp fields to appropriate formats.
  - Renamed columns for clarity and consistency.

### 3. **Load**
- Established a remote connection to a MySQL database using `mysql.connector`.
- Bulk inserted the cleaned and transformed data into a structured table.
- The database is now primed for SQL-based exploration and analysis.

---

## 📈 Future Work

- Developed a **Tableau Dashboard** to visualize crime trends, patterns, and anomalies across Colorado.
- Shared insights and visualizations through a **LinkedIn article**.
- Conduct deeper analysis on:
  - Crime by location and time of day
  - Demographic correlations
  - Longitudinal trends and seasonal patterns

---

## 🧠 Methodologies Used

- ETL (Extract, Transform, Load) Pipelines
- Multiple Imputation for Missing Data
- Data Cleaning & Normalization
- Predictive Data Imputation with Scikit-learn
- SQL Query Optimization (planned)
- Visualization & Storytelling (upcoming)

---

## 💡 Why This Project?

- To grow my technical stack in **data engineering** and **analytics**
- To understand more about crime trends in my community
- To create public-facing data work that is **impactful**, **relevant**, and **insightful**

---

## 📂 Dataset Reference

**Title**: Crimes in Colorado  
**Source**: [Colorado Department of Public Safety](https://data.colorado.gov/Public-Safety/Crimes-in-Colorado/j6g4-gayk/about_data)  
**License**: Public Domain / Open Data  

---

## Hindsight is 20/20

I should have formulated the months through string selection first, before attempting to convert the format to a valid one for SQL. I could have retrieve