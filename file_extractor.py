"""
@author Jackson Elowitt

Given a directory path as "old_path" and a different directory path as "new_path", move every file which isn't a folder
from old_path to new_path.

There is no way to undo the move other than manually, so be extremely careful.
The folders will remain in the old_path.
"""
from os import path as p
from os import walk as w
from shutil import move as m

# Validate the directories

cont = True
while cont:
    old_path = input("Please enter the parent directory of all the files you want to move:\n")
    cont = False if p.exists(old_path) else True
    if cont:
        print("Directory not found. Please enter a valid directory.")

cont = True
while cont:
    new_path = input("Please enter the directory where all the files should be moved to:\n")
    cont = False if p.exists(new_path) else True
    if cont:
        print("Directory not found. Please enter a valid directory.")

f = []  # List of files in those directories
df = []  # List of files with the directories attached to them

print("Running...")

# Get the path, name, and filename of every item from the top, to the lowest file level.
for (dirpath, dirnames, filenames) in w(old_path):
    for item in filenames:
        f.append(item)
        df.append(dirpath + "/" + item)

for index, item in enumerate(df):
    m(item, fr"{new_path}\{f[index]}")  # Move the file to the new location

total_files = len(f)
input(f"Complete. Total Files Moved: {total_files}. Press enter to exit.")
