# Large-Scale Analysis of Heavy Rainfall Patterns Across the United States Using NASA GPM IMERG

## Team Members

- Akshitha Tolupunuri
- Saksham Saxena
- Harini Karnati

Course: EAS 587 - Data-Intensive Computing  
University at Buffalo  
Fall 2026

---

## Project Overview

Heavy rainfall can cause flooding, road problems, travel issues, and damage to homes and public places. Rainfall is also not the same in every location or at every time.

The goal of this project is to study heavy rainfall patterns across the continental United States using NASA GPM IMERG Final Run V07 data.

The study period is from August 1, 2025 to September 14, 2025.

NASA IMERG provides precipitation estimates every 30 minutes for locations across the world.

Our main research question is:

**How do the frequency, intensity, and geographic distribution of heavy rainfall vary across different regions of the United States from August 1 to September 14, 2025?**

---

## Dataset

Dataset: NASA GPM IMERG Final Run V07  
Product: GPM_3IMERGHH_07  
Source: NASA GES DISC / NASA Earthdata  
File Format: HDF5  
Time Resolution: 30 minutes  
Spatial Resolution: About 0.1 degree by 0.1 degree  
Raw Data Area: Global  
Project Area: Continental United States  

The full selected period normally contains:

- 45 days
- 48 half-hour files per day
- 2,160 expected HDF5 files

We downloaded:

- 2,067 HDF5 files
- about 16 GB of raw data

The complete raw dataset is not stored in GitHub because it is too large.

---

## Why This Is a Data-Intensive Project

Each global HDF5 file contains about:

- 3,600 longitude values
- 1,800 latitude values
- about 6.48 million grid cells

The full dataset cannot be loaded into one normal Pandas DataFrame because it would require much more memory than the available 16 GB RAM.

Because of this, we process the files one at a time instead of loading everything into memory together.

This makes the processing more scalable and reduces memory usage.

---

## Project Workflow

The main workflow of the project is:

```text
NASA Earthdata
        ↓
Download HDF5 Files
        ↓
Inspect and Profile Raw Data
        ↓
Clean and Filter the Data
        ↓
Keep the U.S. Study Area
        ↓
Save Processed Data as Parquet
        ↓
Create Analytics Summaries
        ↓
Perform EDA
        ↓
Study Rainfall Frequency and Intensity
        ↓
Study Geographic Heavy Rainfall Patterns
        ↓
Create Figures and Results
```

---

## Repository Structure

```text
project-repo/
│
├── README.md
├── requirements.txt
├── research_plan.md
├── phase2_report.md
│
├── data/
│   ├── samples/
│   ├── raw/
│   ├── processed/
│   ├── analytics/
│   └── boundaries/
│
├── src/
│   ├── data_access.py
│   ├── data_sampling.py
│   ├── data_cleaning.py
│   ├── pipeline.py
│   └── analytics.py
│
├── notebooks/
│   └── phase2_analysis.ipynb
│
└── figures/
```

---

## Main Source Files

### `src/data_access.py`

This file was created in Phase 1 to help access and inspect the dataset.

### `src/data_sampling.py`

This file creates a smaller representative sample from the processed data.

The sample is stored in:

```text
data/samples/imerg_sample.parquet
```

A fixed random seed of 42 is used for reproducibility.

### `src/data_cleaning.py`

This file contains the main cleaning steps.

The code:

- reads one NASA IMERG HDF5 file
- reads latitude, longitude, time, and precipitation
- keeps the required geographic area
- removes invalid fill values
- removes negative precipitation values
- keeps valid zero rainfall values
- creates useful date and time columns
- converts the result into a Pandas DataFrame

### `src/pipeline.py`

This file is the main raw-to-processed pipeline.

It:

1. finds the raw HDF5 files
2. processes one file at a time
3. applies the cleaning steps from `data_cleaning.py`
4. saves the cleaned data as Parquet files
5. continues until all available files are processed

Processing files one at a time prevents the full dataset from using all available memory.

### `src/analytics.py`

This file creates smaller summary datasets from the processed Parquet files.

It creates:

