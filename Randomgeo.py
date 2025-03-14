import googlemaps
import time

gmaps = googlemaps.Client(key='YOUR_API_KEY')

query = "821432"
places = gmaps.places(query)

def process_places(places):
    for place in places.get("results", []):
        print(place.get("name"))
        print(place.get("formatted_address"))
        print(place.get("geometry", {}).get("location"))
        print(place.get("place_id"))
        print("\n")

# Process the first page of results
process_places(places)