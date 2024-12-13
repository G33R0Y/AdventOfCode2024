import os  # Import os module for handling file paths

# Function to read the input file and return a list of strings (each string is a row in the grid)
def read_input(filename):
    with open(filename, 'r') as file:  # Open the file in read mode
        return [line.strip() for line in file]  # Read each line, strip leading/trailing whitespace, and return as a list

# Function to search for the word "XMAS" in the grid in all possible directions
def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
    word_length = len(word)  # Length of the word "XMAS"
    word_count = 0  # Initialize the count of the word occurrences

    # Define 8 possible directions to search for the word
    directions = [
        (0, 1),    # right
        (0, -1),   # left
        (1, 0),    # down
        (-1, 0),   # up
        (1, 1),    # down-right
        (-1, -1),  # up-left
        (1, -1),   # down-left
        (-1, 1)    # up-right
    ]

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check each direction from the current cell
            for dr, dc in directions:
                # Ensure the word can fit in the current direction from the current cell
                if 0 <= row + (word_length - 1) * dr < rows and 0 <= col + (word_length - 1) * dc < cols:
                    # Check if all characters match the word "XMAS" in the current direction
                    if all(grid[row + i * dr][col + i * dc] == word[i] for i in range(word_length)):
                        word_count += 1  # Increment the word count if a match is found

    return word_count  # Return the total count of the word occurrences

# Main execution block, only runs when the script is executed directly
if __name__ == "__main__":
    input_filename = 'input.txt'  # Define the input filename
    
    # Get the directory of the script and construct the full path to the input file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, input_filename)
    
    # Check if the input file exists at the constructed path
    if not os.path.exists(input_path):
        print(f"File {input_path} not found.")  # Print an error message if the file is not found
    else:
        grid = read_input(input_path)  # Read the grid from the input file
        word = "XMAS"  # Set the word to search for
        count = search_word(grid, word)  # Search for the word in the grid
        # Print the total count of the word occurrences
        print(f"The word '{word}' occurs {count} times in the grid.")