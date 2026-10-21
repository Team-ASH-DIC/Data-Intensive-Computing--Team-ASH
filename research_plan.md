Research Plan

Research Project Title
Large-Scale Analysis of Heavy Rainfall Patterns Across the United States Using NASA GPM IMERG

Created By
Akshitha Tolupunuri  
Saksham Saxena  
Harini Karnati

Version
1.0

Target Community of Interest
This project can be useful for weather researchers, people who study rainfall and flooding, emergency planning teams, and people who want to understand heavy rainfall patterns in the United States.

Date Created
September 17, 2026

Last Updated
September 17, 2026

GitHub Repository
https://github.com/sakshamsaxena111/Data-Intensive-Computing--Team-ASH.git

1. Research Goal

Heavy rainfall can cause many problems like flooding, road closures, damage to houses, and problems with travel. Rainfall is also not the same in every place. Some places may get very little rain, while other places may get very heavy rain in a short time.
The goal of this project is to study heavy rainfall patterns across the United States using NASA GPM IMERG data. We are using data from 1st August 2025 to 14th September 2025. The IMERG dataset gives rainfall values every 30 minutes for locations across the world.
For this project, we will focus only on the continental United States. We will study where heavy rainfall happens more often, where the rainfall is stronger, and how rainfall changes during the 45 day period.

Main Research Question:
How do the frequency, intensity, and geographic distribution of heavy rainfall vary across different regions of the United States from August 1 to September 14, 2025?

Supporting Questions:
1. Which parts of the United States get heavy rainfall more often?
2. Which areas have the highest rainfall values?
3. How does rainfall change during the 45-day period?
4. Are there places where heavy rainfall happens many times?
5. Can the recent rainfall values later be used to find places or times where extreme rainfall may happen?

2.Background and Motivation
Rainfall is very important because it affects water supply, farming, travel, and daily life. Heavy rainfall can also lead to flooding and can cause damage to roads, houses, and other places.
Rain gauges can measure rainfall, but they only measure rain at certain locations. Radar can cover a bigger area, but it also has limits. Satellite data can help because it can cover large areas and give rainfall information for many locations.
NASA GPM IMERG is useful for this project because it gives rainfall data across the world every 30 minutes. This gives a large amount of data for many locations and many time points.
We chose this project because we wanted to work with a real large dataset and study something that can have a real effect on people. Heavy rainfall is a good topic as it changes by location and time.
We believe this project is a good fit for EAS 587 because the dataset is too large to work with like a normal small CSV file. The data has to be downloaded in many files, processed in parts, filtered, cleaned, and later analyzed using tools that can work with large data.

3.Research Objectives and Scope
Objectives:
Objective 1: Download and understand the dataset - We will download NASA GPM IMERG Final Run V07 data for August 1 to September 14, 2025.
Expected result: We will have the HDF5 files needed for the project and understand the main fields in the data.
Objective 2: Focus on the United States - The original data is global, but our project only needs the continental United States.
Expected result: We will create a smaller dataset that contains only the area we need.
Objective 3: Clean the data - We will check the rainfall values, remove invalid values, and keep the important fields like time, latitude, longitude, and precipitation.
Expected result: We will have clean data that can be used for analysis.
Objective 4: Study rainfall intensity and frequency - We will study how strong the rainfall is and how often heavy rainfall happens.
Expected result: We will create tables, graphs, and maps that show heavy rainfall patterns.
Objective 5: Study rainfall over time - We will look at how rainfall changes during the 45-day period.
Expected result: We will show which days or time periods had more rainfall.
Objective 6: Use large-data tools - Later in the project, we plan to use PySpark and Spark to work with the larger processed dataset.
Expected result: We will build a process that can handle many files without loading everything into memory at the same time.

In Scope
This project will include:
1. NASA GPM IMERG Final Run V07 data
2. August 1, 2025 to September 14, 2025
3. Continental United States
4. Rainfall data every 30 minutes
5. Rainfall intensity
6. Rainfall frequency
7. Location-based rainfall patterns
8. Data cleaning
9. HDF5 file processing
10. Parquet files for processed data
11. Exploratory data analysis
12. Spark or PySpark later in the project

Out of Scope
This project will not include:
1. Rainfall analysis for the whole world
2. Long-term climate change analysis
3. Yearly rainfall analysis
4. Hurricane prediction
5. Weather forecasting
6. Direct flood prediction
7. Detailed climate modeling
8. Checking every rainfall value against a ground weather station
We are keeping the project focused because the main goal is to study heavy rainfall patterns using the large IMERG dataset.

