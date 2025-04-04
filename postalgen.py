import random
import googlemaps
 
districtcode = random.randint(1, 82)
if districtcode < 10:
    districtcode = "0" + str(districtcode)
inbetweencode = random.randint(0, 8)
sectorcode = random.randint(1, 999)

postalcode = str(districtcode) + str(inbetweencode) + str(sectorcode)

api_key = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=api_key)

geocode_result = gmaps.geocode(postalcode + ", Singapore")
if not geocode_result:
    print("No location found for this postal code.")
    exit()

location = geocode_result[0].get("geometry", {}).get("location")

reversed_result = gmaps.reverse_geocode((location.get("lat"), location.get("lng")))

if reversed_result:
    for place in reversed_result:
        formatted_address = place.get("formatted_address")
        if formatted_address == '9R29+RW Singapore':
            break
        else:
            print(f"Coordinates for {postalcode}: {location}")
            print(place.get("formatted_address"))
            print("https://www.google.com/maps/place/?q=place_id:"+ geocode_result[0].get("place_id"))
