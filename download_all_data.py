
from products import products_gdf
from function_download_all_data import Download_All_ProductID_Sentinel2_Data
from params import path_geojson_file, start_date, end_date, cloudcoverpercentage


products_gdf_uuid = products_gdf.uuid


def main():

    Download_All_ProductID_Sentinel2_Data(path_geojson_file, start_date, end_date, cloudcoverpercentage)



if __name__ == "__main__":
    main()
