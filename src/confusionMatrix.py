

import seaborn as sns
import matplotlib.pyplot as plt

from params import *
from .Model import *






# Train the model
_, nb_img_tain, nb_img_test, testingPartition, trainedclassifier, _, trainConfusionMat = model.train(10)

# Test the model
testErrorMat = model.test(testingPartition, trainedclassifier)



def plot_trainConfusionMatrix(trainConfusionMat, nb_img_tain):
    
    trainCM = trainConfusionMat/nb_img_tain

    fig, ax = plt.subplots(1, figsize=(10,10))
    sns.heatmap(trainCM, annot=True)
    ax.set_xlabel('model predictions', fontsize=10)
    ax.set_ylabel('actual', fontsize=10)
    plt.title("Training data confusion matrix", fontsize=15)
    plt.show()





def plot_testErrorMatrix(testErrorMat, nb_img_test):
    
    testEM = testErrorMat/nb_img_test

    fig, ax = plt.subplots(1, figsize=(10,10))
    sns.heatmap(testEM, annot=True)
    ax.set_xlabel('model predictions', fontsize=10)
    ax.set_ylabel('actual', fontsize=10)
    plt.title("Test data error matrix", fontsize=15)
    plt.show()