- `half_hour_summary.parquet`
- `daily_summary.parquet`
- `hourly_summary.parquet`
- `spatial_summary.parquet`
- `eda_sample.parquet`

These files are used for EDA and first analytics.

### `notebooks/phase2_analysis.ipynb`

This notebook contains the Phase 2 EDA and first analytics.

It includes:

- processed data checks
- rainfall distribution
- heavy rainfall definition
- daily rainfall analysis
- hourly rainfall analysis
- rainfall frequency
- rainfall intensity
- heavy rainfall frequency
- correlation analysis
- spatial rainfall analysis
- maps for the lower 48 states
- key findings
- design decisions
- dead ends

---

## Installation

Python is required for this project.

Install the required packages using:

```bash
pip install -r requirements.txt
```

The main packages used are:

```text
pandas
numpy
matplotlib
h5py
pyarrow
pyshp
jupyter
```

---

# Reproducibility and Running the Project

The project uses relative project paths so the code does not depend on a personal Windows username, OneDrive folder, or other computer-specific path.

The expected main project structure is:

```text
project-repo/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── analytics/
│   └── boundaries/
├── src/
└── notebooks/
```

---

## Raw Data Requirement

The complete NASA GPM IMERG raw dataset is not included in this repository because it is about 16 GB.

To run the full raw-data processing workflow, the required HDF5 files must first be downloaded from NASA Earthdata and placed inside:

```text
data/raw/
```

The original NASA filenames should be kept.

For example, the test file used by `data_cleaning.py` is expected at:

```text
data/raw/3B-HHR.MS.MRG.3IMERG.20250914-S230000-E232959.1380.V07B.HDF5
```

Once the raw files are placed in `data/raw/`, the scripts can run without changing the code to use a personal computer path.

---

## Step 1: Test the Cleaning Script

The cleaning script can be tested using one HDF5 file.

From the main project folder, run:

```bash
python src/data_cleaning.py
```

The test HDF5 file must exist inside:

```text
data/raw/
```

The cleaning script reads the HDF5 file and checks:

- cleaned data shape
- sample rows
- data types
- missing values
- minimum precipitation
- maximum precipitation

The cleaning function itself is also used by `pipeline.py` for the full dataset.

---

## Step 2: Process the Raw Data

Make sure the NASA HDF5 files are inside:

```text
data/raw/
```

Then run:

```bash
python src/pipeline.py
```

The pipeline:

- reads the raw HDF5 files from `data/raw/`
- processes one file at a time
- applies the cleaning function
- saves each cleaned file as Parquet

The generated files are saved in:

```text
data/processed/
```

The `data/processed/` folder is created automatically if needed.

The complete processed dataset is also large, so all processed Parquet files do not need to be stored in GitHub.

---

## Step 3: Create the Sample Data

To create the small sample file, run:

```bash
python src/data_sampling.py
```

This uses the processed Parquet data and creates:

```text
data/samples/imerg_sample.parquet
```

The sample uses a fixed random seed of 42.

This file can be included in GitHub because it is much smaller than the full processed dataset.

---

## Step 4: Run the Analytics Script

Before running `analytics.py`, the processed Parquet files must already exist in:

```text
data/processed/
```

The final reproducible version of `analytics.py` should use the project root to find:

```text
data/processed/
```

and save results into:

```text
data/analytics/
```

The recommended reproducible path setup is:

```python
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

processed_folder = project_root / "data" / "processed"
results_folder = project_root / "data" / "analytics"
```

Then the analytics script can be run from the main project folder using:

```bash
python src/analytics.py
```

The script creates:

```text
data/analytics/half_hour_summary.parquet
data/analytics/daily_summary.parquet
data/analytics/hourly_summary.parquet
data/analytics/spatial_summary.parquet
data/analytics/eda_sample.parquet
```

These smaller files are used by the Phase 2 analysis notebook.

### If an older analytics version is used

An older version of `analytics.py` may contain:

```python
processed_folder = "../data/processed"
results_folder = "../data/analytics"
```

This version depends on the current working directory.

If that version is used, run it from inside the `src` folder:

```bash
cd src
python analytics.py
```

The final repository should preferably use the reproducible `Path(__file__)` version instead.

---

## Step 5: Run the Phase 2 EDA Notebook

