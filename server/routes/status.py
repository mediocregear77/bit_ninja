# server/routes/status.py
# System status endpoint for DAG health and entropy summary

from flask import Blueprint, jsonify
from core.entropy_engine import EntropyEngine
from core.dag_consensus import DAGGraph

status_route = Blueprint("status_route", __name__)

entropy = EntropyEngine()
dag = DAGGraph()

@status_route.route("/status", methods=["GET"])
def get_system_status():
    """
    Returns current DAG stats, entropy score, and latest valid block chain.
    """
    current_entropy = entropy.measure_entropy()
    latest_chain = dag.get_latest_valid_chain(depth=5)

    return jsonify({
        "status": "online",
        "entropy_score": current_entropy,
        "dag_nodes": len(dag.nodes),
        "latest_valid_blocks": [
            {
                "id": node.id,
                "timestamp": node.timestamp,
                "entropy": node.entropy_score
            }
            for node in latest_chain
        ]
    })
