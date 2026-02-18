# This function further breaks down the stored water by elevation bands
import rasterio 
import rasterio.mask 
from rasterio.warp import reproject, Resampling
import numpy as np
import pandas as pd

def stored_water_by_elev_band(swe_path, dem_path, bands):
    # --- Load SWE raster ---
    with rasterio.open(swe_path) as swe_src:
        swe = swe_src.read(1).astype(float)
        swe[swe == swe_src.nodata] = np.nan
        swe_transform = swe_src.transform
        swe_crs = swe_src.crs
        pixel_area = abs(swe_transform[0] * swe_transform[4])  # m² per pixel

    # --- Load DEM and reproject to SWE grid ---
    with rasterio.open(dem_path) as dem_src:
        dem = dem_src.read(1).astype(float)

        dem_reproj = np.empty_like(swe)
        reproject(
            dem,
            dem_reproj,
            src_transform=dem_src.transform,
            src_crs=dem_src.crs,
            dst_transform=swe_transform,
            dst_crs=swe_crs,
            resampling=Resampling.bilinear,
        )

    # --- Compute stored water for each elevation band ---
    results = {}
    for label, (z_min, z_max) in bands.items():
        if z_max is None:
            mask = (dem_reproj >= z_min)
        else:
            mask = (dem_reproj >= z_min) & (dem_reproj < z_max)

        swe_band = np.where(mask, swe, np.nan)

        volume_m3 = np.nansum(swe_band * pixel_area)  # mm → m³
        bl = volume_m3 / 1e9  # m³ → billion litres

        results[label] = bl

    return results