import pandas as pd
from loguru import logger


def read_parquet(fname:str, limit:int=20_000, count_variable='temperature')->pd.DataFrame:
    """
    Read parquet file and return a pandas dataframe
    """
    df = pd.read_parquet(fname)

    count = df[count_variable].where(lambda x: x != 0).count()
    if count > 20_000:
        logger.info(f'Reading in {fname}')
        df['datetime'] = process_datetime(df)
    else:
        logger.debug(f'Skipping file - too few data {fname}')
        df['datetime'] = ''
        df = df.iloc[[]]

    df = df.set_index(['Station_name', 'datetime'])
    df = convert_to_geopandas(df)

    return df
    

def process_datetime(df:pd.DataFrame)->pd.Series:
    
    date = df.Year.astype(str) + "-" + df.Month.astype(str) + "-" + df.Day.astype(str)
    time = df.Hour.astype(str) + ":" + df.Minute.astype(str)
    datetime = pd.to_datetime(date + " " + time)

    return datetime


def convert_to_geopandas(df):
    # convert df.Latitude and df.Longitude to a geopandas.geometry object
    import geopandas as gpd

    gdf = gpd.GeoDataFrame(
        data=df, 
        geometry=gpd.points_from_xy(df.Longitude, df.Latitude),
        crs='EPSG:4326',
    )

    return gdf