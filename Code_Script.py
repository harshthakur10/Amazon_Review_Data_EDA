-- Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

-- LOAD DATA:
data = pd.read_csv('amazon.csv') #Read the CSV File.

data.head() #Checking and have a look of the Head and Top 5 Row of Data.

-- DATA CLEANING:
data.isnull().sum() #Checking Null Value. 

#convert Dtype and removing the symbol from the data
numeric_columns = ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']
for column in numeric_columns:
    data[column] = data[column].astype(str).str.replace(',', '').str.replace('₹', '').str.replace('%', '').str.replace('|', '')
    data[column] = data[column].apply(lambda x: float(x) if x.strip() else None)

# Droping null values
data = data.dropna()
data.isnull().sum()

-- DATA UNDERSTANDING:
# Describe the data and print Statistical view
data.describe()
data.describe(include=object)

-- DATA EXPLORATION:
## After cleaning the data checking the Head of the data 
data.head()

#info of the data
data.info()

#Checking the Shape of the data
data.shape

-- FINDING INSIGHTS AFTER CLEANING THE DATA
 ## How are product prices distributed, and are there notable outliers?
price_columns = ['discounted_price', 'actual_price']
data[price_columns] = data[price_columns].replace('[\₹,]', '', regex=True).astype(float)

# Calculate summary statistics
price_summary = data[price_columns].describe()

# Plot boxplot to visualize the distribution and identify outliers
plt.figure(figsize=(10, 6))
data[price_columns].boxplot()
plt.title('Distribution of Product Prices')
plt.ylabel('Price (INR)')
plt.xticks(range(1, len(price_columns) + 1), price_columns)
plt.show()

# Print summary statistics
print("Summary Statistics of Product Prices:")
print(price_summary)

## What is the average rating across different product categories ?
# Group the data by 'category' and calculate the average rating for each category
average_rating_by_category = data.groupby('category')['rating'].mean()

# Print or display the average ratings for each category
print("Average Rating Across Different Product Categories:")

print(average_rating_by_category)

average_rating_by_category = data.groupby('category')['rating'].mean().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
average_rating_by_category.plot(kind='barh', color='skyblue')
plt.title('Average Rating Across Different Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Print average rating by category
print("Average Rating Across Different Product Categories:")
print(average_rating_by_category)

## Is there a correlation between discount percentage and product rating?
# Calculate the correlation between 'discount_percentage' and 'rating'
correlation = data['discount_percentage'].corr(data['rating'])

# Print the correlation coefficient
print("Correlation between Discount Percentage and Product Rating:", correlation)

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='discount_percentage', y='rating', data=data)
plt.title('Discount Percentage vs. Product Rating')
plt.xlabel('Discount Percentage')
plt.ylabel('Product Rating')
plt.grid(True)
plt.show()

# Correlation coefficient
correlation = data['discount_percentage'].corr(data['rating'])
print("Correlation coefficient between discount percentage and product rating:", correlation)

## What are the top 5 most reviewed products, and what insights do their reviews offer?
# Sort the dataset by 'rating_count' column in descending order
top_reviewed_products = data.sort_values(by='rating_count', ascending=False).head(5)

# Display the top 5 most reviewed products
print("Top 5 Most Reviewed Products:")
print(top_reviewed_products[['product_name', 'rating_count']])

review_counts = data.groupby('product_id')['review_id'].count()

# Step 2: Sort products based on the number of reviews in descending order and get the top 5 most reviewed products
top_reviewed_products = review_counts.nlargest(5)

# Step 3: Extract reviews for the top 5 most reviewed products
top_reviews = data[data['product_id'].isin(top_reviewed_products.index)]

# Step 4: Analyze the reviews to gain insights
# For example, you can print the product names and the number of reviews for each product
print("Top 5 Most Reviewed Products:")
for product_id, review_count in top_reviewed_products.items():
    product_name = data[data['product_id'] == product_id]['product_name'].iloc[0]
    print(f"{product_name}: {review_count} reviews")

# Plotting the number of reviews for each product
plt.figure(figsize=(10, 6))
top_reviewed_products.plot(kind='bar', color='skyblue')
plt.title('Top 5 Most Reviewed Products')
plt.xlabel('Product ID')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

