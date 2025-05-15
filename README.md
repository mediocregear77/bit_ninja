# ⚡ Bitcoin_Ninja_GPU
### A Pure GPU-Powered Blockchain Execution Engine — Faster Than Bitcoin, Built for 2025

---

## 🔥 What Is It?
**Bitcoin_Ninja_GPU** is a next-gen blockchain framework built entirely on the GPU. It replaces Bitcoin’s slow, CPU-bound architecture with:

- ⚡ **CUDA-based Schnorr signature verification**
- 🧠 **Entropy-scored DAG consensus**
- 🌀 **ZK rollup batching with GPU hashing**
- 🚀 **14+ TPS baseline throughput (vs Bitcoin’s 7 TPS)**
- 🟠 **Pure GPU — no CPU fallback**

---

## 🧱 Core Features
| Module         | Function                                        |
|----------------|-------------------------------------------------|
| `cuda_kernel.cu`     | Raw CUDA kernels for hashing, entropy, Schnorr  |
| `cuda_wrapper.py`    | PyCUDA interface to launch GPU ops            |
| `dag_consensus.py`   | DAG-based Proof-of-Computation consensus      |
| `zk_batcher.py`      | GPU-based rollup compressor                   |
| `entropy_engine.py`  | Randomness miner for DAG scoring              |
| `flask_server.py`    | REST API to control the engine                |
| `frontend/index.html`| Live dashboard to view performance            |

---

## ⚙️ Requirements

- Python 3.10+
- CUDA 11.8+ (recommended: CUDA 12.2)
- GPU with at least 6 GB VRAM (RTX 3060+ recommended)

```bash
pip install -r requirements.txt
