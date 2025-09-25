from block import block

class blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> block:
        return block(previous_hash="\emptyset", content="Genesis Block")

    def add_block(self, content: str):
        previous_hash = self.chain[-1].hash
        new_block = block(previous_hash, content)
        self.chain.append(new_block)

    def verify_hashes(self):
        for i in range(len(self.chain)-1):
            if self.chain[i].hash != self.chain[i+1].previous_hash:
                print("Error, hashes do not match")
                break
        print("All hashes match correctly")
