# Real-time_Streaming_Analysis_and_Implementation

## Overview:
In this project, I implemented three streaming algorithms using Python and Spark. The tasks involved generating a simulated data stream with the Yelp dataset and implementing Bloom Filtering, Flajolet-Martin algorithm, and Fixed Size Sampling (Reservoir Sampling). The project focuses on efficient processing of continuous data streams and estimation of various metrics.

## Problem Statement:
The goal of this project is to implement streaming algorithms to analyze data streams efficiently without storing the entire dataset in memory. Specifically, we aim to estimate false positive rates, unique user counts, and sample data streams within given constraints using appropriate algorithms.

## Technologies Used:

Python: Main programming language used for implementation.

Spark: Framework used for distributed stream processing.

JDK 1.8, Scala 2.12: Required for Spark setup and execution.

Spark 3.1.2: Version used for compatibility and testing.

## Datasets:
The project utilizes the users.txt file as the input dataset. Additionally, a Python blackbox file (blackbox.py) is provided to generate data from the input file. Both files are available in the public data directory.

## Tasks Implemented:

### Task 1: Bloom Filtering

Bloom Filtering: Employed to efficiently determine the presence of elements in a large dataset without the need for extensive memory usage, making it ideal for applications requiring fast set membership tests.

Implemented the Bloom Filtering algorithm to estimate whether user IDs in the data stream have appeared before. This involved designing proper hash functions and maintaining a global filter bit array. The algorithm efficiently handles false positive rates within specified constraints.

### Task 2: Flajolet-Martin Algorithm

Flajolet-Martin Algorithm: Utilized for estimating the cardinality of large data sets, especially in streaming scenarios, by leveraging probabilistic methods to provide approximate results with high accuracy.

Implemented the Flajolet-Martin algorithm to estimate the number of unique users within a window in the data stream. Proper hash functions and combining estimations from groups of hash functions were designed to achieve accurate estimations within given constraints.

### Task 3: Fixed Size Sampling (Reservoir Sampling)

Fixed Size Sampling (Reservoir Sampling): Implemented to select a representative subset of data from a continuous stream, ensuring memory efficiency and unbiased sampling for statistical analysis and inference.

Implemented the fixed-size sampling method (Reservoir Sampling Algorithm) to sample a subset of users from the streaming data. The algorithm ensures that memory usage remains constant and provides representative samples of the data stream.

## Conclusion:
This project showcases proficiency in implementing streaming algorithms for real-time data analysis. By leveraging Python and Spark, I successfully tackled challenges such as false positive rate estimation, unique user count estimation, and fixed-size sampling within specified constraints. The project demonstrates strong analytical and problem-solving skills, making it an attractive addition to my portfolio for potential employers.
