
import random
from sentinelsat import SentinelAPI
from sentinelsat.sentinel import read_geojson, geojson_to_wkt

from config import args


def Download_Random_ProductID_Sentinel2_Data(args):
    
    cpt = 0
    lis_of_index_products_online = []
    
    # api
    api = SentinelAPI(args.user, args.password, "https://scihub.copernicus.eu/dhus")
    
    # Search by polygon, time, and SciHub query keywords
    footprint = geojson_to_wkt(read_geojson(args.geojson_file))
    products = api.query(footprint,
                     date = (args.start_date, args.end_date),
                     platformname = args.platformname,
                     processinglevel = args.processinglevel,
                     cloudcoverpercentage = args.cloudcoverpercentage
                    )
    
    # Convert the result into pandas
    products_gdf = api.to_geodataframe(products)
    
    # Print the number of the products ID
    print(f"The number of products ID is : {len(products_gdf['uuid'])}")
    
    # Go over the number of products
    for i in range(len(products_gdf['uuid'])):
        
        # Check the threshold of cloudcoverpercentage for every ID
        if products_gdf['cloudcoverpercentage'][i]>= args.threshold_cloudcover:
            
            # Get each ID products which is a dictionnary
            product_id = api.get_product_odata(products_gdf['uuid'][i])
        
            # Go over the keys and get the values
            for j in product_id.keys():
                if (product_id[j] == True):

                    # Put the index of product available online  in the list
                    lis_of_index_products_online.append(i)

                    # Print the index and ID of available product online
                    print(f"For the index = {i} , the product with ID = {products_gdf['uuid'][i]} is online")

                    # Count the number of product available online
                    cpt += 1
    
    # Print the list of the index available products online
    print()
    print(f"The list of the available product ID index online is : {lis_of_index_products_online}")
    print('----'*10)
    print()
    print(f"The number of available products ID online is : {cpt}")
    
    # Check if the list is empty
    if len(lis_of_index_products_online) == 0:
        raise ValueError("You can't proceed to the download now because there is no product available online at the moment.")
    else:
        
        # Downloading for a particular ID randomly from the list of index
        choice_index_product_random = random.choice(lis_of_index_products_online)
        api.download(products_gdf['uuid'][choice_index_product_random])