from fastapi import FastAPI
import requests
import sqlite3
import csv

DATA_URL = "https://www.datakhk.cz/api/download/v1/items/3ec5df3a89d7470ea40330baadca74f4/csv?layers=0"

app = FastAPI()

def map_data(row):
    return {
        "name": row[0],
        "district": row[1],
        "zip_code": row[2],
        "web": row[3]
    }

@app.get("/obce")
def get_obce(district: str, zip_code: str):
    conn = sqlite3.connect("data.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT name, district, zip_code, web FROM data WHERE district = ? AND zip_code = ?", (district, zip_code))
    data = cursor.fetchall()

    return list(map(map_data,data))

def import_data():
    print("Importing data...")
    # Download data from DATA_URL and save to sqlite database
    response = requests.get(DATA_URL)

    # Create sqlite database
    conn = sqlite3.connect("data.sqlite")
    cursor = conn.cursor()

    # Create table
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, district TEXT, zip_code TEXT, web TEXT)")

    # Insert data
    csv_file = response.text.splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute("INSERT INTO data (name, district, zip_code, web) VALUES (?, ?, ?, ?)", (row["Název obce"], row["Název okresu"], row["PSČ"], row["Webové stránky"]))
    conn.commit()
    
    print("Data imported.")

import_data()