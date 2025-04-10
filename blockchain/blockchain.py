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
        
        prev_hash = self.head.block.block_hash if self.head else "0"
        
        # create blocks
        new_block = mine_block(
            index = self.length,
            prev_hash = prev_hash,
            map_hash = map_hash,
            transactions = [transactions]
        )
        self.add_block(new_block) # adding to chain
        print(f"✔ Block #{new_block.index} mined with hash: {new_block.block_hash[:12]}...")
    
    
    
    # print blockchain
    def print(self):
        print("\n📜 Blockchain:")
        current = self.head
        while current:
            block = current.block
            print(f"\033[30m\n🧱 Block #{block.index}\033[0m")
            print(f"\033[90m  - Hash:\033[0m \033[37m{block.block_hash}\033[0m")
            print(f"\033[90m  - Previous:\033[0m \033[37m{block.prev_hash}\033[0m")
            print(f"\033[90m  - Map hash:\033[0m \033[37m{block.map_hash}\033[0m")
            print(f"\033[90m  - Nonce:\033[0m \033[37m{block.nonce}\033[0m")
            print(f"\033[90m  - Transaction:\033[0m \033[37m{block.transactions}\033[0m")
            current = current.previous
            
    # hash and chain validations
    def is_valid(self) -> bool:
        current = self.head
        
        while current and current.previous:
            block = current.block
            prev_block = current.previous.block
            
            # Comparison of current hash
            if block.block_hash != block.calculate_hash():
                print(f"\033[31m❌ Block #{block.index} have a invalid hash.\033[0m")
                return False

            # comparison of previous hash
            if block.prev_hash != prev_block.block_hash:
                print(f"\033[31m❌ Block #{block.index} have a bad previous hash.\033[0m")
                return False

            current = current.previous

            print(f"\033[32m✔ Blockchain valid.\033[0m")
        return True