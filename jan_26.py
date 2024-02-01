import json
import sqlite3
from pathlib import Path

json_content = Path("movies.json").read_text()
movies = json.loads(json_content)

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES (?, ?, ?)"
    for movie in movies:
        values = (movie['title'], movie['genre'])
        conn.execute(command, values)
    conn.commit()

# Not working
