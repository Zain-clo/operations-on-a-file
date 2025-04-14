# Function to create a file and write some data to it
def create_file(filename):
    with open(filename, 'w') as f:
        f.write("Hello, this is a simple file handling project.\n")
        f.write("We will perform various operations on this file.\n")

# Function to read from the file
def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        print("File Content:")
        print(content)

# Function to append data to the file
def append_to_file(filename, additional_text):
    with open(filename, 'a') as f:
        f.write(additional_text + "\n")

# Main function to demonstrate file handling
def main():
    filename = "sample_file.txt"

    # Create file and write to it
    create_file(filename)

    # Read from the file
    read_file(filename)

    # Append new data to the file
    additional_text = "This is a new line added to the file."
    append_to_file(filename, additional_text)

    # Read the file again to see the appended content
    read_file(filename)

if __name__ == "__main__":
    main()