Open:

```text
notebooks/phase2_analysis.ipynb
```

The notebook uses the summary files in:

```text
data/analytics/
```

The following files are required:

```text
half_hour_summary.parquet
daily_summary.parquet
hourly_summary.parquet
spatial_summary.parquet
eda_sample.parquet
```

The notebook uses a reproducible project-path setup:

```python
from pathlib import Path

current_dir = Path.cwd()

if current_dir.name == "notebooks":
    project_root = current_dir.parent
else:
    project_root = current_dir
```

This allows the notebook to work whether it is started from the main project folder or from the `notebooks` folder.

---

## Spatial Boundary Files Required for EDA

The final spatial analysis uses U.S. Census state boundary data.

The shapefile folder should be available at:

```text
data/boundaries/tl_2025_us_state/
```

The folder should include the shapefile components, including files such as:

```text
tl_2025_us_state.shp
tl_2025_us_state.shx
tl_2025_us_state.dbf
```

The notebook uses:

```text
data/boundaries/tl_2025_us_state/tl_2025_us_state.shp
```

for the lower-48 spatial filtering.

The spatial analysis uses `pyshp` and Matplotlib paths.

To avoid a naming conflict with `pathlib.Path`, the notebook uses:

```python
from matplotlib.path import Path as MplPath
```

and polygon paths are created using:

```python
MplPath(polygon_points)
```

This keeps:

```python
Path
```

for file and folder paths, and:

```python
MplPath
```

for geographic polygon paths.

---

## Recommended Full Run Order

After the raw files and required boundary files are available, the project can be run in this order:

```bash
pip install -r requirements.txt
python src/data_cleaning.py
python src/pipeline.py
python src/data_sampling.py
python src/analytics.py
```

Then open:

```text
notebooks/phase2_analysis.ipynb
```

and run the notebook from top to bottom.

The `data_cleaning.py` command is mainly a test of one raw file. The full cleaning of all files happens when `pipeline.py` calls the cleaning function.

---

## Reproducing Without Downloading the Full Raw Dataset

The full raw dataset is about 16 GB, so every team member does not need to keep a complete copy.

A practical team workflow is:

```text
Raw HDF5 Data
      ↓
Akshitha
data_cleaning.py + pipeline.py
      ↓
Processed Parquet Files
      ↓
analytics.py
      ↓
Analytics Summary Files
      ↓
EDA Notebook
```

Team members working only on EDA can use the smaller files in:

```text
data/analytics/
```

instead of downloading the complete 16 GB raw dataset.

However, reproducing the entire workflow from the original NASA files requires the raw HDF5 files to be downloaded and placed in:

```text
data/raw/
```

---

## Data Cleaning

The main cleaning steps are:

- extract latitude, longitude, time, and precipitation
- keep the required U.S. geographic area
- remove invalid fill values
- remove negative precipitation values
- keep valid zero rainfall values
- create date, hour, and minute fields
- save the cleaned data as Parquet files

Zero rainfall is kept because it is a valid observation showing that no rain occurred at that location and time.

---

## Heavy Rainfall Definition

In Phase 1, the final heavy rainfall value had not yet been selected.

During Phase 2, we studied the distribution of positive rainfall values.

We defined heavy rainfall as:

**Precipitation greater than or equal to 5.3 mm/hr**

The value 5.3 mm/hr is the 95th percentile of positive rainfall observations in our processed EDA sample.

This threshold is used for this study period. It is not a general definition for all rainfall studies.

---

## Data Coverage

The selected study period is August 1 to September 14, 2025.

However, the downloaded data is incomplete at the beginning of the period.

- August 1 has no downloaded data.
- August 2 contains only 3 of the expected 48 half-hour files.
- August 3 to September 14 contains 43 complete days.

For this reason, daily comparisons use the 43 complete days.

---

## Exploratory Data Analysis

The Phase 2 EDA studies rainfall using different views.

### Rainfall Distribution

About 9.9% of observations in the EDA sample had precipitation greater than 0 mm/hr.

The positive rainfall distribution is strongly right-skewed.

Most rainfall values are small, while a smaller number of observations have much higher rainfall intensity.

