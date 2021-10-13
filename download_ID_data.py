
from function_download_ID_data import Download_Random_ProductID_Sentinel2_Data
from params import path_geojson_file, start_date, end_date, platformname
from params import processinglevel, cloudcoverpercentage



def main():

    Download_Random_ProductID_Sentinel2_Data(path_geojson_file, start_date, end_date, platformname, processinglevel, cloudcoverpercentage)


if __name__ == "__main__":
    main()
