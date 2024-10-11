# MD5 Hash Generator

This Python script generates MD5 hashes from text input. It either reads input from a file (`strings-to-hash.txt`) or accepts user input if the file is empty or doesn't exist. The output is written to `output-multiple.txt` in the format `STRING\tHASH`.

## Features

- Generates MD5 hash for each line in `strings-to-hash.txt`
- If the input file is empty or not found, the script prompts the user to enter text
- Outputs the results in `output-multiple.txt` in the format `STRING\tHASH`
- Provides status messages to indicate the progress of the operation

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the script file.
2. Ensure Python 3.x is installed on your system.
3. Place your input file `strings-to-hash.txt` (if available) in the same directory as the script.

## Usage

### Running the Script

1. If `strings-to-hash.txt` exists and contains data, the script will generate an MD5 hash for each line and write the output to `output-multiple.txt`:
    ```
    STRING<TAB>HASH
    ```
2. If the file is empty or doesn't exist, the script will ask for text input via the console and generate an MD5 hash for the provided text.

### Command

```bash
python md5_hash_generator.py
```

## Usage

1. **Prepare the input file (optional):**
   
   - Create a file named `strings-to-hash.txt` in the same directory as the script.
   - Add the strings to be hashed, one per line.

2. **Run the script:**
   
Open a terminal, navigate to the directory containing the script, and run:

```bash
python3 get-hash.py
```