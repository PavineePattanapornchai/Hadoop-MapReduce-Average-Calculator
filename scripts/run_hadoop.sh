#!/bin/bash
INPUT_PATH=/path/to/hdfs/input/yellow_tripdata_2024-01.parquet
OUTPUT_PATH=/path/to/hdfs/output

hadoop fs -rm -r $OUTPUT_PATH

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -file src/mapper.py \
    -file src/reducer.py
