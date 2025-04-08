from blockchain.blockchain import BlockChain
from utils.utils import transaction_input
# from generator import generate_map  

def main():
    chain = BlockChain()

    while True:
        print(f"\n\033[30m💰 New transaction:\033[0m")
        transaction = transaction_input()

        print(f"\033[30m🗺  Generating token map...\033[0m")
        # ...

        cont = input(f"\033[30m💱 ¿Add other transaction? (y/n): \033[0m")
        if cont.lower() != "y":
            print(f'\033[30mValidating chain...\033[0m')
            chain.is_valid()
            chain.print()
            break

if __name__ == "__main__":
    main()