## Are certain product categories more frequently discounted?
# Calculate the frequency of discounts for each product category
discount_frequency = data.groupby('category')['discount_percentage'].apply(lambda x: (x != 0).sum() / len(x) * 100)

# Sort the categories based on discount frequency in descending order
discount_frequency = discount_frequency.sort_values(ascending=False)

# Display the result
print("Frequency of Discounts by Product Category:")
print(discount_frequency)

## Do higher-priced products tend to receive higher ratings?
# Calculate the correlation between product prices and ratings
correlation = data['actual_price'].corr(data['rating'])

# Display the correlation coefficient
print("Correlation between Product Prices and Ratings:", correlation)

price_ranges = [(0, 100), (100, 200), (200, 300), (300, 400), (400, 500), (500, 600), (600, 700), (700, 800), (800, 900), (900, 1000)]

# Create a function to assign price range labels
def assign_price_range(price):
    for i, (start, end) in enumerate(price_ranges):
        if start <= price < end:
            return f"${start}-{end}"

# Apply the price range function to create a new column 'price_range'
data['price_range'] = data['actual_price'].apply(assign_price_range)

# Calculate the average rating for each price range
avg_rating_by_price_range = data.groupby('price_range')['rating'].mean()

# Plotting
plt.figure(figsize=(10, 6))
avg_rating_by_price_range.plot(kind='bar', color='skyblue')
plt.title('Average Rating by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

## Is there a relationship between description length and price or rating?
data['description_length'] = data['about_product'].str.len()

# Plotting the relationship between description length and price
plt.figure(figsize=(10, 6))
plt.scatter(data['description_length'], data['actual_price'], alpha=0.5)
plt.title('Description Length vs. Product Price')
plt.xlabel('Description Length')
plt.ylabel('Product Price')
plt.grid(True)
plt.show()

# Plotting the relationship between description length and rating
plt.figure(figsize=(10, 6))
plt.scatter(data['description_length'], data['rating'], alpha=0.5)
plt.title('Description Length vs. Product Rating')
plt.xlabel('Description Length')
plt.ylabel('Product Rating')
plt.grid(True)
plt.show()

## How do ratings differ between products with high and low review counts?
high_review_threshold = 100  # Example threshold for high review count
low_review_threshold = 10    # Example threshold for low review count

# Categorize products based on review counts
data['review_count_category'] = pd.cut(data['rating_count'], 
                                       bins=[0, low_review_threshold, high_review_threshold, float('inf')],
                                       labels=['Low Review Count', 'Medium Review Count', 'High Review Count'])

# Calculate average rating for each review count category
average_rating_by_review_count = data.groupby('review_count_category')['rating'].mean()

# Plotting
plt.figure(figsize=(8, 6))
average_rating_by_review_count.plot(kind='bar', color='lightgreen')
plt.title('Average Rating by Review Count Category')
plt.xlabel('Review Count Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=0, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Print average rating by review count category
print("Average Rating by Review Count Category:")
print(average_rating_by_review_count)

## Can products be clustered based on features and pricing?
# Classifying Category column
data['main_category'] = data['category'].astype(str).str.split('|').str[0]
data['sub_category'] = data['category'].astype(str).str.split('|').str[-1]

df_cat = data['category'].str.split('|', expand=True).rename(columns={0:'category_1', 1:'category_2', 2:'category_3', 3:'category_4',4:'category_5'})
 
data['category_1'] = df_cat['category_1']
data['category_2'] = df_cat['category_2']
data['category_3'] = df_cat['category_3']
data['category_4'] = df_cat['category_4']

# PLotting

plt.figure(figsize=(8,6))
sns.scatterplot(data=data, x='category_2', y='actual_price')
plt.title('Clustering of Products based on Category and Price')
plt.xlabel('Category')
plt.xticks(rotation=90)
plt.ylabel('Price')
plt.show()

## How does the discount percentage vary across different brands?
data['pro_name'] = data['product_name'].str.split(',').str[0]
data['pro_name']

top_products = data['pro_name'].value_counts().head(30)
dp=data['discount_percentage'].head(30)

# Plotting

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.index, y=dp, palette='viridis')
plt.title('Top-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Discount Percentage')
plt.xticks(rotation=90)
plt.show()

## Is there a relationship between the number of images and sales performance?
data.columns

data['sales_performance'] = data['discounted_price']/ data['actual_price'] * 100
data['Number_of_Images'] = data['img_link'].apply(lambda x: len(x.split(',')))

# Plotting

plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x='Number_of_Images', y='sales_performance')
plt.title('Relationship between Number of Images and Sales Performance')
plt.xlabel('Number of Images')
plt.ylabel('Sales Performance')
plt.show()

