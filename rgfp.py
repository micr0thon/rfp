#!/usr/bin/env python3

# Imports. Just imports here.
import argparse
from pathlib import Path
import random

# Start of the main definition.
def main():
    # The parser object itself.
    parser = argparse.ArgumentParser(description="This is a file picker, of course, to randomly choose a file out of the folder of your choosing.")

    # Argument(s) of the parser.
    parser.add_argument("-r", "--recursive", action='store_true', help="look for files recursively")
    parser.add_argument("path")

    # Parses the arguments (using argparse)
    args = parser.parse_args()

    # Imports the pathlib thing, or whatever (idk).
    target_path = Path(args.path)

    # Checks if the directory exists.
    if not target_path.exists() or not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid path.")
        return

    if args.recursive:
        # Look through everything recursively.
        items = target_path.rglob('*')
    else:
        # Look only in the immediate, top path directory.
        items = target_path.iterdir()

    # Filter the list so only files are shown, and not subdirectories.
    files = [item for item in items if item.is_file()]

    # Checks if the directory is empty.
    if not files:
        print("No files have been found in this directory.")
        return
    
    print(f"Found {len(files)} files.")

    # Prints the file.
    selected_file = random.choice(files)
    print(selected_file)

if __name__ == "__main__":
    main()
