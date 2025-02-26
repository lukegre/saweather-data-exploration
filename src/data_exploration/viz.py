from matplotlib import pyplot as plt


# example of useage: gdf.explore(**shp.GOOGLE_TERRAIN)
_LEAFLET_DEFAULTS = dict()
GOOGLE_TERRAIN = dict(tiles='http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}', attr='Google', **_LEAFLET_DEFAULTS)
GOOGLE_SATELLITE = dict(tiles='http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}', attr='Google', **_LEAFLET_DEFAULTS)


def plot_station_timeseries(df, station_name, save_dir, variable='temperature', filter=lambda x: (x != 0) & (x > -10)):
    import pathlib

    save_dir = pathlib.Path(save_dir)
    assert save_dir.exists()
    station_fname = station_name.replace('/', '_').replace(' ', '_')
    sname = save_dir / f"{variable}/{variable}-{station_fname}.png"
    if sname.exists():
        return sname

    ser = df.loc[station_name, variable]
    mask = filter(ser)
    ser = ser.where(mask)

    _matplotlib_backend(ser, station_name, variable, sname)

    return sname


def _plotly_backend(ser, station_name, variable, sname):
    import pandas as pd
    pd.options.plotting.backend = "plotly"

    img = ser.plot()
    html = img.to_html(include_plotlyjs='cdn', full_html=False)
    with open(sname, 'w') as f:
        f.write(html)
    
    
def _matplotlib_backend(ser, station_name, variable, sname):
    import pandas as pd
    pd.options.plotting.backend = "matplotlib"

    fig, ax = plt.subplots(figsize=(9, 3))

    ax = ser.plot(ax=ax, lw=0.5)

    ax.set_title(station_name, loc='left')
    ax.set_ylabel(variable.replace('_', ' ').capitalize())
    ax.set_xlabel('')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    if sname is not None:
        sname.parent.mkdir(exist_ok=True, parents=True)
        fig.savefig(sname, bbox_inches='tight', dpi=100)

        plt.close(fig)
        return sname
    else:
        return ax