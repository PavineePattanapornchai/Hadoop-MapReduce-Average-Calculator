# Simulate Hadoop streaming by passing the file path to mapper.py
Write-Output "Running local Hadoop simulation (PowerShell)..."

# Define Python path and dataset
$pythonPath = "C:\Users\asus\miniconda3\python.exe"
$parquetFile = "data\yellow_tripdata_2024-01.parquet"

# Run mapper with file path as stdin input, sort, pass to reducer
$parquetFile | & $pythonPath src\mapper.py | Sort-Object | & $pythonPath src\reducer.py
