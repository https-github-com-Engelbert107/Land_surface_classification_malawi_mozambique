
from sentinelsat.sentinel import read_geojson, geojson_to_wkt

from params import api, path_geojson_file, start_date, end_date, cloudcoverpercentage

# This function take as input a path for the geoson file, started and ended date for the tobacco crop,
# print the number of ID products, check if the products ID is available online,
# print he number of products ID available online, download all the data for all available ID

def Download_All_ProductID_Sentinel2_Data(path_geojson_file, start_date, end_date, cloudcoverpercentage):
    
    cpt = 0
    lis_of_index_products_online = []
    
    # Search by polygon
    footprint = geojson_to_wkt(read_geojson(path_geojson_file))
    
    # Searching products
    products = api.query(footprint,
                     date = (start_date, end_date),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = cloudcoverpercentage
                    )
    
    # Convert the result into pandas
    products_gdf = api.to_geodataframe(products)
    
    # Print the number of the products ID
    print(f"The number of products are : {len(products_gdf['uuid'])}")
    
    # go over the number of products
    for i in range(len(products_gdf['uuid'])):
        
        # get each ID products which is a dictionnary
        product_id = api.get_product_odata(products_gdf['uuid'][i])
        
        # go over the keys and get the values
        for j in product_id.keys():
            if (j == 'Online' and product_id[j] == True):
                
                # put the index of product available online  in the list
                lis_of_index_products_online.append(i)
                    
                # print the index and ID of available product online
                print(f"For the index = {i} , the product with ID = {products_gdf['uuid'][i]} is online")
            
                # count the number of product available online
                cpt += 1
    
    # print the list of the index available products online
    print()
    print(f"The list of the available index product online is : {lis_of_index_products_online}")
    print('----'*10)
    print()
    print(f"The number of available products online are : {cpt}")
    
    for k in range(len(lis_of_index_products_online)):
    
        # check if the list is empty
        if len(lis_of_index_products_online) == 0:

            raise ValueError("You can't proceed to the download now because there is no product available online at the moment.")

        else:

            # Downloading all the available product from the list of index
            api.download(products_gdf['uuid'][k])