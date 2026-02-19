# SWE Analysis
## Overview
This repository contains tools and workflows for analyzing Snow Water Equivalent (SWE) from WeGaw remote sensing products in the Capilano and Seymour watersheds.
It includes:
* Elevation‑band stored water calculations
* SWE maps from raw raster data
* Climatology and percent‑of‑normal analysis
* Reproducible Jupyter notebooks
* Modular Python functions in src/

The goal is to support consistent, transparent, and repeatable watershed snowpack reporting.

## Repo Structure
### Data Setup
Large raster data (SWE, DEMs, masks) is not included in this repository and is excluded via .gitignore.

Access data through the WeGaw data dashboard website at: https://dashboard.staging.defrost.io/dashboard. Username and password are shared separately. 

To run the analysis:
1. Create a data/ folder in the project root.
2. Add rasters to:
  * data/rasters/
  * data/raw/
  * data/processed/
3. Place CSV timeseries data in data/timeseries/ (these can be committed).
4. Ensure the DEM file is located at config/dem10m.tif.

