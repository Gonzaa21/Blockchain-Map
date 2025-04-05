import hashlib
import json
from models.block import Block
from typing import List, Dict, Any

DIFFICULTY = 4  # number of zeros of hash

def mine_block(
    index: int,
    prev_hash: str,
    map_hash: str,
    transactions: List[Dict[str, Any]]
    ) -> Block:
    
    nonce = 0
    while True:
        block_data = {
            "index": index,
            "prev_hash": prev_hash,
            "map_hash": map_hash,
            "transactions": transactions,
            "nonce": nonce
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        block_hash = hashlib.sha256(block_string).hexdigest()

        if block_hash.startswith("0" * DIFFICULTY):
            # hash finded:
            return Block(
                index=index,
                prev_hash=prev_hash,
                map_hash=map_hash,
                transactions=transactions,
                nonce=nonce,
                block_hash=block_hash
            )

        nonce += 1