# AWS Braket Hybrid Job Sample

Sample repository showing how to:
- run a Linux shell script inside a Braket hybrid job
- call Python code from the same job
- execute a simple quantum circuit using Amazon Braket
- store results to a local file and/or S3 output

This is a minimal example for learning and experimentation.

## Files

- `hybrid_job.py` - main Python entrypoint
- `run.sh` - sample Linux shell script called from Python
- `requirements.txt` - Python dependencies
- `example_create_job.py` - example boto3 script to submit the job to Braket
- `README.md` - usage docs

## Prerequisites

- AWS account with access to Amazon Braket
- IAM role that can run Braket hybrid jobs and read/write to S3
- AWS CLI configured or AWS credentials available
- Python 3.9+

## Example structure

```text
.
├── hybrid_job.py
├── run.sh
├── requirements.txt
├── example_create_job.py
└── README.md
```

## Install dependencies locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run locally (without AWS Braket)

```bash
python3 hybrid_job.py
```

This will:
1. execute `run.sh`
2. print Linux environment information
3. run a simple quantum circuit using the local Braket simulator
4. save output to `/tmp/quantum_output.json`

## Upload to S3 and create Braket hybrid job

The file `example_create_job.py` shows an example using `boto3` to upload the source and start a job.

Example flow:

```bash
aws s3 mb s3://my-braket-bucket --region us-west-2
python3 example_create_job.py
```

## Notes

- In Braket Hybrid Jobs, the main entrypoint is usually Python.
- You can still call Linux commands using `subprocess.run(...)` from Python.
- The quantum circuit is executed with Amazon Braket SDK.
- For production workloads, use proper IAM roles, S3 buckets, and monitoring.
