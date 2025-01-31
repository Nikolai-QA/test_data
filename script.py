import json
import csv
from files import JSON_FILE_PATH, CSV_FILE_PATH
from csv import DictReader

# Читаем пользователей из JSON
with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

# Читаем книги из CSV
books = []
with open(CSV_FILE_PATH, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        books.append({
            "title": row["Title"],
            "author": row["Author"],
            "genre": row["Genre"],
            "pages": int(row["Pages"]),
            "publisher": row["Publisher"]
        })

# Распределяем книги по пользователям
result = []
for i, user in enumerate(users):
    result.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": books[i::len(users)]  # Равномерное распределение книг
    })

# Сохраняем результат в result.json
with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

