import csv
import json

# Part 1: Reading Files
try:
    with open('sample.txt', 'r') as file:
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print("Error: File not found.")
    exit()

# Part 2: Writing Files
with open('output.txt', 'w') as file:
    file.write("This is some sample text.\n")
    file.write("This is another line of text.\n")

# Part 3: Appending to Files
with open('output.txt', 'a') as file:
    file.write("This is some more text.\n")

# Part 5: Working with Different File Formats
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Part 6: Parsing JSON Files
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Part 7: Best Practices for Working with Files
# - Using context managers to ensure files are closed properly
# - Using meaningful variable names
# - Using comments to explain code
# - Handling errors appropriately
# - Following best practices for file naming and organization
