# Raw Data

The raw data for this project comes from the NASA GPM IMERG Final Run V07 dataset.

## Dataset Information

Dataset: NASA GPM IMERG Final Run V07  
Product: GPM_3IMERGHH_07  
Source: NASA GES DISC / NASA Earthdata  
File format: HDF5  
Time resolution: 30 minutes  
Spatial resolution: about 0.1 degree by 0.1 degree  
Study period: August 1, 2025 to September 14, 2025

The full selected period contains 2,160 expected HDF5 files.

We downloaded 2,067 HDF5 files. The local raw data folder is about 16 GB.

## Why the Raw Files Are Not Included

The complete raw dataset is too large to store in the GitHub repository.

The original files can be downloaded from NASA Earthdata Search using the GPM IMERG Final Run V07 half-hourly product.

The project processing pipeline reads the raw HDF5 files one at a time and creates cleaned Parquet files in the processed data folder.

## Raw Data Location

Place the downloaded HDF5 files in the raw data location used by `src/pipeline.py`.

The raw files should keep their original NASA filenames.
