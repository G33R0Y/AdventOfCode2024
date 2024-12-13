import os

# Function to read input from a file and parse it into rules and updates
def parse_input(file_path):
    with open(file_path, 'r') as file:
        input_string = file.read()
    # Split the input into two parts: rules and updates
    rules_part, updates_part = input_string.strip().split('\n\n')
    # Parse rules into a list of tuples, where each tuple is a pair of integers
    rules = [tuple(map(int, line.split('|'))) for line in rules_part.split('\n')]
    # Parse updates into a list of lists of integers
    updates = [list(map(int, update.split(','))) for update in updates_part.split('\n')]
    return rules, updates

# Function to check if a given update is in the correct order according to the rules
def verify_update(update, rules):
    # Create a dictionary to map each page number to its index in the update list
    index_map = {page: idx for idx, page in enumerate(update)}
    # For each rule (x must come before y)
    for (x, y) in rules:
        # Check if both x and y are in the update
        if x in index_map and y in index_map:
            # If x comes after y in the update, return False
            if index_map[x] > index_map[y]:
                return False
    # If all rules are respected, return True
    return True

# Function to find the middle element of a list
def find_middle(update):
    # Return the element at the middle index
    return update[len(update) // 2]

# Function to sum the middle pages of all correctly ordered updates
def sum_middle_pages(rules, updates):
    # Initialize sum to 0
    middle_sum = 0
    # For each update
    for update in updates:
        # Check if the update is in the correct order
        if verify_update(update, rules):
            # Add the middle page of the update to the sum
            middle_sum += find_middle(update)
    return middle_sum

# Main execution starts here

# Determine the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to 'input.txt' by combining the script directory with the file name
input_file_path = os.path.join(script_dir, 'input.txt')

# Print the current working directory and the input file path for debugging purposes
print(f"Current working directory: {os.getcwd()}")
print(f"Using input file path: {input_file_path}")

# Check if the input file exists at the constructed path
if not os.path.exists(input_file_path):
    print(f"Error: File '{input_file_path}' does not exist.")
else:
    # Parse the input file to get rules and updates
    rules, updates = parse_input(input_file_path)

    # Calculate the sum of the middle pages of correctly ordered updates
    result = sum_middle_pages(rules, updates)

    # Print the result
    print(result)