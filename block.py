import hashlib
import time

class block:
    def __init__(self, previous_hash: str, content: str):
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.content = content
        self.hash = hashlib.sha256(f"{self.previous_hash}{self.timestamp}{self.content}".encode()).hexdigest()