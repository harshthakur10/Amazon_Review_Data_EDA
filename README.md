# Amazon Review Data Analysis and Performed EDA

## Overview
*This project focuses on Exploratory Data Analysis (EDA) of a dataset sourced from Amazon. The main objectives include importing necessary libraries, performing data cleaning, understanding the dataset, exploring it through various statistical measures, and visualizing key insights.*

## Dataset
The dataset used in this project is sourced from Amazon.
- 'Data/' https://docs.google.com/spreadsheets/d/1F2V4oXFoWm0fFlupZ9kJDcQRzRGIZY2LkwAyoCAHW_c/edit?usp=sharing

This dataset is having the data of 1K+ Amazon Product's Ratings and Reviews as per their details listed on the official website of Amazon¶

**Column Descriptors**
* `product_id` - Product ID
* `product_name` - Name of the Product
* `category` - Category of the Product
* `discounted_price` - Discounted Price of the Product
* `actual_price` - Actual Price of the Product
* `discount_percentage` - Percentage of Discount for the Product
* `rating` - Rating of the Product
* `rating_count` - Number of people who voted for the Amazon rating
* `about_product` - Description about the Product
* `user_id` - ID of the user who wrote review for the Product
* `user_name` - Name of the user who wrote review for the Product
* `review_id` - ID of the user review
* `review_title` - Short review
* `review_content` - Long review
* `img_link` - Image Link of the Product
* `product_link` - Official Website Link of the Product


