import csv

def csv_to_markdown(csv_file):
    # Open the CSV file
    with open(csv_file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        
        # Read the header (first row)
        header = next(csv_reader)
        
        # Create the Markdown table format
        markdown_table = "| " + " | ".join(header) + " |\n"
        markdown_table += "| " + " | ".join(["-" * len(col) for col in header]) + " |\n"
        
        # Add each row of the CSV as a Markdown table row
        for row in csv_reader:
            markdown_table += "| " + " | ".join(row) + " |\n"
    
    return markdown_table

# Example usage:
csv_file = 'Dataset/age_cat_offense_cat_percent.csv'  # Replace with the path to your CSV file
markdown_table = csv_to_markdown(csv_file)

# Print the Markdown table
print(markdown_table)