## What are common keywords or phrases in product titles or descriptions?
data[['product_name']]

def extract_keywords(product_name):
    if isinstance(product_name, str):
        keywords = product_name.lower().split()
        clean_keywords = []
        for word in keywords:
            if word.isalpha():
                clean_keywords.append(word)
        return clean_keywords
    else:
        return []

data["keywords"] = data["product_name"].apply(extract_keywords)


all_keywords = []
for keywords in data["keywords"]:
    for keyword in keywords:
        all_keywords.append(keyword)
keyword_counts = pd.Series(all_keywords).value_counts()

print(keyword_counts.head(10))

## Can product rating be predicted based on features and category?
data[['category_1','rating']]

result1 = data.groupby('category_1')['rating'].agg(['min','max'])
result1

# Plotting

plt.figure(figsize=(10, 6))

result1.plot(kind='bar', color=['skyblue','lightgreen'])

plt.title('Ratings Summary by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Rating')
plt.legend(['Min Rating', 'Max Rating'])

plt.show()

## How can insights from this analysis improve product recommendations?
# Plotting

plt.figure(figsize=(10, 6))

sns.histplot(data=data, x='rating' ,bins=20, kde=True, color='skyblue')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('')
plt.show()

## PRODUCT CATEGORY DISTRIBUTION
# Plotting

plt.figure(figsize=(10, 8))
sns.countplot(data=data, y='main_category', order=data['main_category'].value_counts().index, palette='viridis')
plt.title('Distribution of Products by Main Category')
plt.xlabel('Number of Products')
plt.ylabel('Main Category')
plt.show()

## Top Selling Products
# Plotting

top_products = data['pro_name'].value_counts().head(25)

c=data['user_name'].value_counts().head(25)

plt.figure(figsize=(10, 6))
sns.barplot(y=top_products.index, x=c.values, palette='viridis')
plt.title('Top-Selling Products')
plt.ylabel('Product Name')
plt.xlabel('Number of Sales')
plt.xticks(rotation=0)  
plt.show()

## Rating Distribution by Category
# Plotting

plt.figure(figsize=(10, 6))
sns.lineplot(x='rating_count', y='category_1', data=data, sort=False)

plt.title('Top 20 Ratings by Category')
plt.xlabel('Rating Count')
plt.ylabel('Category')

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

## The Correlation between discounted_price and rating:
correlation_coefficient = data["discounted_price"].corr(data["rating"])

print(f"Correlation between discounted_price and rating: {correlation_coefficient:.2f}")

## The most popular Product name:
product_counts = data["product_name"].value_counts()

print(product_counts.sort_values(ascending=False).head(10))

## Rating Count
# Plotting
plt.figure(figsize=(8,6))
sns.countplot(data=data, x='rating')
plt.tight_layout()


## Most popular words in Review in a picture
from wordcloud import WordCloud

reviews_text = ' '.join(data['review_content'].dropna().values)
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(reviews_text)
plt.figure(figsize=(6, 6), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

## How can insights from this analysis improve product recommendations?
Insights from the analysis of the Amazon dataset can lead to several improvements in product recommendations. Here are some potential insights and how they can be used to enhance recommendations:

Correlation between Price and Rating:

If there's a positive correlation between the actual price and rating, it suggests that higher-priced products tend to receive higher ratings.
Correlation between Description Length and Price/Rating:

If there's a correlation between the length of product descriptions and price/rating, it indicates that more detailed descriptions might influence the perceived value or quality of the product.
User Preferences and Behavior Analysis:

Analyzing user reviews, ratings, and interactions with products can provide insights into their preferences, interests, and purchasing behavior.
Feedback Loop for Product Improvement:

Monitoring user reviews and feedback can help identify areas for product improvement or features that users appreciate.
Personalized Recommendations:

Utilizing machine learning algorithms to create personalized recommendations tailored to each user's preferences, browsing history, purchase history, and demographic information.
                      
