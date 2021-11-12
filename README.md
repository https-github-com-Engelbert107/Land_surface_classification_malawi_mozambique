
# Land surface classification

The objective of this project is to use remote sensing to classify different regions on the bio-geographic land surface.

## How to run scripts for downloading

1. Download the data. Instruction on how to do this can be found in [Instruction](https://github.com/https-github-com-Engelbert107/Tobacco_areas_classification_malawi_mozambique/tree/main/Instruction).

2. Setup your new virtual environment.
    - `conda create -n name_env`
    - `conda activate name_env`

3. Install dependencies using the `requirements.txt` file provided

    You can install `geopandas` by following:
     ```bash 
     conda activate name_env
     ```
     ```bash 
     conda config --env --add channels conda-forge
     ```
     ```bash
     conda config --env --set channel_priority strict
     ```
    ```bash 
    conda install geopandas
    ```
     ```bash 
     conda install jupyter notebook
     ```
     ```bash 
     python -m ipykernel install --name name_env
     ```
    - Open Anaconda Navigator, select `nane_env`, click on `play` button and select `Open with jupyter notebook`

    You can also install `rasterio` and avoid the update by following:
     ```bash 
     conda install -c conda-forge rasterio --freeze-installed
     ```
     ```bash 
     conda install -c conda-forge rasterio --no-update-deps
     ```


4. Run code

   - Download a particular product ID for sentinel: 
    ```bash 
    python download_ID_sent_data.py
    ```

   - Download all the products ID for sentinel: 
    ```bash  
    python download_all_sent_data.py
    ```
    
    - Download a particular product ID for landsat: 
    ```bash 
    python download_ID_landsat_data.py
    ```

   - Download all the products ID for landsat: 
    ```bash  
    python download_all_landsat_data.py
    ```

   - For display the map for the Area of Interest (AoI): 
    ```bash 
    python map.py
    ```
    
  
  ## How to run scripts for model
  
  1. To authenticate to the Earth Engine servers, you need to allow your vscode to be able to edit on the terminal by following:    
      - Go to File > Preference > Settings then
      - type: ``run code`` and scroll down and select ``code-runner: Run in terminal``
      - restart your vscode.



  - Authenticate to the Earth Engine servers
      ```bash 
      python authenticate.py
      ```
      
  2. Run the train and test script
      
      - Train the model
       ```bash 
       python train_RF.py
       ```
      
      - Test the model
       ```bash 
       python test_RF.py
       ```
   
  3. Display the confusion matrix and map result for classification
   
      - Plot the confusion matrix for train data
       ```bash 
       python plot_trainCM.py
       ```
      
      - Plot the error matrix for test data
       ```bash 
       python plot_testEM.py
       ```
      
      - Display the classification model
       ```bash 
       python Display_RF_result.py
       ```

