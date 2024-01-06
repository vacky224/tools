import os

user_directory = input("Enter the directory path: ")
print("You entered:", user_directory)

if os.path.isdir(user_directory):
    # Use os.walk to traverse the directory tree
    for dirpath, dirnames, filenames in os.walk(user_directory):
        print(f"Current directory: {dirpath}")
        print(f"Subdirectories: {dirnames}")
        print(f"Files: {filenames}")
        print("--------------------")
else:
    print("Invalid directory path. Please provide a valid directory.")

