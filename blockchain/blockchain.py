from models.block import Block
from blockchain.miner import mine_block
from typing import Optional, Dict

# Node class
class Node:
    def __init__(self, block = Block, previous: Optional["Node"] = None):
        self.block = block
        self.previous = previous

# Each node must storage the previous node/block, i use 
# Optional[] because the first node don't have previous one

# linked list
class BlockChain:
    def __init__(self):
        self.head = None
        self.length = 0
        
    #add block (connect the new block with the previous)
    def add_block(self, block = Block):
        new_node = Node(block, previous = self.head)
        self.head = new_node
        self.length += 1
    
    # travel the blockchain to validate
    def validate(self):
        current = self.head
        while current:
            yield current.block # with yield create a generator
            current = current.previous
    
    
    def create_input(self, map_hash: str, transactions: Dict):
        new_block = mine_block(
            index = self.length,
            prev_hash = self.get_last_hash(),
            map_hash = map_hash,
            transactions = [transactions]
        )
        print(f"✅ Bloque #{new_block.index} minado con hash: {new_block.block_hash[:12]}...")