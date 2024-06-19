#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):

    try:
        # Read the CSV file and convert each row into a dictionary
        with open(csv_filename, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON
        with open("data.json", mode="w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
