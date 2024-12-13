import os
from collections import defaultdict, deque

def parse_input(file_path):
    """Reads and parses the input file into rules and updates."""
    with open(file_path, 'r') as file:
        input_string = file.read()
    # Splitting the input into two parts: rules and updates
    rules_part, updates_part = input_string.strip().split('\n\n')
    # Parsing rules into a list of tuples
    rules = [tuple(map(int, line.split('|'))) for line in rules_part.split('\n')]
    # Parsing updates into a list of lists of integers
    updates = [list(map(int, update.split(','))) for update in updates_part.split('\n')]
    return rules, updates

def verify_update(update, rules):
    """Checks if an update is correctly ordered according to the rules."""
    # Create a dictionary to map each page number to its index in the update list
    index_map = {page: idx for idx, page in enumerate(update)}
    # Check each rule to see if it is correctly followed
    for (x, y) in rules:
        if x in index_map and y in index_map:
            # If x should come before y but it does not, return False
            if index_map[x] > index_map[y]:
                return False
    return True

def find_middle(update):
    """Finds the middle element of a list."""
    return update[len(update) // 2]

def reorder_update(update, rules):
    """Reorders an update according to the rules using topological sorting."""
    # Create a graph and in-degree count based on the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    # Create a set of pages in the current update for reference
    pages_in_update = set(update)

    # Build the graph and in-degree count only for relevant pages in the update
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1

    # Initialize a deque (double-ended queue) with nodes that have zero in-degree (no dependencies)
    zero_in_degree_queue = deque([page for page in update if in_degree[page] == 0])
    ordered_update = []

    # Perform topological sorting
    while zero_in_degree_queue:
        current_page = zero_in_degree_queue.popleft()
        ordered_update.append(current_page)
        for neighbor in graph[current_page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree_queue.append(neighbor)
    
    return ordered_update

def sum_middle_pages_after_reordering(rules, updates):
    """Sums the middle pages of re-ordered incorrectly-ordered updates."""
    middle_sum = 0
    # Process each update
    for update in updates:
        # If the update is incorrectly ordered, reorder it
        if not verify_update(update, rules):
            ordered_update = reorder_update(update, rules)
            middle_sum += find_middle(ordered_update)
    return middle_sum

# Main execution starts here
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full file path to 'input.txt'
input_file_path = os.path.join(script_dir, 'input.txt')

# Print the current working directory and the input file path for debugging purposes
print(f"Current working directory: {os.getcwd()}")
print(f"Using input file path: {input_file_path}")

# Check if the input file exists at the specified path
if not os.path.exists(input_file_path):
    print(f"Error: File '{input_file_path}' does not exist.")
else:
    # Parse the input file to get rules and updates
    rules, updates = parse_input(input_file_path)

    # Part 2: Calculate the sum of the middle pages after reordering incorrectly ordered updates
    result_part2 = sum_middle_pages_after_reordering(rules, updates)
    print(result_part2)