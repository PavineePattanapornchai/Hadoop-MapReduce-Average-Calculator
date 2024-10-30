# Hadoop MapReduce Average Calculator

## Overview
This project demonstrates the use of Hadoop MapReduce to calculate the average value from a given dataset. By using Hadoop Streaming, the Python-based mapper and reducer scripts process the data in a distributed manner across a Hadoop cluster, showcasing how large datasets can be handled efficiently.

The mapper script reads and processes the input data by summing the numbers in each line and counting the total number of values. The reducer script aggregates these sums and counts from the mapper and calculates the overall average.

## Key Features
- **Hadoop Streaming**: Utilizes Hadoop Streaming to run custom Python code as mapper and reducer tasks within the Hadoop framework.
- **Mapper**: The mapper script processes each line of data, outputting the sum and count of numbers.
- **Reducer**: The reducer script aggregates the results from the mappers and calculates the final average.
- **Distributed Computation**: Takes advantage of Hadoop's distributed architecture to handle large datasets.

## Files
- `average_mapper.py`: Python script that acts as the mapper, reading lines from the input and calculating the sum and count of numbers.
- `average_reducer.py`: Python script that acts as the reducer, aggregating the sum and count from the mapper output and calculating the average.
- `test.dat`: Sample dataset file used to demonstrate the calculation process.

## How to Run
1. **Install Hadoop**: Ensure Hadoop is installed and properly configured on your machine or cluster. You can download Hadoop from [Apache Hadoop](https://hadoop.apache.org/releases.html).
   ```bash
   wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
   tar -xzf hadoop-3.3.6.tar.gz
