import hashlib
import os

# Function to create the MD5 hash of a text
def generate_md5_hash(text):
    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()

# Filename for input and output
input_filename = 'strings-to-hash.txt'
output_filename = 'output-multiple.txt'

# Check if the file exists and is not empty
if os.path.exists(input_filename) and os.path.getsize(input_filename) > 0:
    # Open the file and read it line by line
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    # Write the results to the output file
        print("✅ Success!")
        print("Output written in output-multiple.txt")
    with open(output_filename, 'w') as output_file:
        for line in lines:
            line = line.strip()  # Remove any whitespace and line breaks
            if line:  # Ensure the line is not empty
                hash_value = generate_md5_hash(line)
                output_file.write(f"{line}\t{hash_value}\n")
else:
    # File is empty or doesn't exist, ask for user input
    print("✔️ strings-to-hash.txt is empty...")
    text = input("🤓 Enter the text for hash: ")
    if text:
        hash_value = generate_md5_hash(text)
        with open(output_filename, 'w') as output_file:
            output_file.write(f"{text}\t{hash_value}\n")
    else:
        print("🥲 No text provided.")