4.Prior Research and References
We looked at previous work related to NASA IMERG and rainfall analysis.
Reference 1: NASA IMERG Version 7 Documentation
NASA provides information about how the IMERG data is created and what the different rainfall fields mean. This source is useful for our project because it helps us understand the dataset and how the rainfall values are produced.
Our project is different because we are not creating the IMERG data. We are using the data to study heavy rainfall patterns in the United States.
Reference 2: IMERG and TMPA Rainfall Study over the United States
One study compared IMERG and another satellite rainfall product over the continental United States.
The study looked at the accuracy of satellite rainfall and how the results changed in different locations.
This is useful because it shows that IMERG can be used for rainfall analysis across the United States.
Our project is different because we are focusing on a shorter 45-day period and using half-hourly data.
Reference 3: IMERG Rainfall Event Timing Study
Another study showed how well IMERG can capture rainfall events.
The researchers looked at rainfall duration, rainfall amount, intensity, and timing.
This is useful for our project because we also want to study rainfall intensity and how frequently there is heavy rainfall.
Our project is different because we are mainly doing large scale rainfall pattern analysis instead of comparing the data with radar.
Reference 4: IMERG at Different Time and Space Scales
One study checked how IMERG performs when the data is studied at different time periods and geographic sizes.
This is useful because our project will also work with rainfall at different time levels. We may use 30-minute data and later create hourly or daily values.
Reference 5: IMERG and Hydrology Study in the United States
Another study looked at NASA precipitation data and how rainfall measurement errors can affect flood and water-related studies.
This is useful because it shows why rainfall data quality is important.
Our project is different because we are not doing flood modeling. We are only studying the rainfall patterns.

References:
1.NASA Global Precipitation Measurement Mission. IMERG Version 07 Algorithm Theoretical Basis Document.
2. NASA Global Precipitation Measurement Mission. IMERG Version 07 Technical Documentation.
3. Pirmoradian, R., Hashemi, H., and Fayne, J. Performance evaluation of IMERG and TMPA daily precipitation products over CONUS.
4. Li, R. et al. Study on how well IMERG captures rainfall event timing.
5. Tan, J. et al. Performance of IMERG at different time and space scales.

5. Supporting Data and Resources

Primary Dataset
Dataset Name: NASA GPM IMERG Final Run V07
Product: GPM_3IMERGHH_07
Source: NASA GES DISC / NASA Earthdata
File Format: HDF5
Time Resolution: 30 minutes
Space Resolution: about 0.1 degree by 0.1 degree
Study Period: August 1, 2025 to September 14, 2025
Raw Data Area: Global
Project Area: Continental United States

Data Access
We found the data using NASA Earthdata Search.
We selected the dates from August 1, 2025 to September 14, 2025.
The full selected dataset contains:
 1. 2,160 HDF5 files
 2. 48 files per day
 3. 45 days of data
At the time of writing this report:
1. 2,067 HDF5 files were downloaded
2. the local data folder was about 16 GB
3. 93 files were still not downloaded

Data Structure
The data is not stored like a normal CSV file.
Each HDF5 file contains arrays for different fields.
Some important fields are:
1. latitude
2. longitude
3. time
4. precipitation
5. error or quality-related fields

The global grid has about:
1. 3,600 longitude values
2. 1,800 latitude values
That means one half-hour file can have about:
6,480,000 grid cells.
For the full 2,160 files, this can represent about:
13.99 billion location-time rainfall values.
For this project, one rainfall value at one location and one time will be treated as one observation.

Why This Dataset Is Large
The downloaded files already take about 16 GB of storage.
The full dataset cannot be loaded into one normal Pandas DataFrame because it would need much more memory.
Even if we only look at one rainfall value using 4 bytes, around 14 billion values would need about 56 GB of memory.
This does not include:
1. latitude
2. longitude
3. time
4. other fields
5. DataFrame overhead
Because of this, we cannot load the full dataset into memory at one time. We will have to process the data file by file or in small groups.
Available laptop RAM: 16 GB
Sampling and Subsetting Plan
We will not load all files at the same time. Our plan is:
1. Read one HDF5 file at a time.
2. Get the latitude, longitude, time, and precipitation data.
3. Keep only the continental United States.
4. Remove invalid rainfall values.
5. Save the processed data in a better format like Parquet.
6. Use a smaller sample while writing and testing our code.
7. Later use Spark or PySpark for the larger analysis.

We will also save a small CSV sample in the GitHub repository so the data can be viewed easily.
Software and Tools
We plan to use:
1. Python
2. h5py
3. NumPy
4. Pandas
5. Matplotlib
6. PySpark
7. Apache Spark
8. Parquet
9. Git
10. GitHub
11. Visual Studio Code
12. NASA Earthdata
We will not upload the full 16 GB raw dataset to GitHub because it is too large.

