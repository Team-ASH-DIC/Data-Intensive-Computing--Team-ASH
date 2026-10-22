import h5py
import numpy as np
import pandas as pd
from datetime import datetime, timedelta, timezone
from pathlib import Path


def clean_imerg_file(file_path):

    with h5py.File(file_path, "r") as file:

        grid = file["Grid"]

        latitude = grid["lat"][:]
        longitude = grid["lon"][:]
        time_value = grid["time"][:]
        precipitation = grid["precipitation"][0]

        fill_value = grid["precipitation"].attrs["_FillValue"]

        lat_mask = (latitude >= 24) & (latitude <= 50)
        lon_mask = (longitude >= -125) & (longitude <= -66)

        us_latitude = latitude[lat_mask]
        us_longitude = longitude[lon_mask]

        us_precipitation = precipitation[
            np.ix_(lon_mask, lat_mask)
        ]

        lon_grid, lat_grid = np.meshgrid(
            us_longitude,
            us_latitude,
            indexing="ij"
        )

        latitude_flat = lat_grid.flatten()
        longitude_flat = lon_grid.flatten()
        precipitation_flat = us_precipitation.flatten()

        df = pd.DataFrame({
            "latitude": latitude_flat,
            "longitude": longitude_flat,
            "precipitation_mm_per_hr": precipitation_flat
        })

        df = df[
            df["precipitation_mm_per_hr"] != fill_value
        ].copy()

        base_time = datetime(
            1980,
            1,
            6,
            tzinfo=timezone.utc
        )

        observation_time = base_time + timedelta(
            seconds=int(time_value[0])
        )

        df["datetime"] = observation_time
        df["date"] = observation_time.date()
        df["hour"] = observation_time.hour
        df["minute"] = observation_time.minute

        df = df[
            df["precipitation_mm_per_hr"] >= 0
        ].copy()

        return df


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    test_file = (
        project_root
        / "data"
        / "raw"
        / "3B-HHR.MS.MRG.3IMERG.20250914-S230000-E232959.1380.V07B.HDF5"
    )

    if test_file.exists():

        cleaned_data = clean_imerg_file(test_file)

        print("\nCleaned data shape:")
        print(cleaned_data.shape)

        print("\nFirst 10 rows:")
        print(cleaned_data.head(10))

        print("\nData types:")
        print(cleaned_data.dtypes)

        print("\nMissing values:")
        print(cleaned_data.isnull().sum())

        print("\nMinimum precipitation:")
        print(cleaned_data["precipitation_mm_per_hr"].min())

        print("\nMaximum precipitation:")
        print(cleaned_data["precipitation_mm_per_hr"].max())

    else:
        print("Test HDF5 file not found in data/raw/")
