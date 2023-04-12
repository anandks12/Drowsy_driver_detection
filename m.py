import geocoder
import requests
from geopy.geocoders import GoogleV3
from geopy import Point

# Get the latitude and longitude using geolocation
location = geocoder.ip('me')
lat = location.lat
lon = location.lng

# Use geocoding to get the address for the current location
geolocator = GoogleV3(api_key='AIzaSyDasgAqpl5uNFemz0hn9Yyt6AOd7M1RvcU')
location = geolocator.reverse(Point(lat, lon))

# Print the results
print(location.address)
print(location.latitude, location.longitude)