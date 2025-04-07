import googlemaps
import time

gmaps = googlemaps.Client(key='YOUr API KEY')

query = "821432, Singapore"
origin = "1 Raffles Place, Singapore"  

geocode_result = gmaps.geocode(query)
if not geocode_result:
    print("No location found for the given postal code.")
    exit()

location = geocode_result[0]['geometry']['location']

places = gmaps.places_nearby(location=location, rank_by="distance", keyword=query)

def process_places(places, origin):
    count = 0
    for place in places.get("results", []):
        name = place.get("name")
        place_location = place.get("geometry", {}).get("location")
        latlng = f"{place_location['lat']},{place_location['lng']}" if place_location else None

        if latlng:
            distance_result = gmaps.distance_matrix(origins=[origin], destinations=[latlng], mode="driving")
            distance_info = distance_result['rows'][0]['elements'][0]
            distance_text = distance_info.get('distance', {}).get('text', 'N/A')
            duration_text = distance_info.get('duration', {}).get('text', 'N/A')
        else:
            distance_text = "N/A"
            duration_text = "N/A"

        print(f"Name: {name}")
        print(f"Location: {latlng}")
        print(f"Distance from origin: {distance_text}")
        print(f"Estimated duration: {duration_text}")
        print(f"Place ID: {place.get('place_id')}")
        print("\n")

        count += 1
        if count >= 40:
            return count
    return count

process_places(places, origin)

