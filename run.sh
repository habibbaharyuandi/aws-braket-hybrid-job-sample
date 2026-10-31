#!/bin/bash
set -euxo pipefail

echo "=== Start Linux script ==="
whoami
pwd
uname -a
python3 --version
ls -la

echo "=== End Linux script ==="
