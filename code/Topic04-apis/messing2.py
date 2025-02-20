# get planning applications
# Author: Andrew Beatty
import requests

url = "https://opendata.arcgis.com/datasets/8f69dffe26324ba3acc653cf6cb5cf8b_0.geojson"
list_of_planning = requests.get(url)
print(list_of_planning.json()["features"][0])