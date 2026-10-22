import os
import time
import pandas as pd
from pathlib import Path

from data_cleaning import clean_imerg_file

print("NASA GPM IMERG - Phase 2 Processing Pipeline")
print("---------------------------------------------")

project_root = Path(__file__).resolve().parent.parent

raw_data_folder = project_root / "data" / "raw"

processed_data_folder = project_root / "data" / "processed"

os.makedirs(processed_data_folder, exist_ok=True)

all_files = []

for file_name in os.listdir(raw_data_folder):

    if file_name.endswith(".HDF5"):

        file_path = os.path.join(
            raw_data_folder,
            file_name
        )

        all_files.append(file_path)

all_files.sort()

print("\nTotal HDF5 files found:", len(all_files))

start_time = time.time()

processed_files = 0
skipped_files = 0
failed_files = 0
total_processed_rows = 0

for file_number, file_path in enumerate(all_files, start=1):

    file_name = os.path.basename(file_path)

    print(
        "\nProcessing file",
        file_number,
        "of",
        len(all_files)
    )

    print(file_name)

    parquet_name = file_name.replace(
        ".HDF5",
        ".parquet"
    )

    output_path = os.path.join(
        processed_data_folder,
        parquet_name
    )

    if os.path.exists(output_path):

        print("Already processed - skipping")

        skipped_files += 1

        continue

    try:

        cleaned_data = clean_imerg_file(file_path)

        if cleaned_data.empty:

            print("No valid U.S. data found")

            skipped_files += 1

            continue

        cleaned_data.to_parquet(
            output_path,
            index=False
        )

        processed_files += 1

        total_processed_rows += len(cleaned_data)

        print(
            "Rows saved:",
            len(cleaned_data)
        )

    except Exception as error:

        failed_files += 1

        print("Error processing file:")

        print(error)

end_time = time.time()

runtime_seconds = end_time - start_time

runtime_minutes = runtime_seconds / 60

print("\nPROCESSING SUMMARY")

print("Total HDF5 files:", len(all_files))

print("Files processed:", processed_files)

print("Files skipped:", skipped_files)

print("Files failed:", failed_files)

print("Total rows saved:", total_processed_rows)

print(
    "Runtime in minutes:",
    round(runtime_minutes, 2)
)

print("\nPipeline complete!")
