import json
import csv

def create_routes(filepath="routes.json"):
    data = {
        "routes": [
            {"route_id": "R01", "from": "Jenin",    "to": "AAUP", "departure": "07:30", "return": "16:00", "capacity": 30},
            {"route_id": "R02", "from": "Nablus",   "to": "AAUP", "departure": "07:00", "return": "16:00", "capacity": 25},
            {"route_id": "R03", "from": "Tulkarm",  "to": "AAUP", "departure": "07:15", "return": "16:00", "capacity": 35},
            {"route_id": "R04", "from": "Qalqilya", "to": "AAUP", "departure": "07:45", "return": "16:00", "capacity": 20},
        ]
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Routes saved: {filepath}")

def create_reservations(filepath="reservations.csv"):
    rows = [
        ["res_id",  "student_name",       "student_id", "route_id", "date"],
        ["RES001",  "Ahmad Salameh",       "202200101",  "R01",      "2026-05-15"],
        ["RES002",  "Nour Khalil",         "202200102",  "R01",      "2026-05-15"],
        ["RES003",  "Sara Hassan",         "202200103",  "R02",      "2026-05-15"],
        ["RES004",  "Yousef Awad",         "202200104",  "R03",      "2026-05-15"],
        ["RES005",  "Rania Mahmoud",       "202200105",  "R03",      "2026-05-15"],
        ["RES006",  "Khaled Nasser",       "202200106",  "R03",      "2026-05-15"],
        ["RES007",  "Dina Abu Zaid",       "202200107",  "R01",      "2026-05-16"],
        ["RES008",  "Lara Hijazi",         "202200108",  "R02",      "2026-05-16"],
        ["RES009",  "Faris Barakat",       "202200109",  "R04",      "2026-05-16"],
        ["RES010",  "Hana Odeh",           "202200110",  "R01",      "2026-05-16"],
    ]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Reservations saved: {filepath}")

if __name__ == "__main__":
    create_routes()
    create_reservations()