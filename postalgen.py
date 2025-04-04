import random
import time
import re
import googlemaps
import shelve

api_key = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=api_key)

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

def main(reversed_result, postalcode, location, i=1):
    word = r"\bSingapore\b"
    with shelve.open("database") as db:
        last_key = max(map(int, db.keys()), default=0)  # Get last key or 0 if empty
        i = last_key + 1
        while True:
            if reversed_result:
                for place in reversed_result:
                    formatted_address = place.get("formatted_address")
                    if formatted_address != '9R29+RW Singapore':
                        formatted_address = place.get("formatted_address")
                        index = re.search(word, formatted_address).end()
                        if postalcode == formatted_address[index+1:]:
                            print("\n")
                            print(f"Coordinates for {postalcode}: {location}")
                            print(formatted_address)
                            url = "https://www.google.com/maps/place/?q=place_id:"+ reversed_result[0].get("place_id")
                            print(url)
                            print("\n")
                            print(place)

                            db[str(i)] = {
                                "Postal Code": postalcode,
                                "Location": location,
                                "Address": formatted_address,
                                "Location URL":  url,
                                "Place": place
                            }
                            i += 1
                            
                            while True:
                                continuation = input("\nPrint, exit or continue? ")
                                if continuation == "exit":
                                    exit()
                                elif continuation == "print":
                                    for key, value in db.items():
                                        print(f"Key: {key}")
                                        print("Value:", value)
                                        print("\n")
                                    continue
                        time.sleep(0.3)
                        new_postalcode = postalgen()
                        new_location = geocoding(new_postalcode)
                        new_reversed_result = reverse_geocoding(new_location)
                        main(new_reversed_result, new_postalcode, new_location, i)
                        
postalcode = postalgen()
location = geocoding(postalcode)
reversed_result = reverse_geocoding(location)
main(reversed_result, postalcode, location)
