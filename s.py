from geopy.geocoders import Nominatim
from geopy import Point
from geopy import distance
import requests

# Get the latitude and longitude using geolocation
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
lat = geo_data['latitude']
lon = geo_data['longitude']

# Use geocoding to get the address for the current location
geolocator = Nominatim(user_agent="Maps")
location = geolocator.reverse(Point(lat, lon))

# Print the results
print(location.address)
print(location.latitude, location.longitude)