__author__ = 'bshillingford'

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