## Contents
1. [Introduction](#introduction)
2. [Importing Python Modules](#importing-python-modules)
3. [Dataset Overview](#dataset-overview)
4. [Data Cleaning](#data-cleaning)
5. [Data Understanding](#data-understanding)
6. [Data Exploration and Visualization](#data-exploration-and-visualization)
7. [Conclusion](#conclusion)

## Introduction

- Welcome to our Amazon Product Dataset Exploratory Data Analysis (EDA) project.
- In this project, we delve into a comprehensive analysis of Amazon product data, aiming to uncover valuable insights and trends.
- Through rigorous data cleaning, exploration, and visualization techniques, we aim to provide a deeper understanding of the dataset and its underlying characteristics.
- Join us on this journey as we explore the fascinating world of Amazon products through data.


## Dataset Overview

* Shape of the data is 1462 Columns & 24 Rows.
* The dataset encompasses attributes associated with Amazon products and user reviews.
* Columns include product ID, name, category, and pricing details (discounted and actual).
* Additional columns feature the discount percentage, average rating, and rating count.
* User-related attributes consist of user ID and name.
* Review details include review ID, title, and content.
* Links to product images and pages complement the dataset.
* These attributes collectively offer profound insights into product characteristics, user feedback, and pricing dynamics, facilitating comprehensive analysis and interpretation.

## Importing Python Modules:
We will use the following libraries¶
1. Pandas: Data manipulation and analysis
2. Numpy: Numerical operations and calculations
3. Matplotlib: Data visualization and plotting
4. Seaborn: Enhanced data visualization and statistical graphics¶

## Data Cleaning  

The dataset underwent a series of cleaning steps to ensure its quality and usability for analysis. Here's a summary of the data cleaning process:

1. **Handling Missing Values:**
   The `isnull().sum()` method was used to identify missing values in the dataset. After identifying the columns with missing values, those rows were either dropped or imputed with appropriate values to maintain data integrity.

2. **Data Type Conversion:**
   Certain numeric columns such as 'discounted_price', 'actual_price', 'discount_percentage', 'rating', and 'rating_count' contained special characters like currency symbols and percentage signs. These were removed using string manipulation techniques (`str.replace()`) and the columns were then converted to numeric data type using `astype(float)`.

3. **Handling Special Characters:**
   Special characters such as currency symbols ('₹') and percentage signs were removed from numeric columns to facilitate numerical computations.

4. **Removing Unnecessary Characters:**
   Characters such as commas (',') and vertical bars ('|') were removed from numeric columns to ensure consistency and enable proper data conversion.

5. **Removing Rows with Missing Values:**
   After cleaning, rows with any remaining missing values were dropped from the dataset using the `dropna()` method to ensure the completeness of the data for analysis.

*Following these steps, the dataset was cleaned and prepared for further analysis.*

*The cleaned dataset was confirmed to have no missing values, ensuring the reliability of the subsequent analysis.*


## Data Understanding

Before diving into exploratory analysis, it's essential to understand the structure and characteristics of the dataset. 

The following steps were taken:

1. **Descriptive Statistics:**
   Summary statistics such as count, mean, standard deviation, min, max, and quartiles were computed for numeric columns using the `describe()` method. This provided an overview of the distribution and central tendencies of the numerical features.

2. **Descriptive Statistics for Categorical Columns:**
   Summary statistics for categorical columns, including count, unique, top, and frequency, were obtained using the `describe(include=object)` method. This helped understand the frequency and distribution of categorical values.

3. **Dataset Information:**
   The `info()` method was used to obtain:
   * Concise summary of the dataset, including the data types of each column. 
   * The presence of missing values. 
   * Identification of any potential data type inconsistencies or missing values.

*By understanding the dataset's structure and characteristics, we gained insights into its key features and prepared for the subsequent exploratory data analysis (EDA) phase.*


## Data Exploration and Visualization

**Techniques Used:**
The code employs various techniques such as summary statistics, scatter plots, bar plots, and box plots to explore and visualize the dataset. These techniques help in understanding the distribution, relationships, and patterns within the data.

**Key Insights:**
Through the data exploration process facilitated by the code-
* Significant insights and trends are uncovered.
* Insights include identifying the distribution of product prices.
* Analyzing the relationship between discount percentage and product rating.
* Exploring variations in product attributes across different categories.

**Visualization Methods:**
* The code utilizes various visualization methods such as box plots, scatter plots, bar plots, and histograms to represent and analyze the dataset effectively.
* Visualizations aid in interpreting complex data structures, identifying outliers, and understanding relationships between variables.



***Distribution of Product Prices, to identify notable Outliners***
![Screenshot 2024-05-13 212521](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/621c37b7-fb95-4174-b46e-28cf1a82a57f)


***Correlation between Discount percentage and Product Rating***
![Screenshot 2024-05-13 213312](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/4d81809d-6559-4753-9ab5-11e83c5c2c61)


***Product Tends based on Product Price & Rating***
![Screenshot 2024-05-13 214623](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/2c739044-9c71-4811-a8b7-8bea10591a4d)


***Relationship between Description length and Price or Rating***
![Screenshot 2024-05-13 214023](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/ca795ba2-9e4e-4398-aeac-149fa6af769a)
![Screenshot 2024-05-13 214037](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/4a4a137c-bc17-4a38-bb4a-2043fc76874f)


***Clustering of Products based on Categories and Pricing***
![Screenshot 2024-05-13 214911](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/825892f8-c9b5-4ab1-bcc1-9d9f950068c1)



***Discount Percentage across Different Brands***
![Screenshot 2024-05-13 215704](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/d9a7fa3e-025b-4f18-b203-93b1fb64c7da)




**Insights analysis to improve Product Recommendations**


***Rating Distribution***
![Screenshot 2024-05-13 220326](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/8607c0d1-5394-48b9-b7ab-aa336e53b578)


***Product Category Distribution***
![Screenshot 2024-05-13 220539](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/582102b7-87a5-402a-8fde-79e11880c29f)


***Rating Distribution by Category***
![Screenshot 2024-05-13 220844](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/e4f4d13b-f611-4df7-937a-7bb6f7215812)


***Rating Count***
![Screenshot 2024-05-13 221056](https://github.com/Riku1014/Amazon-Review-Data-EDA-Project-05/assets/164614767/f9c5709b-8d8d-4f17-a364-dc2c26d9de81)




## Conclusion
**Data Quality Assurance:**
*The code ensures data quality through rigorous cleaning and preprocessing steps, enhancing the reliability of subsequent analyses.*

**Visual Representation:**
*Visualizations aid in presenting complex data structures and patterns in an accessible format, facilitating easier interpretation and understanding.*

**Continuous Improvement Encouraged:**
*The exploratory data analysis process is iterative, allowing for continuous refinement and improvement of analytical techniques and insights..*

