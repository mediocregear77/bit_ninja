# core/entropy_engine.py
# GPU-powered entropy engine for DAG-based Proof-of-Computation

import time
import numpy as np
from core.cuda_wrapper import score_entropy

class EntropyEngine:
    def __init__(self):
        self.sample_count = 512  # Number of entropy samples per scoring run

    def get_entropy_seed(self):
        """
        Uses current time to generate a dynamic entropy seed.
        Can be replaced with hardware entropy or QRNG later.
        """
        return int(time.time_ns() & 0xFFFFFFFFFFFFFFFF)

    def measure_entropy(self):
        """
        Launches the GPU entropy kernel and returns the average score.
        """
        seed = self.get_entropy_seed()
        scores = score_entropy(seed, self.sample_count)
        average = float(np.mean(scores))
        return round(average, 6)

    def sample_entropy_distribution(self):
        """
        Returns full array of entropy values for analysis or DAG visualization.
        """
        seed = self.get_entropy_seed()
        scores = score_entropy(seed, self.sample_count)
        return scores.tolist()
