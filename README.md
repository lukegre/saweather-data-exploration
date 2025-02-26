# Dataset exploration

This repo contains the code for the dataset exploration for SA Weather for Benedict's thesis. 

## Getting started

I'm using `uv` to manage the python environment. It's like `pip` but much faster and better at managing dependencies. I can really recommend looking into this a bit more if you don't know it: https://astral.sh/uv/

```bash
# install uv for the shell 
curl -LsSf https://astral.sh/uv/install.sh | less

# OR you can use your current python environment
pip install uv
```

To install all the required packages and dependencies, run the following command in the project directory.
```bash
cd data-exploration  # the project directory
uv sync  # installs all required packages and dependencies
```

## Data
Automatic weather stations were downloaded by Benedict. This needs to be manually downloaded and placed in the `/data` folder. 
The notebook [`notebooks/station_data.ipynb`](notebooks/station_data.ipynb) contains the code to load and explore this station data.

The notebook [`notebooks/modis_land_surface_temp.ipynb`](notebooks/modis_land_surface_temp.ipynb) contains the code to load and explore the MODIS land surface temperature data which we'll use for the project.