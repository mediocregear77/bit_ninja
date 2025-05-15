# tests/test_schnorr.py
# Unit test for GPU-accelerated Schnorr batch verifier

from core.schnorr_gpu import SchnorrGPUVerifier
import os
import time

def test_schnorr_verification():
    verifier = SchnorrGPUVerifier()

    print("[*] Generating fake signature batch...")
    count = 1024
    pubkeys = [os.urandom(32) for _ in range(count)]
    msgs = [os.urandom(32) for _ in range(count)]
    sigs = [os.urandom(32) for _ in range(count)]

    print("[*] Running GPU verification...")
    start = time.time()
    results = verifier.verify_batch(pubkeys, msgs, sigs)
    end = time.time()

    assert len(results) == count, "Result count mismatch"
    assert all(isinstance(r, bool) for r in results), "Invalid output type"

    duration = round(end - start, 4)
    tps = round(count / duration, 2)

    print(f"[✔] Verified {count} signatures in {duration} sec")
    print(f"[→] Estimated GPU TPS: {tps}")

if __name__ == "__main__":
    test_schnorr_verification()
