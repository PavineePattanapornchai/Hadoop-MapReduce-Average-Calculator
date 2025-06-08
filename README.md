# NYC Taxi Hadoop Analytics

This project demonstrates a scalable data processing pipeline that analyzes New York City taxi trip data using the Hadoop MapReduce paradigm. It supports both local simulation (using Python scripts) and Hadoop streaming for distributed execution. The pipeline extracts and computes average fare, trip distance, and duration from large Parquet datasets.

---

## Project Objectives

* Implement a MapReduce pipeline for large-scale data analytics
* Process Parquet-formatted NYC taxi trip data using Python
* Enable both local and distributed (Hadoop-based) processing workflows
* Maintain modularity, test coverage, and CI automation for reliability

---

## Repository Structure

```
nyc-taxi-hadoop-analytics/
├── data/                      # Parquet data (excluded from Git)
├── src/
│   ├── mapper.py              # Extracts fare, distance, and duration
│   └── reducer.py             # Computes averages from trip metrics
├── scripts/
│   ├── run_hadoop.sh          # Hadoop streaming script (Linux)
│   └── test_local.ps1         # Local simulation script (PowerShell)
├── tests/
│   ├── test_mapper.py         # Unit test for mapper
│   └── test_reducer.py        # Unit test for reducer
├── .github/workflows/ci.yml  # GitHub Actions for CI
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Local Testing (Python Only)

You can simulate the Hadoop streaming behavior locally using this one-liner:

```bash
echo "data/yellow_tripdata_2024-01.parquet" | python src/mapper.py | sort | python src/reducer.py
```

Expected output:

```
Average Fare: 18.18
Average Distance: 3.65 miles
Average Duration: 15.61 minutes
```

---

## Running with Hadoop (Streaming)

To execute on a Hadoop cluster:

1. Update `scripts/run_hadoop.sh` with your `$HADOOP_HOME` and appropriate HDFS paths
2. Run the script:

```bash
bash scripts/run_hadoop.sh
```

---

## Continuous Integration (CI)

The project includes a GitHub Actions workflow:

* Automatically triggered on commits to `main` or pull requests
* Installs Python 3.10 and project dependencies
* Runs `pytest` for unit testing and `flake8` for linting

CI is defined in `.github/workflows/ci.yml`.

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies include:

* `pandas`
* `pyarrow`
* `pytest`
* `flake8`

---

## Future Enhancements

* Add time-based or geographic segmentation analysis
* Support Apache Spark for more scalable processing
* Create visualizations or dashboards
* Integrate with cloud-based storage and pipelines

---

## Author

Pavinee Pattanapornchai