We kept the high rainfall values because strong rainfall events are important for our research question.

### Daily Rainfall

We studied:

- daily rainfall frequency
- average rainfall intensity
- maximum rainfall intensity
- heavy rainfall frequency

September 5 had the highest overall rainfall frequency among the complete days.

August 20 and August 21 had high rainfall intensity and high heavy rainfall activity.

### Hourly Rainfall

The time values are studied in UTC.

Rainfall frequency was highest mainly around 21:00 to 23:00 UTC.

Average rainfall intensity was highest mainly around 14:00 to 18:00 UTC.

This shows that the time when rainfall happened most often was not always the same time when rainfall was strongest.

### Spatial Rainfall

The original geographic subset was rectangular and included some ocean areas and locations outside the lower 48 states.

We used U.S. Census state boundary data to keep only spatial bins whose center points were inside the lower 48 states.

The spatial data was reduced from:

- 1,534 original spatial bins
- to 851 lower-48 spatial bins

These 851 bins were used for the final spatial analysis.

---

## Main Phase 2 Findings

Some of the main findings are:

- About 9.9% of sampled observations had positive rainfall.
- Heavy rainfall was defined as 5.3 mm/hr or higher.
- September 5 had the highest overall rainfall frequency among the complete days.
- August 20 and August 21 had high rainfall intensity and heavy rainfall activity.
- Rainfall frequency and heavy rainfall frequency had a moderate positive correlation of about 0.54.
- Rainfall frequency was highest mainly around 21:00 to 23:00 UTC.
- Average rainfall intensity was highest mainly around 14:00 to 18:00 UTC.
- Rainfall frequency was high mainly around Florida and parts of the southeastern United States.
- Heavy rainfall frequency was also high mainly around Florida and nearby southeastern areas.
- The highest spatial heavy rainfall frequency was about 1.87%.
- The strongest individual rainfall events were found across different parts of the United States.

These results only describe the selected study period. They should not be treated as long-term climate results.

---

## Design Decisions

### File-by-File Processing

We process one file at a time because the complete dataset is too large to load into memory at once.

### Parquet Format

We save processed data in Parquet format because it is useful for large datasets and easier to use for later analysis than reading thousands of HDF5 files again.

### Heavy Rainfall Threshold

We use the 95th percentile of positive rainfall values to define heavy rainfall instead of selecting a random value.

### High Rainfall Values

We do not automatically remove high rainfall values as outliers because strong rainfall is important for our research question.

### Incomplete Days

August 1 and August 2 are not used in daily comparisons because the data is incomplete.

### U.S. Boundary Filtering

We use U.S. Census state boundaries for the final spatial analysis because a simple latitude and longitude box included ocean areas.

---

## Dead Ends

### Simple Latitude and Longitude Filtering

At first, we used simple latitude and longitude limits for the final spatial analysis.

This method still included some ocean areas. Some of the highest rainfall frequency locations appeared in the Atlantic Ocean.

Because of this, we did not use this method for the final spatial results.

### GeoPandas and Shapely

We also tried GeoPandas and Shapely for U.S. state boundary filtering.

Some required library files were blocked in the Windows environment.

We later used `pyshp` with Matplotlib paths to perform the boundary filtering.

---

## Limitations

There are some important limitations to the current analysis.

- The study covers only a short 45-day period.
- The beginning of the study period has missing files.
- NASA IMERG precipitation values are satellite-based estimates and are not exact ground measurements.
- The results should not be used as long-term climate conclusions.
- We are studying rainfall patterns and are not directly predicting floods or weather.

---

## Phase 3

Phase 2 prepares the cleaned data and first analytics needed for the next phase.

In Phase 3, we plan to continue using large-data tools such as Apache Spark and PySpark.

We can also study repeated heavy rainfall patterns, improve the scalable processing workflow, and decide whether a machine learning method is useful for the project.

---

## References

1. NASA Global Precipitation Measurement Mission, IMERG Version 07 Algorithm Theoretical Basis Document.
2. NASA Global Precipitation Measurement Mission, IMERG Version 07 Technical Documentation.
3. NASA GES DISC / NASA Earthdata.
4. U.S. Census state boundary data.
