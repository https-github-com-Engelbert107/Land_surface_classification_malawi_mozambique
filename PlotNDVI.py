
import earthpy.plot as ep
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
from src.ComputeNDVI import ndvi


def plot():
    # Create classes and apply to NDVI results
    ndvi_class_bins = [-np.inf, 0, 0.1, 0.25, 0.4, np.inf]
    ndvi_sentinel_class = np.digitize(ndvi, ndvi_class_bins)

    # Apply the nodata mask to the newly classified NDVI data
    ndvi_sentinel_class = np.ma.masked_where(
        np.ma.getmask(ndvi), ndvi_sentinel_class)

    # Define color map
    nbr_colors = ["gray", "y", "yellowgreen", "g", "darkgreen"]
    nbr_cmap = ListedColormap(nbr_colors)

    # Define class names
    ndvi_cat_names = [
        "No Vegetation",
        "Bare Area",
        "Low Vegetation",
        "Moderate Vegetation",
        "High Vegetation",
        ]

    # Get list of classes
    classes = np.unique(ndvi_sentinel_class)
    classes = classes.tolist()
    # The mask returns a value of none in the classes. remove that
    classes = classes[0:5]

    # reshape from (1, 10980, 10980) ----> (10980, 10980)
    ndvi_sentinel_class = np.squeeze(ndvi_sentinel_class)

    # Plot your data
    fig, ax = plt.subplots(figsize=(15, 15))
    im = ax.imshow(ndvi_sentinel_class, cmap=nbr_cmap)

    ep.draw_legend(im_ax=im, classes=classes, titles=ndvi_cat_names)
    ax.set_title(
        "Sentinel 2 - Normalized Difference Vegetation Index (NDVI) Classes",
        fontsize=14,
        )
    ax.set_axis_off()

    # Auto adjust subplot to fit figure size
    plt.tight_layout()
    plt.show()