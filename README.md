
# Tobacco area classification

## How to run code

1. Download the data. Instruction on how to do this can be found in `Instruction`

2. Install all the required libraries

   2.1. Install `geopandas` by following:
    - `conda create -n name_env`
    - `conda activate -n name_env`
    - `conda config --env --add channels conda-forge`
    - `conda config --env --set channel_priority strict`
    - `conda install geopandas`
    - `conda install jupyter notebook`
    - `python -m ipykernel install --name name_env`
    - Open Anaconda Navigator, select `mane_env`, click on `play` button and select `Open with jupyter notebook`

   2.2. Install `rasterio` and avoid the update by following:
    - `conda install -c conda-forge rasterio --freeze-installed`
    - `conda install -c conda-forge rasterio --no-update-deps`


3. Run code

```bash
python map.py

python download_ID_data.py

python download_all_data.py
```