#!/bin/bash

echo "Simulating local Hadoop streaming..."
cat data/yellow_tripdata_2024-01.parquet | python src/mapper.py | sort | python src/reducer.py
