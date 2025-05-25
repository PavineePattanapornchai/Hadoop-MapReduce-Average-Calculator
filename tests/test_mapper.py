import subprocess
import sys

def test_mapper_output():
    # Path to test dataset
    test_file = "data/yellow_tripdata_2024-01.parquet"

    # Use sys.executable to ensure correct Python interpreter is used
    process = subprocess.Popen(
        [sys.executable, 'src/mapper.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input=test_file + '\n')

    # Split and check output lines
    lines = stdout.strip().split('\n')
    assert any(line.startswith("trip\t") for line in lines), "Mapper output missing 'trip' key"

if __name__ == "__main__":
    test_mapper_output()
    print("test_mapper.py passed.")
