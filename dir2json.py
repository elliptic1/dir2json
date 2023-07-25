import json
import os


def count_words(text):
    """Count the number of words in a text."""
    return len(text.split())


def get_filename(write_dir, page_num):
    filename = os.path.expanduser(f"~/dir2json/"
                                  + write_dir.replace("/", "_")
                                  + f"directory_contents_{page_num}.json")
    print(f"Generated filename: {filename}")
    return filename


# Get the current directory
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

# Set the word count threshold
word_threshold = 100000

# Create a JSON object
json_object = {"message": f"This is the directory structure of {current_directory}. "}

# Initialize file counter
file_number = 1

file_name = get_filename(current_directory, file_number)
os.makedirs(os.path.dirname(file_name), exist_ok=True)

# Initialize total word count
total_word_count = 0

# Walk through the directory tree
for dir_path, dir_names, file_names in os.walk(current_directory):
    print(f"Inspecting directory: {dir_path}")
    for file_name in file_names:
        print(f"Inspecting file: {file_name}")
        # Construct the full file path
        file_path = os.path.join(dir_path, file_name)

        # If the content is a file, read it and add its contents to the JSON object
        try:
            with open(file_path, "r") as file:
                file_contents = file.read()
            print(f"File contents: {file_contents}")
        except UnicodeDecodeError:
            print(f"Cannot read file: {file_path}")
            file_contents = "<non-text file>"

        # Use the relative path to the file as the key in the JSON object
        relative_path = os.path.relpath(file_path, current_directory)
        json_object[relative_path] = file_contents

        # Update total word count
        total_word_count += count_words(file_contents)
        print(f"Total word count: {total_word_count}")

        # If the word count exceeds the threshold, write the JSON object to a file and start a new one
        if total_word_count > word_threshold:
            with open(get_filename(current_directory, file_number), "w") as f:
                json.dump(json_object, f, indent=4)
            print(
                f"Word count exceeded threshold. Wrote JSON object to file: {get_filename(current_directory, file_number)}")

            # Increment the file number and start a new JSON object
            file_number += 1
            json_object = {
                "message": f"This is the directory structure of {current_directory}. File number {file_number}."}
            total_word_count = 0
            print(f"Starting new JSON object. File number: {file_number}")

# Write the remaining JSON object to a file
with open(get_filename(current_directory, file_number), "w") as f:
    json.dump(json_object, f, indent=4)
print(f"Wrote remaining JSON object to file: {get_filename(current_directory, file_number)}")
