import hashlib
import json
from pathlib import Path
import generator_code.generator

def generate_hash(filename): # generate hash
    hasher = hashlib.sha256() # create hash with SHA-256
    
    # open bin file, read the folder in parts (blocks of maximum 4096bytes) and 
    # each block read, will be added to hash. The loop breaks when the last block is empty
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
            
    return hasher.hexdigest() # return hash in hex format for more readability

def save_hash(map_filename): # save hash in json
    hash_value = generate_hash(map_filename) # generate hash
    
    hash_dir = Path(__file__).resolve().parent / "maps" / "hash"
    hash_dir.mkdir(parents=True, exist_ok=True)
    
    hash_filename = hash_dir / Path(map_filename).with_suffix(".json").name # save route and replace .bin -> .json

    with open(hash_filename, "w") as f: # add hash value in json file
        json.dump({"hash": hash_value}, f)

    return str(hash_filename)

if __name__ == "__main__":
    map_filename = generator_code.generator.gen_save_map(map)  # save map
    hash_filename = save_hash(map_filename)  # generate and save hash