import csv
import json

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile:
        # Read the entire file as a string
        file_content = infile.read()

    # Split the file content into separate JSON objects based on '}\n{' delimiter
    json_objects = file_content.strip().split('}\n{')

    # Add missing curly braces back to each JSON object string and parse them
    data_list = []
    for json_object_str in json_objects:
        # Add missing curly braces
        if not json_object_str.endswith('}'):
            json_object_str += '}'
        if not json_object_str.startswith('{'):
            json_object_str = '{' + json_object_str
        # Parse the JSON object string
        try:
            data_list.append(json.loads(json_object_str))
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON object: {e}")

    # Check if there's any data to write
    if not data_list:
        print("No data to write")
        return

    # Get the header (column names) from the keys of the first item
    header = data_list[0].keys()

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)

        # Write the header to the CSV file
        writer.writeheader()

        # Write the data to the CSV file
        for data in data_list:
            writer.writerow(data)

# Call the function, specifying the input and output file names
convert_to_csv('output.txt', 'output.csv')
