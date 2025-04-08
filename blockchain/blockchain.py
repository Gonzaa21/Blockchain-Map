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
    
    # create transactions input
    def create_input(self, map_hash: str, transactions: Dict):
        new_block = mine_block(
            index = self.length,
            prev_hash = self.get_last_hash(),
            map_hash = map_hash,
            transactions = [transactions]
        )
        print(f"✅ Block #{new_block.index} mined with hash: {new_block.block_hash[:12]}...")
    
    
    
    # print blockchain
    def print(self):
        print("\n📜 Blockchain:")
        current = self.head
        while current:
            block = current.block
            print(f"\n🧱 Block #{block.index}")
            print(f"  - Hash: {block.block_hash}")
            print(f"  - Previous: {block.prev_hash}")
            print(f"  - Map hash: {block.map_hash}")
            print(f"  - Nonce: {block.nonce}")
            print(f"  - Transaction: {block.transactions}")
            current = current.previous
            
    # hash and chain validations
    def is_valid(self) -> bool:
        current = self.head
        
        while current and current.previous:
            block = current.block
            prev_block = current.previous.block
            
            # Comparison of current hash
            if block.block_hash != block.calculate_hash():
                print(f"❌ Bloque #{block.index} tiene un hash inválido.")
                return False

            # comparison of previous hash
            if block.prev_hash != prev_block.block_hash:
                print(f"❌ Bloque #{block.index} tiene un hash anterior incorrecto.")
                return False

            current = current.previous

            print("✅ Blockchain válida.")
        return True