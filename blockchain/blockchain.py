from models.block import Block
from blockchain.miner import mine_block
from typing import Optional

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
            

# nuevo_bloque = mine_block(
#     index=1,
#     prev_hash="0000...",
#     map_hash="abc123",
#     transactions=[{"from": "A", "to": "B", "amount": 10}]
# )