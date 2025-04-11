import src.generator as generator
import src.visualizer as visualizer
import generator.src.hash_utils as hash_utils
import json
import numpy as np

# config.json
with open("config.json", "r") as file:
    config = json.load(file)

def Main():
    print("Generating map...")
    map = generator.generate_map(config["size"], config["scale"], config["octaves"])
    map_filename = generator.gen_save_map(map)

    print("Showing and saving image...")
    visualizer.visualizer_map(map)
    visualizer.save_map(map, config["output"])
    
    hash_filename = hash_utils.save_hash(map_filename)
    print(f"Map saved in: {map_filename}")
    print(f"Hash saved in: {hash_filename}")
    
    print("Process completed. Map saved in:", config["output"])

if __name__ == "__main__":
    Main()