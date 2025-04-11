from blockchain.blockchain import BlockChain
from utils.utils import transaction_input
import json
from pathlib import Path
from generator_code.generator import generate_map, gen_save_map
from generator_code.hash_utils import save_hash

# read submodule config.json file
with open(Path(__file__).resolve().parent / "generator" / "config.json") as f:
    config = json.load(f)

def main():
    chain = BlockChain()

    while True:
        print(f"\n\033[30m💰 New transaction:\033[0m")
        transaction = transaction_input()

        print(f"\033[30m🗺  Generating token map...\033[0m")
        map_data = generate_map(
            size=config["size"],
            scale=config["scale"],
            octaves=config["octaves"]
        )
        map_path = gen_save_map(map_data)
        hash_path = save_hash(map_path)

        # Leer el hash del archivo
        with open(hash_path) as f:
            map_hash = json.load(f)["hash"]

        chain.create_input(map_hash, transaction)

        cont = input(f"\033[30m💱 ¿Add other transaction? (y/n): \033[0m")
        if cont.lower() != "y":
            print(f'\033[30mValidating chain...\033[0m')
            chain.is_valid()
            chain.print()
            break

if __name__ == "__main__":
    main()
