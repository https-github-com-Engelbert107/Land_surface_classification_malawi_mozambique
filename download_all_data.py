
from src.function_download_all_data import Download_All_ProductID_Sentinel2_Data
from config import args




def main(args):

    Download_All_ProductID_Sentinel2_Data(args.geojson_file, args.start_date, args.end_date, args.cloudcoverpercentage, args.threshold_cloudcover)



if __name__ == "__main__":
    main(args)
