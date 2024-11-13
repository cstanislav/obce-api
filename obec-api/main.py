from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests
import psycopg2
import csv

DATA_URL = "https://www.datakhk.cz/api/download/v1/items/3ec5df3a89d7470ea40330baadca74f4/csv?layers=0"

DB_HOST = "postgres"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "postgres"

def get_database_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS
    )

app = FastAPI()

def map_data(row):
    return {
        "id": row[0],
        "name": row[1],
        "district": row[2],
        "zip_code": row[3],
        "web": row[4]
    }

@app.get("/obce")
def get_obce(district: str, zip_code: str):
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, district, zip_code, web FROM data WHERE district = %s AND zip_code = %s", (district, zip_code))
    data = cursor.fetchall()
    conn.close()

    return list(map(map_data,data))

# Serve static files from /client
app.mount("/", StaticFiles(directory="client", html=True), name="client")

def import_data():
    print("Importing data...")
    # Download data from DATA_URL and save to sqlite database
    response = requests.get(DATA_URL)

    # Create PostgreSQL database
    conn = get_database_connection()
    cursor = conn.cursor()

    # Drop table if exists
    cursor.execute("DROP TABLE IF EXISTS data")

    # Create table
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id SERIAL PRIMARY KEY, name TEXT, district TEXT, zip_code TEXT, web TEXT)")

    # Insert data
    csv_file = response.text.splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute("INSERT INTO data (name, district, zip_code, web) VALUES (%s, %s, %s, %s)", (row["Název obce"], row["Název okresu"], row["PSČ"], row["Webové stránky"]))
    conn.commit()
    conn.close()
    
    print("Data imported.")

import_data()