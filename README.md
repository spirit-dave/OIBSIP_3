# Customer Segmentation Analysis

## Overview

This project performs customer segmentation on an e-commerce dataset, specifically focusing on customer spending behaviors and demographics. The goal of the analysis is to identify distinct customer segments using unsupervised machine learning, specifically KMeans clustering.

## Dataset

The dataset used in this analysis is the ifood_df.csv, which contains customer information such as:

- Income: Customer's annual income

- Kidhome: Number of children in the household

- Teenhome: Number of teenagers in the household

- Recency: Number of days since the customer's last purchase

- MntTotal: Total spending of the customer

- NumWebPurchases: Number of purchases made through the website

- NumCatalogPurchases: Number of purchases made through catalogs

- NumStorePurchases: Number of purchases made in stores

- NumWebVisitsMonth: Number of visits to the website per month

- Age: Customer's age

## Analysis Workflow
### Data Preprocessing:

The dataset is cleaned and features are standardized using StandardScaler for efficient clustering.

### Clustering:

KMeans clustering with k=4 clusters is applied to identify customer segments based on the provided features. This number of clusters was selected after analyzing the dataset and evaluating different clustering methods.

### Visualization:

- Scatter Plot: A scatter plot of Income vs. MntTotal is created to visualize customer segments based on income and total spending.

- Bar Chart: A bar chart is created to show the average total spending for each customer cluster.

## Insights and Recommendations from Analysis

- Cluster 0: Budget-Conscious Shoppers

- Income: Likely to have low to mid-range income.

- Kidhome/Teenhome: May have fewer children or teenagers, suggesting they might not be shopping for large family needs.

- MntTotal: Lower average spending compared to other clusters.

- Recency: These customers might not shop frequently.

- Purchases: Likely to make more store and catalog purchases rather than web-based purchases.

### Insight
This segment consists of customers with lower spending power who prefer traditional shopping methods. They may look for budget-friendly products and promotions.

## Cluster 1: High-Spending, Frequent Shoppers

- Income: High income levels, suggesting they are more financially stable or affluent.

- MntTotal: High total spending, which is consistent with their higher income.

- Recency: These customers shop more frequently, suggesting that they are active and loyal customers.

- Purchases: Likely to make purchases both online and in stores, possibly favoring online for convenience.

- Insight: This segment represents high-value customers who make frequent purchases and spend a lot. Targeting them with premium products or loyalty rewards would be effective.

## Cluster 2: Middle-Aged Parents with Moderate Spending

- Income: Mid-range income.

- Kidhome/Teenhome: Likely to have children, both younger and teenagers.

- MntTotal: Moderate spending compared to other clusters.

- Purchases: Tend to shop both online and in stores, though their total spending may not be as high as Cluster 1.

### Insight 
These customers may be looking for family-oriented products. They may value convenience but also consider product quality. Offering family bundles or discounts might appeal to them.

## Cluster 3: Younger Shoppers with Moderate to Low Spending

- Income: Lower to moderate income.

- Age: Typically younger customers.

- MntTotal: Lower spending compared to other clusters.

- Recency: May shop infrequently, possibly due to lower disposable income or shifting priorities.

- Purchases: Likely to make more online purchases, driven by ease and discounts.

### Insight 
This segment could represent students or early-career individuals. Targeting them with affordable, trendy, or tech-related products could be effective. Discounts and promotional offers may attract them to shop more often.

## Marketing Strategy Based on Insights

- Cluster 0 (Budget-Conscious Shoppers): Focus on offering discounts, bundle deals, and promotions that highlight affordability. Traditional marketing channels (catalogs, in-store events) may resonate more with them.

- Cluster 1 (High-Spending, Frequent Shoppers): Personalize marketing to make them feel valued. Offer loyalty programs, exclusive product launches, and personalized shopping experiences. This group could benefit from VIP memberships and early access to sales.

- Cluster 2 (Middle-Aged Parents): Highlight family-oriented products. Offer bundles, seasonal promotions, and items catering to children's needs. Advertise through both online and offline channels, focusing on product quality and convenience.

- Cluster 3 (Younger Shoppers): Engage with this group using online channels (social media, digital ads) and emphasize trendy, affordable products. Offer student discounts and limited-time offers to encourage more frequent purchases.

