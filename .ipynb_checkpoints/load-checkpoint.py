import pandas as pd
import sqlite3
import os
import json

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok = True)

def save_to_csv(posts, comments):
    print("saving data - posts to csv")
    pd.DataFrame(posts).to_csv(f"{DATA_DIR}/posts.csv", index = False)
    print("saving data - comments to csv")
    pd.DataFrame(comments).to_csv(f"{DATA_DIR}/comments.csv", index =False)

def save_to_json(data):
    with open(f"{DATA_DIR}/full_data.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 2, ensure_ascii = False)

def save_to_sqlite(posts,comments):
    conn = sqlite3.connect(f"{DATA_DIR}/reddit.db")
    pd.DataFrame(posts).to_sql("posts", conn, if_exists = "append", index = False)
    pd.DataFrame(comments).to_sql("comments", conn, if_exists = "append", index = False)
    conn.close()