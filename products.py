

from params import api, start_date, end_date, platformname, processinglevel
from params import cloudcoverpercentage, footprint


# searching the products
products = api.query(footprint,
                     date = (start_date, end_date),
                     platformname = platformname,
                     processinglevel = processinglevel,
                     cloudcoverpercentage = cloudcoverpercentage
                    )

# convert the result to the pandas
products_gdf = api.to_geodataframe(products)
#products_gdf.head()