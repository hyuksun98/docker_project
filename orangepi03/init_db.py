import sqlite3
import subprocess
import os

db_file = "/app/orangepi03/data/broker.db"

conn = sqlite3.connect(db_file)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS dht (
id INTEGER PRIMARY KEY,
topic TEXT,
temperature REAL,
humidity REAL
);
"""

cursor.execute(create_table_query)

conn.commit()

conn.close()

print("Database initialization completed.")

subprocess.run(["python3", "mqtt_broker.py"])
