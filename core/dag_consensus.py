# core/dag_consensus.py
# DAG-based Proof-of-Computation consensus engine

import time
import hashlib
import uuid
import random
from collections import defaultdict

class DAGNode:
    def __init__(self, tx_root, entropy_score, parent_ids):
        self.id = str(uuid.uuid4())
        self.timestamp = time.time()
        self.tx_root = tx_root
        self.entropy_score = entropy_score
        self.parent_ids = parent_ids
        self.children = []
        self.valid = False

    def compute_link_weight(self, parent_node):
        age = self.timestamp - parent_node.timestamp
        if age <= 0:
            age = 0.001
        return self.entropy_score / age

class DAGGraph:
    def __init__(self):
        self.nodes = {}
        self.genesis = self.create_genesis()

    def create_genesis(self):
        root = DAGNode("GENESIS", entropy_score=1.0, parent_ids=[])
        root.valid = True
        self.nodes[root.id] = root
        return root

    def add_node(self, tx_root, entropy_score, parent_ids):
        node = DAGNode(tx_root, entropy_score, parent_ids)
        for pid in parent_ids:
            parent = self.nodes.get(pid)
            if parent:
                parent.children.append(node)
        self.nodes[node.id] = node
        return node

    def validate_node(self, node_id):
        node = self.nodes.get(node_id)
        if not node:
            return False

        # Validate based on entropy threshold and link weight
        weights = []
        for pid in node.parent_ids:
            parent = self.nodes.get(pid)
            if not parent:
                continue
            weight = node.compute_link_weight(parent)
            weights.append(weight)

        if weights and min(weights) > 0.25:  # Threshold is tunable
            node.valid = True
        return node.valid

    def get_latest_valid_chain(self, depth=10):
        valid_nodes = [n for n in self.nodes.values() if n.valid]
        valid_nodes.sort(key=lambda n: n.timestamp, reverse=True)
        return valid_nodes[:depth]

    def simulate_entropy_block(self):
        entropy = random.uniform(0.1, 2.0)
        fake_tx_root = hashlib.sha256(str(time.time()).encode()).hexdigest()
        parents = self.get_latest_valid_chain(depth=2)
        parent_ids = [p.id for p in parents]
        new_node = self.add_node(fake_tx_root, entropy_score=entropy, parent_ids=parent_ids)
        self.validate_node(new_node.id)
        return new_node

