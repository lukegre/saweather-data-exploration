import xarray as xr


def drop_coords_without_dims(da: xr.DataArray)-> xr.DataArray:
    """Drop coordinates that are not dimensions of the DataArray"""

    coords_to_drop = tuple([c for c in da.coords.keys() if c not in list(da.dims)])
    return da.drop_vars(coords_to_drop)