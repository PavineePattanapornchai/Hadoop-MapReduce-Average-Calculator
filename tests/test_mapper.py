import subprocess

def test_mapper():
    test_file = 'data/yellow_tripdata_2024-01.parquet'
    process = subprocess.Popen(['python', 'src/mapper.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = process.communicate(input=test_file + '\n')

    assert any("trip\t" in line for line in stdout.splitlines()), "Mapper output missing expected key"

if __name__ == "__main__":
    test_mapper()
    print("Mapper test passed.")
