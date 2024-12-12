import csv

# Specify the file name and the columns to read
file_name = 'car.csv'
columns_to_read = ['Company', 'Car Model']  # Columns to extract

try:
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Check if the requested columns are in the file
        missing_columns = [col for col in columns_to_read if col not in reader.fieldnames]

        if missing_columns:
            print(f"Error: Missing columns in the file: {', '.join(missing_columns)}")
        else:
            # Print the selected columns
            print(", ".join(columns_to_read))
            for row in reader:
                print(", ".join(row[col] for col in columns_to_read))

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
