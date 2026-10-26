#!/usr/bin/env python3

# Imports. Yaaaaaaaay.
import os
import argparse
from pathlib import Path
import random
import sys

# Start of the main definition.
def main():
    # The parser object itself.
    parser = argparse.ArgumentParser(description="This is an application, of course, to randomly choose a file out of the folder of your choosing.")

    # Argument(s) of the parser.
    parser.add_argument("-r", "--recursive", action='store_true', help="look for files recursively")
    parser.add_argument("-f", "--filetype", help="look for a specific filetype")
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
        items = target_path.iterdir()

    files = [item for item in items if item.is_file()]

    if args.filetype:
        ext = args.filetype.strip().lower()
        if not ext.startswith("."):
            ext = f".{ext}"

        files = [f for f in files if str(f).lower().endswith(ext)]  

        if not files:
            print(f"Error: No files found matching '{args.filetype}'.")
            sys.exit(1)

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
