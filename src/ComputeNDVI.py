
# import relevant libraries

import rasterio



# Open b4 and b8

#path = "path_to_folder_R10m"
path = 'C:/Users/engelbert/Downloads/Ishango/Notebook/S2A_MSIL2A_20201109T074131_N0214_R092_T36LYM_20201109T101027.SAFE/GRANULE/L2A_T36LYM_A028117_20201109T080034/IMG_DATA/R10m/'

band4 = rasterio.open(path+'T36LYM_20201109T074131_B04_10m.jp2')
band8 = rasterio.open(path+'T36LYM_20201109T074131_B08_10m.jp2')


# read Red(b4) and NIR(b8) as arrays
red = band4.read()
nir = band8.read()


# Calculate ndvi = (nir - red)/(nir + red)
ndvi = (nir.astype(float)-red.astype(float))/(nir+red)

# Write the NDVI image
meta = band4.meta
meta.update(driver='GTiff')
meta.update(dtype=rasterio.float32)

with rasterio.open('NDVI.tif', 'w', **meta) as dst:
    dst.write(ndvi.astype(rasterio.float32))
    