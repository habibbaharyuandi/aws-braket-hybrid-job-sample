import json
import subprocess
from pathlib import Path

from braket.circuits import Circuit
from braket.devices import LocalSimulator


def run_linux_script():
    """Execute a bash script from inside the Python hybrid job."""
    print("Menjalankan script Linux...")
    result = subprocess.run(
        ["bash", "-lc", "./run.sh"],
        capture_output=True,
        text=True,
        check=True,
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)


def run_quantum_job():
    """Run a simple quantum circuit with the local Braket simulator."""
    circuit = Circuit().h(0).measure(0)
    device = LocalSimulator()

    task = device.run(circuit, shots=100)
    result = task.result()
    counts = result.measurement_counts

    print("Measurement counts:", counts)

    output_path = Path("/tmp") / "quantum_output.json"
    with open(output_path, "w") as f:
        json.dump({"counts": dict(counts), "shots": 100}, f, indent=2)

    print(f"Output disimpan di: {output_path}")


def main():
    run_linux_script()
    run_quantum_job()

    final_output = {
        "status": "success",
        "message": "Hybrid job berhasil dijalankan"
    }

    final_path = Path("/tmp") / "final_output.json"
    with open(final_path, "w") as f:
        json.dump(final_output, f, indent=2)

    print(json.dumps(final_output, indent=2))


if __name__ == "__main__":
    main()
