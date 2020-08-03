import os
import re


def ls_files(dir):
    """List all files in the current directory

    Args:
        string: Path to list from

    Returns:
        list: List of all the files

    TAKEN FROM THE FOLLOWING STACKOVERFLOW ANSWER:
    https://stackoverflow.com/a/58170903/10933841
    """
    files = []
    for item in os.listdir(dir):
        abspath = os.path.join(dir, item)
        try:
            if os.path.isdir(abspath):
                files = files + ls_files(abspath)
            else:
                files.append(abspath)
        except FileNotFoundError as err:
            print('invalid directory\n', 'Error: ', err)
    return files


project_name = input('What is the name of this project?\n').lower()
project_description = input(
    '\nWhat is the description for this project?\n').lower()

cleaned_files = []
for filename in ls_files('.'):
    ignore = False
    if not (filename.startswith(
            './.git') or '__pycache__' in filename or '.pytest_cache' in filename or filename == './init.py'):
        cleaned_files.append(filename)

for filename in cleaned_files:
    with open(filename, 'r') as file:
        cleaned_lines = []
        lines = file.readlines()
        for line in lines:
            cleaned_lines.append(
                line.replace(
                    'PROJECT_NAME',
                    project_name).replace(
                    'PROJECT_DESCRIPTION',
                    project_description)
            )
    with open(filename, 'w') as file:
        file.write(''.join(cleaned_lines))

print('Everything filled in!\nPlease now delete this file!')
