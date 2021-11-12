import sys
import os

# make the file in the parent directory available in the current file for import
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import geemap
import webbrowser

from params import *
from .Model import *





# Train the model
Input, nb_img_tain, nb_img_test, testingPartition, trainedclassifier, classified, trainConfusionMat = model.train(10)


def Display_classification(Input, classified, params):
    
    # add map
    map0 = geemap.Map()
    
    # Display the input and the classification.
    map0.centerObject(params.AOI, params.start_zoom)
    map0.addLayer(Input, {'bands': params.bands_select, 'max': 0.4}, 'landsat') 
    map0.addLayer(classified, {'palette': params.igbpPalette, 'min': params.min_leg, 'max': params.max_leg}, 'classification')


    # Add legend
    legend_keys = params.legend_keys

    legend_colors = params.legend_colors


    # Classify the input imagery.
    classified = classified.remap(params.x, params.y)

    map0.addLayer(classified, {'min': params.min_leg, 'max': params.max_leg, 'palette': legend_colors}, 'Labelled clusters')
    map0.add_legend(legend_keys=legend_keys, legend_colors=legend_colors, position='bottomright')
    
    
    # Temporary filepath
    outHtml = "resultMap.html" 

    map0.save(outHtml)

    webbrowser.open("./"+outHtml)