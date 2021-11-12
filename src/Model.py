
import numpy as np
import pandas as pd
import ee
from params import *







class RandomForest:

    def __init__(self, params):
        self.collection_name = params.collection_name
        self.start_date = params.start_date
        self.end_date = params.end_date
        self.AOI = params.AOI
        self.band_l5 = params.band_l5
        self.land_cover_data = params.land_cover_data
        self.numPixels = params.numPixels
        self.seed = params.seed
        self.split = params.split
        self.Land_Cover_Type = params.Land_Cover_Type

  
    def train(self, numberTrees):
        # Chosen bands
        bands = self.band_l5

        # Image collection
        landsat = ee.Image(ee.ImageCollection(self.collection_name)\
                            .filterDate(self.start_date, self.end_date)\
                            .filterBounds(self.AOI)\
                            .sort('CLOUD_COVER')\
                            .first()\
                            .select(bands))

        # Compute cloud score.
        cloudScore = ee.Algorithms.Landsat.simpleCloudScore(landsat).select('cloud')

        # Mask the input for clouds.  Compute the min of the input mask to mask
        # pixels where any band is masked.  Combine that with the cloud mask.
        Input = landsat.updateMask(landsat.mask().reduce('min').And(cloudScore.lte(90)))

        # Use MODIS land cover, IGBP (International Geosphere-Biosphere Programme) classification, for training.
        modis = self.land_cover_data 

        # Sample the input imagery to get a FeatureCollection of training data.
        training = Input.addBands(modis).sample(numPixels=self.numPixels, seed=self.seed)
        print(f"The number of total images is : {training.size().getInfo()}")

        # The randomColumn() method will add a column of uniform random
        sample = training.randomColumn(seed=self.seed)

        # splitinto training and testing.
        split = self.split  
        trainingPartition = sample.filter(ee.Filter.lt('random', split))
        testingPartition = sample.filter(ee.Filter.gte('random', split))

        # Make a Random Forest classifier and train it.
        trainedclassifier = ee.Classifier.smileRandomForest(numberTrees).train(trainingPartition, self.Land_Cover_Type, inputProperties=bands)

        # Classify the input imagery.
        classified = Input.classify(trainedclassifier)

        # Get a confusion matrix representing resubstitution accuracy.
        trainAccuracy = trainedclassifier.confusionMatrix()

        # train confusion matrix into pandas
        trainConfusionMat = pd.DataFrame(np.asarray(trainAccuracy.getInfo()))

        # number of image for training
        nb_img_tain = trainingPartition.size().getInfo()

        # number of image for test
        nb_img_test = testingPartition.size().getInfo()

        # performance of the training model
        train_performance =  trainAccuracy.accuracy().getInfo()

        print(f"The number of images for training Partition is : {nb_img_tain}")
        print()
        print(f"Training accuracy is : {100 * train_performance:.2f} %")
        
        return Input, nb_img_tain, nb_img_test, testingPartition, trainedclassifier, classified, trainConfusionMat

    def test(self, testingPartition, trainedclassifier):
        
        # Classify the testing data.
        tested = testingPartition.classify(trainedclassifier)

        # Get a confusion matrix representing expected accuracy.
        testAccuracy = tested.errorMatrix(self.Land_Cover_Type, 'classification')

        # test error matrix into pandas
        testErrorMat = pd.DataFrame(np.asarray(testAccuracy.getInfo()))

        print(f"The number of images for test Partition is : {testingPartition.size().getInfo()}")
        print()
        print(f"Test accuracy is : {100 * testAccuracy.accuracy().getInfo():.2f} %")
    
        return testErrorMat


# Test class

# Instantiate the model
model = RandomForest(params)