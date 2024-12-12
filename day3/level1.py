import re
import os

def solve_puzzle(filename):
    try:
        # Derive absolute path to ensure the file is found
        script_dir = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(script_dir, filename)

        with open(input_path, 'r') as file:
            data = file.read()

        # Regex to match valid mul(X,Y) instructions
        pattern = re.compile(r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)")

        # Find all matches
        matches = pattern.findall(data)

        # Compute and sum the results of all valid mul(X,Y) instructions
        total = sum(int(x) * int(y) for x, y in matches)

        return total

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

if __name__ == "__main__":
    input_filename = 'input.txt'
    result = solve_puzzle(input_filename)
    if result is not None:
        print(f"The sum of all valid mul(X,Y) instructions is: {result}")