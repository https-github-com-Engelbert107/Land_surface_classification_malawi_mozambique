
import argparse



args = argparse.Namespace(
    
    # started date
    start_date = '20200901',
    # ended date
    end_date = '20210930',
    # name of the plateform
    platformname = 'Sentinel-2',
    # The level of the processing
    processinglevel = 'Level-2A',
    # set the interval of cloud cover
    cloudcoverpercentage = (0,100),
    # set the max cloud cover
    cloud_max = 90,
    # set the minimum threshold of cloud cover
    threshold_cloudcover = 10,
    # set the Landsat product (LANDSAT_TM_C1|LANDSAT_ETM_C1|LANDSAT_8_C1)
    product = 'LANDSAT_8_C1',
    # latitude of mozambique center
    # latitude = -18.665695,
    # latitude zambezia in Mozambique
    latitude = -16.653909048999935,
    # longitude  of mozambique center
    #longitude = 35.529562,
    # longitude zambezia in Mozambique
    longitude = 36.98368136900007,
    # your username
    user = "username",
    # your password
    password = "password",
    # geojson file
    geojson_file = "mapMozambique.geojson" ,
    # the output directory
    output_dir = 'path_directory'  

)