import random
import time
import googlemaps

found = False
api_key = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=api_key)

def postalgen():
    districtcode = random.randint(1, 82)
    if districtcode < 10:
        districtcode = "0" + str(districtcode)
    inbetweencode = random.randint(1, 5)
    sectorcode = random.randint(100, 500)

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

def main(reversed_result, postalcode, location):
    while found != True:
        if reversed_result:
            for place in reversed_result:
                formatted_address = place.get("formatted_address")
                if formatted_address != '9R29+RW Singapore':
                    print("\n")
                    print(f"Coordinates for {postalcode}: {location}")
                    print(place.get("formatted_address"))
                    print("https://www.google.com/maps/place/?q=place_id:"+ reversed_result[0].get("place_id"))
                    found == True
                    time.sleep(2)
                new_postalcode = postalgen()
                new_location = geocoding(new_postalcode)
                new_reversed_result = reverse_geocoding(new_location)
                main(new_reversed_result, new_postalcode, new_location)
                time.sleep(2)
                        
postalcode = postalgen()
location = geocoding(postalcode)
reversed_result = reverse_geocoding(location)
main(reversed_result, postalcode, location)
