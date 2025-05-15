# utils/logger.py
# Structured JSON logger for Bitcoin_Ninja_GPU

import json
import os
import time
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "logs")
LOG_FILE = os.path.join(LOG_PATH, "ninja_log.jsonl")

# Ensure log folder exists
os.makedirs(LOG_PATH, exist_ok=True)

def log_event(event_type, payload, echo=True):
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": event_type,
        "payload": payload
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    if echo:
        print(f"[{event_type}] {payload}")

# Example usage
if __name__ == "__main__":
    log_event("test", {"message": "Logger online", "entropy": 1.23})
