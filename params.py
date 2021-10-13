
import geopandas as gpd
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt


# username and password of https://scihub.copernicus.eu/dhus
user = "username"     # your username
password = "password"     # your password


# latitude and longitude  of mozambique
latitude = -18.665695
longitude = 35.529562

path_geojson_file = "mapMozambique.geojson"
start_date = '20200901'
end_date = '20200930'
platformname = 'Sentinel-2'
processinglevel = 'Level-2A'
cloudcoverpercentage = (0,60)


api = SentinelAPI(user, password, "https://scihub.copernicus.eu/dhus")

# read a shapefile "MOZ_adm1.shp"
shapefile = gpd.read_file("MOZ_adm1.shp")

# path for your geojson file: here it is for mozambique
AOI = "mapMozambique.geojson"

footprint = geojson_to_wkt(read_geojson(AOI))

