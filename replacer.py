import csv
import sys
import os

# Check if at least two arguments are provided
if len(sys.argv) < 3:
    print("Usage: python script.py <string_with_placeholders> <csv_file> [<output_file>]")
    sys.exit(1)

# Get the string with placeholders, the CSV file path, and the output file path (if provided)
string_with_placeholders = sys.argv[1]
csv_file_path = sys.argv[2]
output_file_path = sys.argv[3] if len(sys.argv) > 3 else 'output.txt'

# Check if the output file already exists, and if it does, delete it
if os.path.exists(output_file_path):
    os.remove(output_file_path)

# Open the CSV file and read the contents
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

# Replace the placeholders in the string with values from the CSV file
for row in rows:
    new_string = string_with_placeholders.format(**row)

    # Write the new string to the output file
    with open(output_file_path, 'a') as output_file:
        output_file.write(new_string + '\n')