6. Risks, Constraints, Assumptions, and Open Questions
Risk 1: Large amount of data - There are thousands of HDF5 files. This may make processing slow.
Plan - We will process the files in smaller groups and keep only the U.S. data before doing the main analysis.
Risk 2: Download problems - While downloading the files, some downloads stopped because the internet connection was reset.
Plan - We will keep track of which files are downloaded and try to download missing files again if needed. We already have more than 2,000 files, so we have enough data to start the project.
Risk 3: Satellite data may not be perfect - IMERG rainfall values are estimates from satellite data. The values may not always be exactly the same as rainfall measured on the ground.
Plan - We will clearly say that this project is based on NASA IMERG rainfall estimates. We will not claim that every rainfall value is exact ground truth.

Risk 4: What counts as heavy rainfall? - We have not yet decided the final rainfall value that will be called heavy rainfall.
Plan - We will look at previous studies and also look at the rainfall values in our data before choosing a final limit. We may also use a percentile based value.
Risk 5: U.S. boundaries - The NASA grid does not follow state borders. A simple latitude and longitude box may also include some ocean areas or nearby places outside the U.S.
Plan - We will first use a simple continental U.S. area. Later, if needed, we can use state boundary data for better location filtering.
Assumptions
For this project, we are assuming that:
1. the downloaded files are valid NASA IMERG files
2. the latitude and longitude values are consistent
3. negative or fill values are not real rainfall values
4. the 45-day period has enough rainfall variation for analysis
5. the dataset is large enough for the EAS 587 project

Open Questions
1. What rainfall value should we use to define heavy rainfall?
2. Should we compare rainfall by state or by larger regions?
3. Should we create hourly and daily rainfall values?
4. Which quality fields from the HDF5 data should we use?
5. Should we add a machine learning part later in the project?

7.Research Approach, Tasks, and Timeline

Week 1:
1. understand the Phase 1 requirements
2. search for large datasets
3. choose NASA GPM IMERG
4.  decide the main project idea
5. download one sample HDF5 file
6. inspect the file
7. check the main fields
8. create a sample rainfall map
Result: dataset selected and checked.

Week 2:
1. select August 1 to September 14, 2025
2. select all 2,160 files
3. download the data
4. check file count and size
5. study the HDF5 structure
6. create the main research question
7. write the Phase 1 research plan
8. prepare the workshop slides
9. organize the GitHub repository
Result: Phase 1 report and presentation.

Week 3:
1. write Python code to read many HDF5 files
2. get latitude, longitude, time, and rainfall
3. keep only the continental United States
4. remove bad values
5. test the code on a small number of files
Result: basic data processing code.

Week 4:
1. process more files
2. save the processed data as Parquet
3. check missing values
4. calculate basic rainfall statistics
5. study the rainfall distribution
6. decide the final definition of heavy rainfall

Result: clean dataset and first analysis.

Weeks 5–6:
1. study rainfall frequency
2. study rainfall intensity
3. compare different parts of the United States
4. create maps
5. create graphs
6. study changes over time
7. prepare the Phase 2 presentation
Milestone: Phase 2 presentation on October 14–16.

Weeks 7–8:
1. use PySpark for larger processing
2. work with the processed data in Spark
3. compare processing methods
4. improve the data pipeline
Result: large scale processing pipeline.

Weeks 9–10:
1. continue the heavy rainfall analysis
2. find areas with repeated heavy rainfall
3. study important rainfall periods
4. decide if a machine learning part is useful
Result: main project results.

Week 11:
1. check the results again
2. check unusual values
3. compare results with previous research
4. write the limitations
5. prepare final graphs and maps
Result: final checked results.

Week 12:
1. clean the code
2. update the GitHub repository
3. update the README
4. prepare the final presentation
5. explain the methods, results, limits, and future work
Milestone: Final presentation during the week of December 7.

Design Decisions

Why We Chose NASA GPM IMERG
We chose NASA GPM IMERG because it is a large public dataset from NASA. The data gives us a chance to work with real problems like downloading many files, working with HDF5, managing storage, and processing large data.

Why We Chose the 45-Day Period
We chose August 1 to September 14, 2025. This gives us 45 days of data. Each day has 48 half-hour files. This gives a total of 2,160 files. This is enough data to make the project large, but it is still possible to work with during one semester.

Why We Chose the Continental United States
The original dataset is global. We only need U.S. rainfall for our research question. Keeping the whole world would make the project much larger without helping the main question. So we will keep only the continental United States.

Why We Are Keeping the Raw HDF5 Files
The original NASA files are in HDF5 format. We will keep these files as the raw data. This means we will always have the original source data if we need to check anything later.

Why We Plan to Use Parquet
We plan to save the cleaned data in Parquet format. Parquet is useful for large datasets and works well with Spark. It can also make later analysis easier than reading thousands of HDF5 files again.

Heavy Rainfall Definition
We have not chosen the final heavy rainfall limit yet. We want to first check the rainfall values in the dataset and read more about common rainfall limits. We will then choose one method and clearly explain why we used it.
