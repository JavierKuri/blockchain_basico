from block import block
from blockchain import blockchain
import json

if __name__ == "__main__":
    my_chain = blockchain()

    my_chain.add_block("Transaction 1")
    my_chain.add_block("Transaction 2")
    my_chain.add_block("Transaction 3")

    for i, block in enumerate(my_chain.chain):
        print(f"Block {i}:")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Content: {block.content}")
        print(f"  Hash: {block.hash}\n")

    my_chain.verify_hashes()

    with open("./blockchain.json", "w") as f:
        json.dump([b.__dict__ for b in my_chain.chain], f, indent=4)

    with open("./blockchain.json", "r") as f:
        loaded_chain = json.load(f)