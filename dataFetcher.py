import requests
import json

API_KEY = "YOUR_API_KEY" # Get API Key from LTA DataMall https://datamall.lta.gov.sg/content/datamall/en.html

whattype = input("What type of data do you want to fetch? (stops/routes): ").strip().lower()
if whattype == "stops":
    base_url = "https://datamall2.mytransport.sg/ltaodataservice/BusStops"
elif whattype == "routes":
    base_url = "https://datamall2.mytransport.sg/ltaodataservice/BusRoutes"
else:
    print("Invalid input. Please enter 'stops' or 'routes'.")
    exit()

headers = {
    "AccountKey": API_KEY,
    "accept": "application/json"
}

all_data = []
skip = 0

while True:
    url = f"{base_url}?$skip={skip}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        break

    data = response.json().get("value", [])
    if not data:
        break

    all_data.extend(data)
    skip += 500
    print(f"Fetching records from {skip-500} to {skip}...")

if whattype == "stops":
    with open("bus_stops.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    print(f" Saved {len(all_data)} bus stop records to 'bus_stops.json'")
else:
    with open("bus_routes.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    print(f" Saved {len(all_data)} bus route records to 'bus_routes.json'")
