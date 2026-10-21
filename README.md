# Data-Intensive-Computing--Team-ASH

## Overview
The EAS 587 Data Intensive Computing Group Project (Team ASH) investigates heavy rainfall patterns across the United States using NASA's Global Precipitation Measurement (GPM) IMERG satellite dataset. This repository holds our Phase 1 work: cleaning, exploring, and scaling analysis of a large precipitation dataset to turn raw satellite records into real climate insights.

## Repository Structure
    project-repo/
    ├── README.md              This file
    ├── requirements.txt       Python dependencies
    ├── research_plan.md       Phase 1 research plan
    ├── data/
    │   ├── samples/           Small representative data samples
    │   ├── raw/               Raw data or download instructions
    │   └── processed/         Cleaned/processed data
    └── src/
        ├── data_access.py     Scripts for accessing GPM IMERG data
        ├── data_sampling.py   Scripts for sampling the dataset
        └── eda.py             Exploratory data analysis

## Setup Instructions
1. Clone the repository git clone https://github.com/Team-ASH-DIC/Data-Intensive-Computing--Team-ASH.git
cd Data-Intensive-Computing--Team-ASH

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate 

3. Install the required Python packages:

pip install -r requirements.txt


## How to Run
1. **Access the data** — download or load the GPM IMERG data (see `data/raw/` for access/download instructions):

python src/data_access.py

2. **Sample the data** — generate a smaller representative subset for local development:

python src/data_sampling.py

3. **Explore the data** — run the exploratory data analysis:

python src/eda.py


Processed output is written to `data/processed/`.

## Team
Team ASH — EAS 587, Data Intensive Computing
