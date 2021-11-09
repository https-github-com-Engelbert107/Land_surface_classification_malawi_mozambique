
# Tobacco area classification

The objective of this project is to use remote sensing to:

- identify tobacco fields;
- measure the area of tobacco field;
- analyze tobacco leaves and estimate crop yield.

## How to run code

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

