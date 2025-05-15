# main.py
# Entry point for Bitcoin_Ninja_GPU

import argparse
import subprocess
import sys
import os

def run_server():
    print("[*] Launching Flask API server...")
    os.chdir("server")
    subprocess.run(["python3", "flask_server.py"])

def run_benchmark():
    print("[*] Running full system benchmark...")
    subprocess.run(["python3", "run_benchmark.py"])

def run_frontend():
    print("[*] Launching standalone dashboard frontend...")
    os.chdir("frontend")
    subprocess.run(["python3", "server.py"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bitcoin Ninja GPU Launcher")
    parser.add_argument("--server", action="store_true", help="Run the API server")
    parser.add_argument("--benchmark", action="store_true", help="Run performance benchmark")
    parser.add_argument("--frontend", action="store_true", help="Serve dashboard UI")

    args = parser.parse_args()

    if args.server:
        run_server()
    elif args.benchmark:
        run_benchmark()
    elif args.frontend:
        run_frontend()
    else:
        print("Usage:")
        print("  python3 main.py --server     # Run Flask API")
        print("  python3 main.py --benchmark  # Run GPU benchmark")
        print("  python3 main.py --frontend   # Launch UI")
