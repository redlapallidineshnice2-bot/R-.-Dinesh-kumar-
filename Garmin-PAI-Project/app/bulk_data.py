import requests
import random

URL = "http://127.0.0.1:8000/garmin-webhook"
subjects = ["n.1", "n.2", "n.3", "n.4", "n.5", "n.6"]

print("Generating 7 months of data for 6 subjects...")

for subject in subjects:
    # Each subject gets 30 entries (simulating weeks or key days)
    for _ in range(30):
        data = {
            "subject_id": subject,
            "steps": random.randint(5000, 15000),
            "floors": random.randint(2, 15),
            "intensity_mins_weekly_avg": random.randint(150, 600),
            "pal": round(random.uniform(1.2, 2.2), 2),
            "active_mins": random.randint(30, 180)
        }
        requests.post(URL, json=data)

print("Done! Database populated.")