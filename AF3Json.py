#!/usr/bin/env python3
"""
AF3Json - Convert FASTA sequences to JSON format for protein structure prediction.
"""
import sys
import json
import argparse
from typing import List, Dict, Any


def parse_fasta_file(fasta_file: str) -> List[Dict[str, str]]:
    """
    Parse a FASTA file and extract sequence information.
    
    Args:
        fasta_file: Path to the FASTA file
        
    Returns:
        List of dictionaries containing sequence name and content
    """
    sequences = []
    current_sequence = None

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                name = line[1:]  # Extract full header after '>'
                current_sequence = {"name": name, "sequence": ""}
            elif current_sequence:  # Only append if we've seen a header
                current_sequence["sequence"] += line

        # Don't forget the last sequence
        if current_sequence:
            sequences.append(current_sequence)

    return sequences


def create_json_structure(sequences: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """
    Convert sequence data to the required JSON structure.
    
    Args:
        sequences: List of dictionaries with sequence information
        
    Returns:
        List of dictionaries formatted for JSON output
    """
    return [
        {
            "name": seq["name"],
            "modelSeeds": [],
            "sequences": [
                {
                    "proteinChain": {
                        "sequence": seq["sequence"],
                        "count": 1
                    }
                }
            ]
        }
        for seq in sequences
    ]


def main():
    """Main function to parse arguments and process the FASTA file."""
    parser = argparse.ArgumentParser(description='Convert FASTA to JSON for protein structure prediction')
    parser.add_argument('fasta_file', help='Path to the input FASTA file')
    parser.add_argument('-o', '--output', default='protein_jobs.json', 
                        help='Output JSON filename (default: protein_jobs.json)')
    args = parser.parse_args()

    try:
        sequences = parse_fasta_file(args.fasta_file)
        if not sequences:
            print(f"Warning: No sequences found in {args.fasta_file}")
            return

        json_data = create_json_structure(sequences)
        
        with open(args.output, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"JSON file '{args.output}' created successfully with {len(sequences)} sequences.")
    
    except FileNotFoundError:
        print(f"Error: File '{args.fasta_file}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when reading '{args.fasta_file}' or writing output file.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

