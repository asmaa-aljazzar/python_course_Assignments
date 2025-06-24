
#?  Data Extraction:
#*  retrieving raw data from various internal and external data sourc3es and moving it into a staging area or processing system

#! Use the dataset to generate something new: photos, videos, etc...
#! Use the dataset to Analyse something state.

#region
#
#?  Data Sources:
#*  relational DB: MySQL, PostgreSQL\
#*  flat files: CSV, Excel[.xlsx, .xlsm, .xls, and .xlsb], JSON\
#*  APIs: REST APIs\
#*  IoT devices or sensors\
#*  Cloud storage: AWS S3, Google Drive\
#*  Logs and clickstreams: from websites or apps

#region

#! In Data Science: Garbage in Garbage out
#! Competetions: price from Companies for challenges to solve proplems in the datasets websites [hakathons]

#region

#? Popular websites for datasets
#* Kaggle [Not all codes are correct or perfect]
#   Huge collection of datasets for machine learning, competitions, and projects.
#
#* UCI Machine Learning Repository
#   Classic datasets for supervised and unsupervised learning.
#
#* DAta.gov
#   US goverment open data platform covering a wide range of topics, [accurate, actual data].
#
#* Google Dataset Search
#   A search enbgine to find datasets across the internet.
#
#* WHO Global Health Observatory
#   Health-related global datasets.

#region

#? Model: 
#   How much the AI was learn, and what did it learn.

#region

#? What is CSV: file.csv 
#*  Comma-Separated Values: a plain text file where each line represents a data record.
# The header of Colomn:   feature. [name, age, ...]
# An entire Row:      Observation. 

#region

#? Pandas Library
#* Class to create objs
# powerful lib for data manipulation and analysis.

#?  Common Pandas Tasks
#*  Read/Export data: CSV, Excel, JSON, SQL.
#*  Data Claning.
#*  Data Analysis.
#*  Filter/query data.
#*  Group and summarize data.

#region
#* Series:
#   One-dimensional labeled array (similar to a colmn in Excel or a dictionary)
#* DataFrame
#   Two-dimensional labeled data structure (like a table with rows and columns)
#
#* Series         DataFrame
#* [apple]     [apple][orange]
#* [88899] ==> [88899][888996]
#* [98876]     [98876][988766]
#region

#? import pandas
import panda as pd
# pip install panda if can't imported
#region