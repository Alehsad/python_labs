from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

print("JSON -> CSV ...")
json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")

print("CSV -> JSON ...")
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")

print("CSV -> XLSX ...")
csv_to_xlsx("data/samples/cities.csv", "data/out/people.xlsx")

print("ГОТОВО")
