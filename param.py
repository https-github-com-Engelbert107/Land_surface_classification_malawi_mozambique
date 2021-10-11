
import geopandas as gpd
from sentinelsat import SentinelAPI


# username and password of https://scihub.copernicus.eu/dhus
user = "Marcinclair"     # your username
password = "Marcinclair"     # your password


# latitude and longitude  of mozambique
latitude = -18.665695
longitude = 35.529562

path_geojson_file = "mapMozambique.geojson"
start_date = '20200901'
end_date = '20200930'
cloudcoverpercentage = (0,60)


api = SentinelAPI(user, password, "https://scihub.copernicus.eu/dhus")

# read a shapefile
shapefile = gpd.read_file("ShapeMozambique/MOZ_adm1.shp")

