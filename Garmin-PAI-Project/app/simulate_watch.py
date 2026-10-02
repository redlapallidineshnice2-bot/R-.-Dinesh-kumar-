import requests

# This URL matches your running Uvicorn server
URL = "http://127.0.0.1:8000/garmin-webhook"

# Simulated data for a participant (Subject n.1) 
# Based on the metrics from Table I of the paper
data = {
    "subject_id": "n.1",
    "steps": 12500,           # Target was 10,000
    "floors": 12,              # Target was 8
    "intensity_mins_weekly_avg": 400, # Target was 450 (300 mod + 150 vig)
    "pal": 1.9,                # Target was 1.85
    "active_mins": 135         # Target was 120
}

print(f"Sending data to IoT Platform: {data}")

try:
    response = requests.post(URL, json=data)
    if response.status_code == 200:
        result = response.json()
        print("\n--- Experiment Results ---")
        print(f"Status: {result['status']}")
        print(f"Calculated Daily PAI Score: {result['calculated_pai']}%")
    else:
        print(f"Error: Server returned status code {response.status_code}")
except Exception as e:
    print(f"Connection failed: {e}")