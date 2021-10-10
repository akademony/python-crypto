from hashlib import sha256
from time import time

class blockchain:
    def __init__(self):
        time()
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash=1, nonce=100)

    @staticmethod
    def hash(self, string): return sha256(string.encode()).hexdigest()

    def create_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            "time": time,
            "proof": nonce,
            "prev-hash": previous_hash or self.hash(self.chain[-1]),
            "transactions": self.pending_transactions
        }

        self.chain.append(block)
        self.pending_transactions = []
        return block

    def make_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "sender": sender,
            "recient": recipient,
            "data": amount,
        })

    def full_chain(self):
        return self.chain
