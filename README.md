# Google Maps API Workshop

This workshop introduces participants to the practical application of Google Maps APIs for building robust, location-based services. Attendees will gain hands-on experience working with three core APIs:

📍Places API – Enables applications to search for places of interest based on geographic location, such as restaurants, landmarks, or businesses. Participants will learn how to retrieve detailed information including place names, categories, and more.

📏Distance Matrix API – Facilitates the calculation of travel distance and duration between origin and destination points. A useful addition into your application to see the distance & duration it takes to travel.

🗺️Geocoding API – Allows applications to convert street addresses into coordinates, and coordinates back into readable addresses. This is essential for applications that require mapping, location tagging, or address validation.

By the end of the workshop, participants will have a solid understanding of how to integrate these APIs into web or mobile applications, along with best practices for handling API requests and responses securely and efficiently.

<br>

## Prerequisites

Before participating in the Google Maps API Workshop, please ensure the following software and libraries are installed on your device:

1. **Code Editor**
   - A code editor such as **VSCode**, **PyCharm**, or any other of your preference for writing Python code.
   
2. **Python**
   - Python version **3.6** or higher. You can download it from the [official Python website](https://www.python.org/downloads/).

3. **Google Maps Python Library**
   - Install the official **Google Maps Python client library** by running the following command in your terminal:

```
pip install -U googlemaps
```

<br>

## Setting Up Your Google Cloud Project

Before you can start using the Google Maps API, you need to create and configure a **Google Cloud Project**. Follow the steps below to get started:

### Step 1: Create a Google Cloud Account
If you don’t already have a Google Cloud account, you can create one by visiting the [Google Cloud Console](https://console.cloud.google.com/).<br>
> ⚠️ **Note:** If you are doing the workshop with NYP GDSC, there will be free credits — **Do NOT claim your free credits manually.**

### Step 2: Create a New Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. In the top-right corner, click on the **Select a Project** dropdown.
3. Click **New Project**.
4. Give your project a name (e.g., *Google Maps API Workshop*) and click **Create**.

### Step 3: Enable APIs
To use Google Maps services, you need to enable the APIs you'll be using. Here’s how:

1. In the Google Cloud Console, navigate to **APIs & Services > Library**.
2. Search for and enable the following APIs (search individually for each):
   - **Geocoding API**
   - **Places API**
   - **Distance Matrix API**

### Step 4: Claim Your Free Credits Using a Coupon
If you are doing the workshop with GDSC you will claim the **coupon code** for free credits, follow these steps to redeem it:

1. Go to the [Google Cloud Credits Redemption Page]([https://cloud.google.com/free](https://cloud.google.com/billing/docs/how-to/edu-grants#redeem) page.
2. Enter your First Name & Last Name.
3. **Enter the coupon code we give you during the workshop**.
   - Note: This coupon will only work if you use it on the Google Account you specified when you signed up for the event.
4. Your credits have now been successfully claimed. You may continue with the next step

   **Note**: You **do not need a billing account** if you're only using the free credits from the coupon.

### Step 5: Create API Key
Now you need to generate an API key to authenticate your application:

1. In the **APIs & Services** menu, go to **Credentials**.
2. Click **Create Credentials**, then select **API Key**.
3. A pop-up will display your new API Key. Copy this key to use in your Python application.

---

## Notes:
- You **do not need to set up billing** if you are using the free credits from the coupon.
- Make sure to monitor your credit usage in the **Billing > Reports** section of the Google Cloud Console to avoid unexpected charges.
- Your **free credits** should be enough for most testing and development needs!

---

If you have any questions or need further assistance, feel free to reach out during the workshop!

## **Getting Started**
- Examples of how to use your project or APIs. Include code samples for how users can interact with the APIs or features of your project.

```python
import googlemaps

# Initialize the client with the API key
gmaps = googlemaps.Client(key='your-api-key')
```
##  **Features**
A list of the key features or functionality the project provides, such as geocoding, distance matrix, places search, etc.

- Places API

```python
# ===================== Places API: Searching Nearby Locations =====================

# The `places_nearby` function finds nearby landmarks around the origin point.
# The location can be either:
#   - Latitude and longitude coordinates, or
#   - A human-readable address (which needs to be geocoded first).

# The `type` parameter specifies the type of places you are interested in (e.g., 'restaurant').

# Example: Search for nearby restaurants using coordinates (latitude, longitude)
location = (43.0617713, 141.3544507)  # Sapporo, Japan (latitude, longitude)
radius = 1000  # Search within a 1000-meter radius
place_type = 'restaurant'  # Searching for restaurants

# Fetch the nearby places
places_result = gmaps.places_nearby(location=location, radius=radius, type=place_type)

# Display the results
print("Nearby Restaurants:")
for place in places_result['results']:
    print(f"Name: {place['name']}")
    print(f"Address: {place['vicinity']}")
    print("-" * 40)
```
<br>
- Geocoding API

```python
address = "1600 Pennsylvania Ave NW, Washington, DC 20500"

# Geocode the address
geocode_result = gmaps.geocode(address)

# Output the result
print("Geocoding Result:")
if geocode_result:
    for result in geocode_result:
        print(f"Formatted Address: {result['formatted_address']}")
        print(f"Latitude: {result['geometry']['location']['lat']}")
        print(f"Longitude: {result['geometry']['location']['lng']}")
        print("-" * 40)
```
<br>
- Distance Matrix API

```python
origin = "1600 Pennsylvania Ave NW, Washington, DC 20500"  # Example origin address
destination = "The White House, Washington, DC"  # Example destination address
# Origin & destination can be either latitude and longitude coordinates or a human-readable address.

distance_result = gmaps.distance_matrix(origins=origin, destinations=destination, mode=driving)
# Mode can be set to walking, bicycling, transit or driving
distance_info = distance_result['rows'][0]['elements'][0]
print(f"Distance: {distance_info.get('distance', {}).get('text', 'N/A')}")
print(f"Duration: {distance_info.get('duration', {}).get('text', 'N/A')}")
```

##  **Starting our project**
We will be making use of what we just learnt earlier to make a simple fetch & search program.
* User Input: A location (e.g., a city name) is taken as input.
* Geocode the Location: Convert the location name into geographic coordinates (latitude and longitude).
* Search Nearby Restaurants: Use the coordinates to find nearby restaurants.
* Use Distance Matrix: Calculate the distance from the origin (input location) to the restaurants.

```python
import googlemaps

# Initialize Google Maps client
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Geocode a human-readable location to coordinates
def geocode_location(location_name):
    geocode_result = gmaps.geocode(location_name)
    return geocode_result[0]['geometry']['location']

# Find nearby restaurants around given coordinates
def find_nearby_restaurants(location, radius=1000):
    # You could add more parameters like 'keyword' or 'rank_by' to filter results
    # For example, use 'rank_by="distance"' to get the closest restaurants
    result = gmaps.places_nearby(location=location, radius=radius, type='restaurant')
    return result.get('results', [])

# Main program
def main():
    location_input = input("Enter a location (e.g. Nanyang Polytechnic): ")
    origin_location = geocode_location(location_input)

    print(f"\nCoordinates: {origin_location}")

    nearby_restaurants = find_nearby_restaurants(origin_location)

    if not nearby_restaurants:
        print("No nearby restaurants found.")
        return

    print("\nNearby Restaurants:")
    for restaurant in nearby_restaurants:
        # Vicinity refers to the address of the location. For example: NYP's address is 180 Ang Mo Kio Avenue 8, Singapore.
        print(f"- {restaurant['name']} ({restaurant['vicinity']})")
        
        # Calculate distance using your format
        mode = "driving"
        distance_result = gmaps.distance_matrix(
            origins=[origin_location],
            destinations=[restaurant.get("vicinity")],
            mode=mode
        )

        distance_info = distance_result['rows'][0]['elements'][0]
        print(f"  Distance: {distance_info.get('distance', {}).get('text', 'N/A')}")
        print(f"  Duration: {distance_info.get('duration', {}).get('text', 'N/A')}\n")

main()
```

## **Conclusion, Acknowledgements & Resources**
You have come to the end of the Google Maps API Workshop.
We hope this session has helped you gain a practical understanding of how to work with the Google Maps API — from geocoding locations, finding nearby places, calculating distances, to integrating these features into your own Python programs.
With these tools, you're now equipped to build location-aware applications, explore real-world data, and create more interactive user experiences.
Feel free to continue experimenting with different endpoints, explore the full range of services offered by the API, and don't hesitate to revisit the workshop materials whenever you need a refresher.
Thank you for participating, and we look forward to seeing what you build! 🚀
<br>
We extend our sincere gratitude to the developers and maintainers of the Python Client for Google Maps Services. Their efforts have been instrumental in enabling seamless integration of Google Maps functionalities into Python applications.
This open-source library, developed by the community and supported by Google, provides Python interfaces to various Google Maps APIs, including:
Directions API
Distance Matrix API
Elevation API
Geocoding API
Geolocation API
Time Zone API
Roads API
Places API
Maps Static API
Address Validation API
The library is licensed under the Apache 2.0 License and is available on GitHub: https://github.com/googlemaps/google-maps-services-python
We also acknowledge the broader community of contributors who have provided documentation, support, and enhancements to this project, making it a valuable resource for developers worldwide.
<br>
[Places API Documentation](https://developers.google.com/maps/documentation/places/web-service)
[Geocoding API Documentation](https://developers.google.com/maps/documentation/geocoding)
[Distance Matrix API Documentation](https://developers.google.com/maps/documentation/distance-matrix)
[Google Maps API Python Documentation](https://googlemaps.github.io/google-maps-services-python/docs/index.html)
