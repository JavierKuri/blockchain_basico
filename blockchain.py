import block

class blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> block:
        return block(previous_hash="0", content="Genesis Block")

    def add_block(self, content: str):
        previous_hash = self.chain[-1].hash
        new_block = block(previous_hash, content)
        self.chain.append(new_block)