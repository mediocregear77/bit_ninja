# server/routes/mine.py
# Modular route to simulate mining a block using DAG + entropy

from flask import Blueprint, jsonify
from core.dag_consensus import DAGGraph
from core.entropy_engine import EntropyEngine

mine_route = Blueprint("mine_route", __name__)

dag = DAGGraph()
entropy = EntropyEngine()

@mine_route.route("/mine", methods=["POST"])
def mine_entropy_block():
    """
    Simulate the creation of a new DAG node based on entropy.
    """
    new_block = dag.simulate_entropy_block()

    return jsonify({
        "block_id": new_block.id,
        "timestamp": new_block.timestamp,
        "tx_root": new_block.tx_root,
        "entropy_score": new_block.entropy_score,
        "valid": new_block.valid,
        "parent_ids": new_block.parent_ids
    })
