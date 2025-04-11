from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import hashlib
import json

@dataclass
class Block:
    index: int
    prev_hash: str
    map_hash: str
    transactions: List[Dict[str, Any]]
    nonce: int
    block_hash: str = ""
    
    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "prev_hash": self.prev_hash,
            "map_hash": self.map_hash,
            "transactions": self.transactions,
            "nonce": self.nonce
        }
        
        # convert data to json file
        block_json = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_json).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        #convert a object to dictionary
        return asdict(self)