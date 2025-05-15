# utils/mempool.py
# Lightweight GPU-prioritized mempool queue

import heapq
import hashlib
import time
import os

class Transaction:
    def __init__(self, tx_data, fee):
        self.tx_data = tx_data  # Raw 32-byte tx
        self.fee = fee
        self.timestamp = time.time()

    def __lt__(self, other):
        # Prioritize higher fees, then earlier timestamps
        return (-self.fee, self.timestamp) < (-other.fee, other.timestamp)

class Mempool:
    def __init__(self):
        self.queue = []

    def add_tx(self, tx_data, fee=None):
        """
        Adds a transaction to the pool.
        """
        if fee is None:
            fee = self.estimate_fee(tx_data)
        tx = Transaction(tx_data, fee)
        heapq.heappush(self.queue, tx)

    def pop_batch(self, count=128):
        """
        Pops top-N transactions by fee.
        """
        batch = []
        while self.queue and len(batch) < count:
            batch.append(heapq.heappop(self.queue).tx_data)
        return batch

    def estimate_fee(self, tx_data):
        """
        Dummy fee estimator — hashes data and maps to a float.
        """
        h = hashlib.sha256(tx_data).digest()
        return int.from_bytes(h[:2], 'big') / 100.0

    def size(self):
        return len(self.queue)

# CLI test
if __name__ == "__main__":
    mempool = Mempool()
    for i in range(10):
        mempool.add_tx(os.urandom(32))
    print("Batch:", [tx.hex() for tx in mempool.pop_batch(5)])
