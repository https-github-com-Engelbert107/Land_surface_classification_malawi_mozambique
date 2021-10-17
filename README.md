
# Tobacco area classification

The objective of this project is to use remote sensing to:

- identify tobacco fields;
- measure the area of tobacco field;
- analyze tobacco leaves and estimate crop yield.

## How to run code

1. Download the data. Instruction on how to do this can be found in `Instruction`

2. Setup your new virtual environment.
    - `conda create -n name_env`
    - `conda activate -n name_env`

3. Install dependencies using the `requirements.txt` file provided

    You can install `geopandas` by following:
     ```bash 
     conda activate -n name_env
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
    - Open Anaconda Navigator, select `mane_env`, click on `play` button and select `Open with jupyter notebook`

    You can also install `rasterio` and avoid the update by following:
     ```bash 
     conda install -c conda-forge rasterio --freeze-installed
     ```
     ```bash 
     conda install -c conda-forge rasterio --no-update-deps
     ```


4. Run code

   - For download the particular product ID: 
    ```bash 
    python download_ID_data.py
    ```

   - For download all the products ID: 
    ```bash  
    python download_all_data.py
    ```

   - For display the map for the Area of Interest (AoI): 
    ```bash 
    python map.py
    ```

