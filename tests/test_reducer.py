import subprocess

def test_reducer():
    test_input = "trip\t10.0,2.5,15.0\ntrip\t20.0,5.0,30.0\n"
    process = subprocess.Popen(['python', 'src/reducer.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = process.communicate(input=test_input)

    assert "Average Fare:" in stdout, "Reducer output missing average fare"
    assert "Average Distance:" in stdout, "Reducer output missing average distance"
    assert "Average Duration:" in stdout, "Reducer output missing average duration"

if __name__ == "__main__":
    test_reducer()
    print("Reducer test passed.")
