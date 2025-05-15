#!/bin/bash
# tests/run_all.sh
# Unified test runner for Bitcoin_Ninja_GPU

echo "=== Bitcoin_Ninja GPU Test Suite ==="
echo "[*] Starting test run..."

TESTS=(
    "test_entropy.py"
    "test_schnorr.py"
    "test_tps.py"
)

cd "$(dirname "$0")"

for test in "${TESTS[@]}"; do
    echo ">> Running $test"
    python3 "$test"
    if [ $? -ne 0 ]; then
        echo "[✘] $test FAILED"
        exit 1
    else
        echo "[✔] $test passed"
    fi
done

echo "=== All tests completed successfully ==="
