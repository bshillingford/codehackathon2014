__author__ = 'bshillingford, kszlim'

from math import radians, cos, sin, asin, sqrt
import requests
import xml.etree.ElementTree as ET
import csv


class WeatherException(Exception):
    pass


# Initialize site list data.
# Consists of (sitename (ID, string), friendly name (string), latlng (double tuple)) pairs.
sites = []
with open('localdata/site_list_towns_en.csv') as f:
    f.readline()
    f.readline()
    f.readline()
    for site, town, prov, lat, lng in csv.reader(f):
        if lat == " " or lng == " " or prov == "HEF":
            continue
        assert lat[-1] == "N"
        assert lng[-1] == "W"
        sites.append((site, town + ", " + prov, (float(lat[:-1]), -float(lng[:-1]))))


#res = requests.get('http://dd.weatheroffice.ec.gc.ca/citypage_weather/xml/siteList.xml')
#if not res.ok:
#    raise WeatherException("Failed to fetch siteList.xml; url={} response={}".format(res.url, str(res)))

def haversine(coordinates1, coordinates2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1 = coordinates1
    lon2, lat2 = coordinates2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

#Given tuple of coordinates (from user phone), return tuple hoding (siteID, province, longitude, latitude)
def closestNeighbour(userCoordinates):
    index = 0
    closestCity = (index, 20000)
    for site in sites:
        x = haversine(userCoordinates, site[2])
        if x < closestCity[1]:
            closestCity = (index, x)
            index += 1
    return sites[index]

print closestNeighbour((23,22))