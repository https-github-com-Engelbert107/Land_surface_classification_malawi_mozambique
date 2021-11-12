
from params import *
from src.Model import *





def main():


    _, _, _, testingPartition, trainedclassifier, _, _ = model.train(10)


    # Test the model
    model.test(testingPartition, trainedclassifier)





if __name__ == "__main__":
    main()