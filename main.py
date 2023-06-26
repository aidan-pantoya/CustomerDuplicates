def normalize_line(line):
    # Remove leading/trailing whitespace and collapse multiple whitespace characters into a single space
    return ' '.join(line.strip().split())

def find_duplicate_customers(file_path):
    lines_seen = set()
    duplicate_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            normalized_line = normalize_line(line)
            lowercase_line = normalized_line.lower()
            if lowercase_line in lines_seen:
                duplicate_lines.append(normalized_line)
            else:
                lines_seen.add(lowercase_line)

    return duplicate_lines

file_path = 'C:/Users/apant/OneDrive/Desktop/CIDM/CustomerDuplicates/customers.txt'  # Replace with the path to your text file. Make sure to use this slash: "/""
output_file = 'C:/Users/apant/OneDrive/Desktop/CIDM/CustomerDuplicates/duplicate_customers.txt'  # Replace with the desired output file path

duplicate_lines = find_duplicate_customers(file_path)

if duplicate_lines:
    print("Duplicate Customers found:")
    for line in duplicate_lines:
        print(line)

    with open(output_file, 'w') as output:
        uppercase_lines = [line.upper() for line in duplicate_lines]
        output.write('\n'.join(uppercase_lines))
        print(f"\nDuplicate Customers written to '{output_file}'.")
else:
    print("No duplicate Customers found.")
