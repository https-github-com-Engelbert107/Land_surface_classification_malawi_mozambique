
from src.function_download_all_data import Download_All_ProductID_Sentinel2_Data
from config import args

import logging
logging.basicConfig(level=logging.DEBUG)




def main(args):

    Download_All_ProductID_Sentinel2_Data(args)



if __name__ == "__main__":
    main(args)
