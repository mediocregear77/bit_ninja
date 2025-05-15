// frontend/app.js
// Controls Bitcoin_Ninja GPU Dashboard actions

const api = "http://localhost:5000"; // Change if deployed remotely

async function fetchEntropy() {
  try {
    const res = await fetch(`${api}/entropy`);
    const data = await res.json();
    document.getElementById("entropy").textContent =
      `Entropy Score: ${data.average_entropy}`;
  } catch (err) {
    alert("Failed to fetch entropy.");
  }
}

async function runBenchmark() {
  try {
    const res = await fetch(`${api}/benchmark`);
    const data = await res.json();
    document.getElementById("tps").textContent =
      `TPS: ${data.TPS_estimate} (in ${data.signature_batch_time}s)`;
  } catch (err) {
    alert("Benchmark failed.");
  }
}

async function mineBlock() {
  try {
    const res = await fetch(`${api}/mine`, { method: "POST" });
    const data = await res.json();
    document.getElementById("block").textContent =
      `Block ID: ${data.block_id}`;
  } catch (err) {
    alert("Block mining failed.");
  }
}

async function rollup() {
  try {
    const res = await fetch(`${api}/rollup`, { method: "POST" });
    const data = await res.json();
    document.getElementById("rollup").textContent =
      `ZK Proof Root: ${data.proof}`;
  } catch (err) {
    alert("Rollup failed.");
  }
}
