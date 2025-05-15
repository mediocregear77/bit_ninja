# tests/test_entropy.py
# Unit test for GPU-based entropy scoring

from core.entropy_engine import EntropyEngine
import numpy as np

def test_entropy_sample():
    engine = EntropyEngine()

    print("[*] Running entropy sampling...")
    values = engine.sample_entropy_distribution()
    
    avg = round(np.mean(values), 6)
    std_dev = round(np.std(values), 6)
    min_val = round(np.min(values), 6)
    max_val = round(np.max(values), 6)

    print(f"Entropy Samples: {len(values)}")
    print(f"Average: {avg}")
    print(f"Std Dev: {std_dev}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    
    # Validation range (expected range: 1.0–1.8)
    assert 0.5 <= avg <= 2.5, "Entropy average out of range"
    assert min_val > 0, "Minimum entropy too low"
    assert max_val <= 5.0, "Maximum entropy too high"
    print("[✔] Entropy test passed.")

if __name__ == "__main__":
    test_entropy_sample()
