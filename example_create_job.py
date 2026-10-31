import os
import boto3


def upload_files_to_s3(bucket: str, prefix: str):
    s3 = boto3.client("s3")

    for filename in ["hybrid_job.py", "run.sh", "requirements.txt"]:
        key = f"{prefix}/{filename}"
        s3.upload_file(filename, bucket, key)
        print(f"Uploaded: s3://{bucket}/{key}")


def create_braket_job(bucket: str, prefix: str, role_arn: str):
    braket = boto3.client("braket", region_name="us-west-2")

    response = braket.create_job(
        jobName="demo-hybrid-job",
        roleArn=role_arn,
        deviceConfig={
            "deviceArn": "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
        },
        outputConfig={
            "s3Path": f"s3://{bucket}/{prefix}/output/"
        },
        scriptModeConfig={
            "entryPoint": "hybrid_job.py",
            "sourceFileLocation": f"s3://{bucket}/{prefix}/"
        },
    )

    print(response)


if __name__ == "__main__":
    bucket = "my-braket-bucket"
    prefix = "braket-demo"
    role_arn = "arn:aws:iam::123456789012:role/BraketHybridJobRole"

    upload_files_to_s3(bucket, prefix)
    create_braket_job(bucket, prefix, role_arn)
