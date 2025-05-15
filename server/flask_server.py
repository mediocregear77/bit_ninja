# server/flask_server.py
# Flask-based control server for Bitcoin_Ninja GPU core

from flask import Flask, jsonify, request
from core.entropy_engine import EntropyEngine
from core.dag_consensus import DAGGraph
from core.schnorr_gpu import SchnorrGPUVerifier
from core.zk_batcher import ZKRollupBatcher
import random
import os

app = Flask(__name__)

entropy_engine = EntropyEngine()
dag = DAGGraph()
verifier = SchnorrGPUVerifier()
zk = ZKRollupBatcher()

@app.route("/")
def home():
    return jsonify({
        "system": "Bitcoin_Ninja GPU Core",
        "version": "v2.0",
        "status": "running"
    })

@app.route("/mine", methods=["POST"])
def mine_entropy_block():
    node = dag.simulate_entropy_block()
    return jsonify({
        "block_id": node.id,
        "entropy": node.entropy_score,
        "valid": node.valid,
        "parents": node.parent_ids
    })

@app.route("/entropy", methods=["GET"])
def entropy_check():
    average = entropy_engine.measure_entropy()
    return jsonify({
        "average_entropy": average
    })

@app.route("/rollup", methods=["POST"])
def rollup():
    txs = [os.urandom(32) for _ in range(zk.batch_size)]
    result = zk.batch_and_prove(txs)
    return jsonify(result)

@app.route("/verify", methods=["POST"])
def verify_batch():
    try:
        data = request.get_json()
        pubkeys = [bytes.fromhex(p) for p in data["pubkeys"]]
        msgs = [bytes.fromhex(m) for m in data["msgs"]]
        sigs = [bytes.fromhex(s) for s in data["sigs"]]
        results = verifier.verify_batch(pubkeys, msgs, sigs)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/status", methods=["GET"])
def system_status():
    return jsonify({
        "entropy": entropy_engine.measure_entropy(),
        "dag_nodes": len(dag.nodes),
        "latest_blocks": [b.id for b in dag.get_latest_valid_chain()]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
