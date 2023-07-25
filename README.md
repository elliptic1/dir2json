# Directory to JSON Python Script

This Python script traverses the file structure of the current working directory and its subdirectories, and outputs the details into a series of JSON files.

Each JSON file contains a dictionary where the keys are the relative paths of the files and the values are the contents of the files. The script also includes a message at the beginning of each JSON file to indicate which part of the directory structure it represents.

The script works by counting the total number of words in the JSON file. When the number of words exceeds a predefined threshold (default is 1000), the current JSON object is written to a file, and a new JSON object is started for the next file.

## Usage

1. Save the Python script (`dir2json.py`) to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory that contains the Python script using the `cd` command.

4. Run the Python script using the `python` command followed by the name of the Python file:

