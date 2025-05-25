#!/usr/bin/env python3
import sys


def compute_averages():
    total_fare = total_distance = total_duration = count = 0

    for line in sys.stdin:
        key, value = line.strip().split("\t")
        fare, distance, duration = map(float, value.split(","))
        total_fare += fare
        total_distance += distance
        total_duration += duration
        count += 1

    if count > 0:
        avg_fare = total_fare / count
        avg_distance = total_distance / count
        avg_duration = total_duration / count
        print(f"Average Fare: {avg_fare:.2f}")
        print(f"Average Distance: {avg_distance:.2f} miles")
        print(f"Average Duration: {avg_duration:.2f} minutes")
    else:
        print("No valid data found.")


if __name__ == "__main__":
    compute_averages()
