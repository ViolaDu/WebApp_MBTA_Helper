import urllib.request   # urlencode function
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    # print(f)
    response_text = f.read().decode('utf-8')
    # print(response_text)
    response_data = json.loads(response_text)
    # print(response_data)
    return response_data


# url_testing = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
#
#
# print(get_json(url_testing))

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url_new = GMAPS_BASE_URL + '?address='+ place_name.replace(' ', '%20')
    # print(url_new)
    json = get_json(url_new)
    lat = json['results'][0]['geometry']['location']['lat']
    lng = json['results'][0]['geometry']['location']['lng']
    return lat, lng

# place_testing= 'Harvard University'
# print(get_lat_long(place_testing))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    url_MBTA = MBTA_BASE_URL + '?api_key={}&lat={}&lon={}&format=json'.format(MBTA_DEMO_API_KEY, latitude, longitude)
    json = get_json(url_MBTA)
    station_name = json['stop'][0]['stop_name']
    distance = json['stop'][0]['distance']
    return station_name,distance



def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """

    lat, lng = get_lat_long(place_name)
    return get_nearest_station(lat, lng)

# print(find_stop_near('MIT'))
