import googlemaps

pid = []

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyCF67qwGMRHJ7m2jxYxWobQikwvU1bXUWs')

query = "restaurants in Singapore"
places = gmaps.places(query)

# If there are results, print them
if places.get("results"):
    for place in places["results"]:
        print(place.get("name"))
        print(place.get("formatted_address"))
        print(place.get("geometry").get("location"))
        print(place.get("place_id"))
        print("\n")
        
else:
    print("No results found.")

# Print the results
print(pid)

#https://www.google.com/maps/place/?q=place_id:PLACEID
for i in range(len(pid)):
    print("https://www.google.com/maps/place/?q=place_id:"+pid[i])
