Write-Output "Running local Hadoop simulation (PowerShell)..."

# Use explicit Conda Python path 
$pythonPath = "C:\Users\asus\miniconda3\python.exe"
$parquetFile = "data\yellow_tripdata_2024-01.parquet"

# Run mapper and reducer pipeline
Get-Content $parquetFile | & $pythonPath src\mapper.py | Sort-Object | & $pythonPath src\reducer.py