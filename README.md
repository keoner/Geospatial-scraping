# Simple Geospatial Scraper

A lightweight Python-based web scraper designed to collect geospatial data using the Google Maps API. Ideal for applications involving location analysis, reverse geocoding, and place metadata extraction.

## Features

- Randomly generates postal codes as starting points  
- Utilizes **Geocoding** and **Reverse Geocoding** to retrieve detailed location information  
- Stores retrieved data using Python's `json` library  
  - Includes attributes such as `place_name`, `place_id`, `coordinates`, and more  
- Scans for nearby landmarks such as grocery stores, schools, hospitals, etc.  
- Calculates distance and estimated travel time to each landmark from the origin  
- Identifies available bus services at the nearest bus stops  
- Extracts other landmarks accessible via the routes of those bus services
<br>

## Tech Stack
- Python
- Google Maps API
- googlemaps Python package
- JSON for storage/output
- Regular Expressions

## **Prerequisites**
1. **Google Maps Python Library**
   - Make sure you have the official **Google Maps Python client library** by running the following command in your terminal:

```
pip install -U googlemaps
```

2. **Python**
    - Python version **3.6** or higher. You can download it from the [Official Python website](https://www.python.org/downloads/).
    - Check your python version using the following command in terminal:
```
python3 --version
```

## Installation

1. **Clone the repository**  
   Open your terminal and run:

   ```
   git clone https://github.com/keoner/Geospatial-scraper.git
   ```

## **Getting Started**
Grab your Google API Key from [Google Cloud Console](https://console.cloud.google.com/apis/credentials).
- Fill it inside the key='YOUR_API_KEY' to get started
```python
import googlemaps

# Initialize the client with the API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')
```
After that run the program and it will automatically do its thing. Data generated will be stored in `generated_data.json`
- If the program doesn't output anything for a while it is normal because most of the randomly generated postal codes might not work. Also there is a sleep timer between each generation.
<br>

## Disclaimer

This project uses the Google Maps API and is subject to usage limits and pricing. Please ensure you understand [Google's API pricing](https://cloud.google.com/maps-platform/pricing) before extensive use.
