# AF3Json Documentation

`AF3Json.py` is a Python script designed to parse sequence data from FASTA formatted files and convert it into a structured JSON format suitable for further processing or analysis. The script reads a FASTA file specified by the user, extracts the sequence information, and outputs a JSON file containing the sequence data.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Functions](#functions)
  - [parse_fasta_file](#parse_fasta_file)
  - [create_json_structure](#create_json_structure)
  - [main](#main)
- [Examples](#examples)
- [Output](#output)

## Requirements

- Python interpreter (version 3.0 or higher)
- FASTA formatted file containing sequence data

## Usage

To use the script, you need to have a FASTA file that you want to convert into JSON. Then, run the script from the command line with the following command:

```bash
python AF3Json.py <fasta_file>
```

Replace `<fasta_file>` with the path to your FASTA file.

## Functions

### parse_fasta_file

The `parse_fasta_file` function takes a single argument, the path to a FASTA file, and parses the sequences contained within it.

#### Arguments:

- `fasta_file`: A string representing the file path of the FASTA file to be parsed.

#### Returns:

- A list of dictionaries where each dictionary contains the sequence name and sequence string.

### create_json_structure

The `create_json_structure` function converts the list of sequences obtained from `parse_fasta_file` into a JSON-friendly list of dictionaries.

#### Arguments:

- `sequences`: A list of dictionaries containing the sequence information.

#### Returns:

- A list of dictionaries formatted for JSON output.

### main

The `main` function orchestrates the parsing of the FASTA file and the creation of the JSON output. It is the entry point of the script when run from the command line.

#### Arguments:

- `fasta_file`: A string representing the file path of the FASTA file to be parsed.

## Examples

Here is an example of how to run the script from the command line:

```bash
python AF3Json.py example.fasta
```

This command will process `example.fasta` and generate a file named `protein_jobs.json` containing the JSON representation of the sequences.

## Output

The script will create a JSON file named `protein_jobs.json` in the same directory as the script. The JSON file will contain an array of objects, each representing a sequence from the FASTA file with the following structure:

```json
[
    {
        "name": "<sequence_name>",
        "modelSeeds": [],
        "sequences": [
            {
                "proteinChain": {
                    "sequence": "<sequence_string>",
                    "count": 1
                }
            }
        ]
    },
    ...
]
```

Each object in the array corresponds to a sequence in the FASTA file, with the `name` and `sequence` extracted from the file.

After the JSON file is created, you will see a confirmation message:

```
JSON file 'protein_jobs.json' created successfully.
```

This documentation provides an overview of how to use the `AF3Json.py` script. For more detailed information about how the code works internally, you may review the source code directly.