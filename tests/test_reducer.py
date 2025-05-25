import subprocess

def test_reducer_output():
    # Simulate mapper output
    test_input = "trip\t10.0,5.0,20.0\ntrip\t20.0,10.0,40.0\n"
    process = subprocess.Popen(
        ['python', 'src/reducer.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input=test_input)

    # Check if output contains expected average labels
    assert "Average Fare:" in stdout, "Reducer output missing average fare"
    assert "Average Distance:" in stdout, "Reducer output missing average distance"
    assert "Average Duration:" in stdout, "Reducer output missing average duration"

if __name__ == "__main__":
    test_reducer_output()
    print("test_reducer.py passed.")
