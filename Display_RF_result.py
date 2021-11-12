

import geemap

from params import *
from src.Model import *
from src.mapClassification import Display_classification






# Train the model
Input, _, _, _, _, classified, _ = model.train(10)



def main(Input, classified, params):

    Display_classification(Input, classified, params)
    



if __name__ == "__main__":
    main(Input, classified, params)