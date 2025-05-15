# tests/test_tps.py
# Full TPS benchmark for Bitcoin_Ninja GPU core

from core.schnorr_gpu import SchnorrGPUVerifier
import os
import time

def run_tps_benchmark(batch_size=4096):
    verifier = SchnorrGPUVerifier()
    pubkeys = [os.urandom(32) for _ in range(batch_size)]
    msgs = [os.urandom(32) for _ in range(batch_size)]
    sigs = [os.urandom(32) for _ in range(batch_size)]

    print(f"[*] Running TPS benchmark with batch size {batch_size}...")

    start = time.time()
    results = verifier.verify_batch(pubkeys, msgs, sigs)
    end = time.time()

    elapsed = end - start
    tps = round(batch_size / elapsed, 2)

    print(f"[✔] Completed in {round(elapsed, 4)} seconds")
    print(f"[🚀] GPU TPS: {tps}")
    return tps

if __name__ == "__main__":
    run_tps_benchmark()
