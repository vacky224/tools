import re
import argparse
import os

def grep(expression, file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if re.search(expression, line):
                    print(f"{file_path}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def search_files(expression, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            grep(expression, file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a regular expression in files.")
    parser.add_argument("expression", help="The regular expression to search for.")
    parser.add_argument("directory", help="The directory to search in.")
    args = parser.parse_args()

    search_files(args.expression, args.directory)

