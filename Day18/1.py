# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
## name.png --> 5.png


import os

# Directory path where files are located
directory = r"c:\Users\mdama\OneDrive\Desktop\Python\Day18"

# Create a dictionary to maintain counters for each file format
file_counters = {}

# List all files in the directory
files = os.listdir(directory)

# Iterate through all files
for file in files:
    # Construct the full file path
    file_path = os.path.join(directory, file)
    
    # Check if it's a file (ignore directories)
    if os.path.isfile(file_path):
        # Extract the file extension
        file_extension = os.path.splitext(file)[1]  # Includes the dot, e.g., '.jpeg'
        
        # Initialize the counter for the current file format
        if file_extension not in file_counters:
            file_counters[file_extension] = 1  # Start counter at 1
        
        # Generate a new file name (e.g., 1.jpeg, 2.png)
        new_name = f"{file_counters[file_extension]}{file_extension}"
        new_file_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed: {file} --> {new_name}")
        
        # Increment the counter for this file format
        file_counters[file_extension] += 1

print("Clutter cleared successfully!")
