import csv
import os
from datetime import datetime

# 1. Define placeholder data
TREND = "#SimpleIsBetter"
POST_CONTENT = "Pivoted from Google Sheets to a simple CSV file. Sometimes the simplest solution is the best!"
TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. Define output file
CSV_FILE = "posts.csv"

# 3. Check if file exists to determine if we need to write headers
file_exists = os.path.isfile(CSV_FILE)

# Data to be written
row = [TREND, POST_CONTENT, TIMESTAMP]
header = ["Trend", "Post", "Timestamp"]

# 4. & 5. Append data to the CSV file
with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(header)

    writer.writerow(row)

print(f"Successfully appended post to {CSV_FILE}")
