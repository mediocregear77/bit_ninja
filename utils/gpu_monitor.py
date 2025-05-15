# utils/gpu_monitor.py
# Real-time GPU telemetry using nvidia-smi

import subprocess

def get_gpu_stats():
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=index,name,utilization.gpu,temperature.gpu,memory.used,memory.total,power.draw,power.limit",
             "--format=csv,noheader,nounits"],
            encoding='utf-8'
        )
        stats = []
        for line in output.strip().split('\n'):
            idx, name, util, temp, mem_used, mem_total, power, limit = line.split(', ')
            stats.append({
                "id": int(idx),
                "name": name,
                "utilization": f"{util}%",
                "temperature": f"{temp}°C",
                "memory_used": f"{mem_used} MiB",
                "memory_total": f"{mem_total} MiB",
                "power_draw": f"{power} W",
                "power_limit": f"{limit} W"
            })
        return stats
    except Exception as e:
        return [{"error": str(e)}]

# Optional CLI test
if __name__ == "__main__":
    import json
    print(json.dumps(get_gpu_stats(), indent=2))
