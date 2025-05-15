# run_benchmark.py
# End-to-end GPU benchmark for Bitcoin_Ninja_GPU system

from core.schnorr_gpu import SchnorrGPUVerifier
from core.entropy_engine import EntropyEngine
from core.zk_batcher import ZKRollupBatcher
import os
import time

def main():
    print("\n=== Bitcoin_Ninja_GPU Benchmark ===\n")

    # Initialize modules
    verifier = SchnorrGPUVerifier()
    entropy = EntropyEngine()
    zk = ZKRollupBatcher()

    # --- Entropy Benchmark ---
    print("[*] Running entropy benchmark...")
    start_entropy = time.time()
    avg_entropy = entropy.measure_entropy()
    end_entropy = time.time()
    entropy_time = round(end_entropy - start_entropy, 4)
    print(f"[✔] Entropy Score: {avg_entropy} in {entropy_time}s")

    # --- Schnorr Signature Verification Benchmark ---
    print("\n[*] Running Schnorr batch verification...")
    count = 2048
    pubkeys = [os.urandom(32) for _ in range(count)]
    msgs = [os.urandom(32) for _ in range(count)]
    sigs = [os.urandom(32) for _ in range(count)]

    start_sig = time.time()
    results = verifier.verify_batch(pubkeys, msgs, sigs)
    end_sig = time.time()
    sig_time = round(end_sig - start_sig, 4)
    tps = round(count / sig_time, 2)
    print(f"[✔] Verified {count} signatures in {sig_time}s")
    print(f"[🚀] Estimated GPU TPS: {tps}")

    # --- ZK Rollup Benchmark ---
    print("\n[*] Running ZK rollup compression...")
    txs = [os.urandom(32) for _ in range(zk.batch_size)]
    start_zk = time.time()
    rollup = zk.batch_and_prove(txs)
    end_zk = time.time()
    zk_time = round(end_zk - start_zk, 4)
    print(f"[✔] Rollup Hash: {rollup['proof']}")
    print(f"[🌀] ZK Time: {zk_time}s for {zk.batch_size} tx")

    print("\n=== Benchmark Complete ===")

if __name__ == "__main__":
    main()
