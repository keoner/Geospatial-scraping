import random
import time
import re
import googlemaps
import json

landmarks = ["Grocery store", "School", "Hospital", "MRT/LRT Station", "Restaurant", "Park", "Bus Stop"]
filterList = ["Blk", "Bef", "Aft", "Before", "After", "Dr", "Opp", "Rd", "Near", "Beside", "Ave",
            "Carpark", "Car Park", "Lor", "Condo", "Est", "Estate", "St", "Jct", "Cres"]
api_key = "AIzaSyD3kbEbVvFHBbS9iIQNaQuDDSViQxylyu4"  # Replace with your actual API key'
gmaps = googlemaps.Client(key=api_key)

with open("bus_routes.json", "r", encoding="utf-8") as f:
    bus_routes_data = json.load(f)
with open("bus_stops.json", "r", encoding="utf-8") as f:
    bus_stop_data = json.load(f)

def postalgen():
    districtcode = random.randint(1, 82)
    if districtcode < 10:
        districtcode = "0" + str(districtcode)
    inbetweencode = random.randint(1, 5)
    sectorcode = random.randint(100, 700)

    postalcode = str(districtcode) + str(inbetweencode) + str(sectorcode)
    return postalcode

def geocoding(postalcode):
    geocode_result = gmaps.geocode(postalcode + ", Singapore")
    location = geocode_result[0].get("geometry", {}).get("location")
    if not geocode_result:
        print("No location found for this postal code.")
        exit()
    return location

def reverse_geocoding(location):
    reversed_result = gmaps.reverse_geocode((location.get("lat"), location.get("lng")))
    return reversed_result

def get_bus_stops(description):
    bus_stops = [item for item in bus_stop_data if item["Description"] == description]
    servicing_buses = [item for item in bus_routes_data if item["BusStopCode"] == bus_stops[0]["BusStopCode"]]
    buses = [item["ServiceNo"] for item in servicing_buses]
    print(f"The bus services for bus stop, {description} are {buses}")
    print("\n")
    return buses

def get_major_routes(buses):
    for i in range(len(buses)):
        bus_codes = [item["BusStopCode"] for item in bus_routes_data if item["ServiceNo"] == buses[i]]
        bus_stop_names = [stop["Description"] for stop in bus_stop_data if stop["BusStopCode"] in bus_codes]
        major_routes = [name for name in bus_stop_names if not any(filter.lower() in name.lower() for filter in filterList)]
        print(f"Major routes for bus service {buses[i]} are at {major_routes}")
        print("\n")

def main(reversed_result, postalcode, origin_location, i=1):
    word = r"\bSingapore\b"
    if reversed_result:
        for place in reversed_result:
            formatted_address = place.get("formatted_address")
            if formatted_address != '9R29+RW Singapore':
                formatted_address = place.get("formatted_address")
                index = re.search(word, formatted_address).end()
                if postalcode == formatted_address[index+1:]:
                    print("\n")
                    print(f"Coordinates for {postalcode}: {origin_location}")
                    print(f"Name: {gmaps.place(place_id=reversed_result[0].get("place_id"))['result'].get("name")}")
                    print(f"Human-Readable Address: {formatted_address}")
                    print("https://www.google.com/maps/place/?q=place_id:"+ reversed_result[0].get("place_id"))
                    print("\n")
                    print(place)
                    input("Press Enter to continue...")
                    print("\n")
                    count = 0
                    while count < len(landmarks):
                        if count <= 3:
                            mode = "driving"
                        else:
                            mode = "walking"
                        
                        results = gmaps.places_nearby(location=origin_location, keyword=landmarks[count], rank_by="distance")
                        places = results["results"][0]
                        landmark_location = gmaps.reverse_geocode((places.get("geometry").get("location")))

                        print(f"{landmarks[count]}: {places.get('name')}")
                        print(landmark_location[0].get("formatted_address"))
                        print("https://www.google.com/maps/place/?q=place_id:"+ places.get("place_id"))
                        distance_result = gmaps.distance_matrix(origins=[origin_location], destinations=[landmark_location[0].get("formatted_address")], mode=mode)
                        distance_info = distance_result['rows'][0]['elements'][0]
                        print(f"Distance: {distance_info.get('distance', {}).get('text', 'N/A')}")
                        print(f"Duration: {distance_info.get('duration', {}).get('text', 'N/A')}")
                        count += 1
                        input("Press Enter to continue...")
                        print("\n")

                    stops = get_bus_stops(places.get('name'))
                    get_major_routes(stops)
                    
                    if input("Enter to continue, 'exit' to leave") == "exit":
                        exit()

                time.sleep(0.3)
                new_postalcode = postalgen()
                new_location = geocoding(new_postalcode)
                new_reversed_result = reverse_geocoding(new_location)
                main(new_reversed_result, new_postalcode, new_location, i)

postalcode = postalgen()
location = geocoding(postalcode)
reversed_result = reverse_geocoding(location)
main(reversed_result, postalcode, location)