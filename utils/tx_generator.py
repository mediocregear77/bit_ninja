# utils/tx_generator.py
# Generates synthetic transactions for testing and benchmarking

import os
import hashlib
import time
import random

def generate_tx(seed=None):
    """
    Generate a synthetic 32-byte transaction hash.
    """
    if seed is None:
        seed = f"{time.time_ns()}_{random.randint(0, 1e9)}"
    raw = seed.encode("utf-8")
    return hashlib.sha256(raw).digest()

def generate_batch(count=128):
    """
    Generate a list of N fake transaction hashes (32 bytes each).
    """
    return [generate_tx() for _ in range(count)]

def generate_hex_batch(count=128):
    """
    Returns a list of 64-char hex strings (for JSON test input).
    """
    return [generate_tx().hex() for _ in range(count)]

# CLI test
if __name__ == "__main__":
    batch = generate_hex_batch(10)
    for tx in batch:
        print(tx)
