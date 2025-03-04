# AF3Json

A Python utility that converts FASTA sequence files into structured JSON format for protein structure prediction workflows.

## Overview

AF3Json parses FASTA formatted protein sequence files and transforms them into a specialized JSON structure that can be used with protein structure prediction tools. The script preserves sequence names from FASTA headers and organizes the data in a consistent format.

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

No installation required. Simply clone or download this repository:

```bash
git clone https://github.com/yourusername/AFSJson.git
cd AFSJson
```

## Usage

### Basic Usage

```bash
python AF3Json.py input.fasta
```

This will create a file named `protein_jobs.json` in the current directory.

### Advanced Options

```bash
python AF3Json.py input.fasta -o custom_output.json
```

#### Command-line Arguments

| Argument | Description |
|----------|-------------|
| `fasta_file` | Path to the input FASTA file (required) |
| `-o, --output` | Custom output filename (default: protein_jobs.json) |

## Output Format

The script generates a JSON file with the following structure:

```json
[
    {
        "name": "protein_identifier",
        "modelSeeds": [],
        "sequences": [
            {
                "proteinChain": {
                    "sequence": "AMINO_ACID_SEQUENCE",
                    "count": 1
                }
            }
        ]
    },
    ...
]
```

Each entry in the array represents a protein sequence from the input FASTA file.

## Error Handling

The script includes robust error handling for common issues:
- Missing input files
- Permission errors
- Empty or malformed FASTA files

## Examples

### Example 1: Basic Conversion

```bash
python AF3Json.py sequences.fasta
```

### Example 2: Custom Output Name

```bash
python AF3Json.py sequences.fasta -o prediction_input.json
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.