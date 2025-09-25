from block import block
from blockchain import blockchain

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