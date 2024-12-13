import os  # This imports the 'os' module, which allows us to interact with the operating system (e.g., to work with file paths).

# This function reads the word search from a file and returns it as a list of lists (grid).
def read_word_search(file_path):
    """Read the word search from the input file and return it as a list of lists."""
    word_search = []  # Create an empty list to store the word search.
    
    # Open the file in read mode ('r') and read its contents.
    with open(file_path, 'r') as f:
        for line in f.readlines():  # Read each line from the file.
            # Remove the newline character at the end of each line and convert it to a list of characters.
            word_search.append([x for x in line if x != '\n'])
    
    return word_search  # Return the list of lists (grid) representing the word search.

# This function counts the number of "X-MAS" patterns in the word search.
def count_x_mas_patterns(word_search):
    """Count the number of X-MAS patterns in the word search."""
    n = len(word_search)  # Get the number of rows in the word search grid.
    m = len(word_search[0])  # Get the number of columns (assumes all rows have the same number of columns).
    
    # The two valid "X-MAS" patterns we are looking for in the diagonals.
    x_goal = ['MAS', 'SAM']
    
    count = 0  # Variable to count the number of X-MAS patterns found.

    # Loop through each possible starting point for a 3x3 diagonal pattern.
    for row in range(n - 2):  # Loop through rows (we leave space for 2 more rows below).
        for col in range(m - 2):  # Loop through columns (we leave space for 2 more columns to the right).
            
            # Check the diagonal from top-left to bottom-right (i.e., row, col -> row+1, col+1 -> row+2, col+2).
            diag_1 = ''.join([word_search[row][col],
                              word_search[row+1][col+1],
                              word_search[row+2][col+2]])
            
            # Check the diagonal from bottom-left to top-right (i.e., row+2, col -> row+1, col+1 -> row, col+2).
            diag_2 = ''.join([word_search[row+2][col],
                              word_search[row+1][col+1],
                              word_search[row][col+2]])

            # If both diagonals match either "MAS" or "SAM", we have found an X-MAS pattern.
            count += diag_1 in x_goal and diag_2 in x_goal

    return count  # Return the total number of X-MAS patterns found.

# This block runs if the script is executed directly (not imported).
if __name__ == '__main__':
    # Get the directory where this script is located.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Create the full file path by combining the script directory with the input file name ('input.txt').
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        # Attempt to read the word search from the file.
        word_search = read_word_search(file_path)
        # Count the number of X-MAS patterns in the word search.
        result = count_x_mas_patterns(word_search)
        # Print the result to the console.
        print("Number of X-MAS patterns:", result)
    
    # If the file doesn't exist, print an error message.
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
