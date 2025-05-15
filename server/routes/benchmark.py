# server/routes/benchmark.py
# Benchmarking route to profile GPU speed (TPS, entropy score)

from flask import Blueprint, jsonify
from core.entropy_engine import EntropyEngine
from core.schnorr_gpu import SchnorrGPUVerifier
import time
import os

benchmark_route = Blueprint("benchmark_route", __name__)

entropy = EntropyEngine()
verifier = SchnorrGPUVerifier()

@benchmark_route.route("/benchmark", methods=["GET"])
def run_benchmark():
    """
    Runs a benchmark using GPU entropy scoring and batch Schnorr verification.
    Measures TPS and entropy rate.
    """
    start_time = time.time()

    # Generate mock inputs
    pubkeys = [os.urandom(32) for _ in range(1024)]
    msgs = [os.urandom(32) for _ in range(1024)]
    sigs = [os.urandom(32) for _ in range(1024)]

    entropy_score = entropy.measure_entropy()

    sig_start = time.time()
    results = verifier.verify_batch(pubkeys, msgs, sigs)
    sig_end = time.time()

    end_time = time.time()
    duration = round(end_time - start_time, 4)
    sig_time = round(sig_end - sig_start, 4)

    tps = round(len(results) / sig_time, 2)

    return jsonify({
        "total_time": duration,
        "signature_batch_time": sig_time,
        "signature_verifications": len(results),
        "TPS_estimate": tps,
        "entropy_score": entropy_score
    })
