# Processed Data

This folder is used for the cleaned and processed NASA GPM IMERG data.

The raw HDF5 files are processed using:

```bash
python src/pipeline.py
```

The pipeline reads the raw HDF5 files one at a time, keeps the continental United States subset, removes invalid precipitation values, creates time-related columns, and saves the cleaned data as Parquet files.

Each processed Parquet file contains:

- latitude
- longitude
- precipitation_mm_per_hr
- datetime
- date
- hour
- minute

The complete processed dataset is very large, so all processed Parquet files are not included in the GitHub repository.

To recreate the processed data, download the raw NASA GPM IMERG files into `data/raw/` and run `src/pipeline.py`.

The generated Parquet files will be saved in this folder.
