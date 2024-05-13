import sys
import json



def parse_fasta_file(fasta_file):
    sequences = []
    current_sequence = None

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                name = line[1:]#[1:5]  I like to do the first 4 characters since that's typically the proteins name with pdb, but this will take all 
                current_sequence = {"name": name, "sequence": ""}
            else:
                current_sequence["sequence"] += line

        if current_sequence:
            sequences.append(current_sequence)

    return sequences

# Function to create JSON structure
def create_json_structure(sequences):
    json_data = []

    for seq in sequences:
        job = {
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
        json_data.append(job)

    return json_data

def main(fasta_file):
    sequences = parse_fasta_file(fasta_file)
    json_data = create_json_structure(sequences)
    output_file = "protein_jobs.json"
    with open(output_file, "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"JSON file '{output_file}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <fasta_file>")
    else:
        fasta_file = sys.argv[1]
        main(fasta_file)

