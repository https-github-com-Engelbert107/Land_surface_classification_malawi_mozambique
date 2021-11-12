
import argparse
import ee
import json

from json_file import json_string



# Initialize the API
ee.Initialize()


params = argparse.Namespace(    
    #  Change the coordinates to get a geometry point
    AOI = ee.Geometry.Point(json.loads(json_string)['features'][0]['geometry']['coordinates']),
    # name of the landsat collection
    collection_name = 'LANDSAT/LT05/C01/T1_TOA',

    # started date chosen
    start_date = '2011-01-01',
    # end date chosen
    end_date =  '2020-12-31',
    # Selected bands for landsat 5
    band_l5 =  [ 'B1','B2', 'B3', 'B4', 'B5', 'B6', 'B7'],

    # Land cover IGBP for training
    land_cover_data = ee.Image('MODIS/051/MCD12Q1/2013_01_01').select('Land_Cover_Type_1'),
    # Type of land cover selected
    Land_Cover_Type = 'Land_Cover_Type_1',

    # Max number of pixel
    numPixels = 5000,
    # Set the seed value
    seed = 0,
    # Set the split of our dataset
    split = 0.7,
    
    # Define a palette for the IGBP classification
    # ['water', 'forest', 'forest', 'forest', 'forest', 'forest', 'shrub, grass','shrub, grass', 'shrub, grass', 'shrub , grass', 'shrub , grass', 'wetlands', 'croplands', 'urban', 'crop mosaic', 'snow and ice', 'barren', 'tundra']
    igbpPalette = ['aec3d4', '152106', '225129', '369b47', '30eb5b', '387242', '6a2325', 'c3aa69', 'b76031', 'd9903d', '91af40', '111149', 'cdb33b', 'cc0013', '33280d', 'd7cdcc', 'f7e084', '6f6f6f'],

    # Define the legend 
    legend_keys = ['water', 'forest', 'forest', 'forest', 'forest', 'forest', 'shrub, grass','shrub, grass', 'shrub, grass', 'shrub , grass', 'shrub , grass', 'wetlands', 'croplands', 'urban', 'crop mosaic', 'snow and ice', 'barren', 'tundra'],
    # Define the color legend 
    legend_colors = ['aec3d4', '152106', '225129', '369b47', '30eb5b', '387242', '6a2325', 'c3aa69', 'b76031', 'd9903d', '91af40', '111149', 'cdb33b', 'cc0013', '33280d', 'd7cdcc', 'f7e084', '6f6f6f'],

    # remap legend
    x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
    y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],

    # range lengend
    min_leg = 0,
    max_leg = len([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) - 1,

    # zoom map
    start_zoom = 8,

    # selected display bands
    bands_select = ['B4', 'B3', 'B1']
)