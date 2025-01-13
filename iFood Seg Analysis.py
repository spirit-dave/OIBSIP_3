import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the directory exists
os.makedirs('visualizations', exist_ok=True)

# Load the dataset
data = pd.read_csv('ifood_df.csv')

# Feature Selection
selected_features = [
    'Income', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts',
    'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
    'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth'
]

# Data Cleaning
data_cleaned = data[selected_features].dropna()

# Calculate Key Metrics
data_cleaned['TotalPurchases'] = (
    data_cleaned['NumDealsPurchases'] +
    data_cleaned['NumWebPurchases'] +
    data_cleaned['NumCatalogPurchases'] +
    data_cleaned['NumStorePurchases']
)
data_cleaned['TotalSpending'] = (
    data_cleaned['MntWines'] +
    data_cleaned['MntFruits'] +
    data_cleaned['MntMeatProducts'] +
    data_cleaned['MntFishProducts'] +
    data_cleaned['MntSweetProducts'] +
    data_cleaned['MntGoldProds']
)
data_cleaned['AvgPurchaseValue'] = (
    data_cleaned['TotalSpending'] / data_cleaned['TotalPurchases']
)

# Display Key Metrics
print("Summary of Key Metrics:")
print(data_cleaned[['TotalPurchases', 'TotalSpending', 'AvgPurchaseValue']].describe())

# Save Key Metrics to a CSV
data_cleaned[['TotalPurchases', 'TotalSpending', 'AvgPurchaseValue']].to_csv('key_metrics_summary.csv', index=False)

# Data Normalization
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data_cleaned[selected_features])

# Elbow Method to Determine Optimal Clusters
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(normalized_data)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.grid()
plt.savefig('visualizations/elbow_method.png')
plt.show()

# Apply K-Means Clustering
optimal_clusters = 4  # Replace with the number determined by the Elbow Method
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42, n_init=10)
kmeans.fit(normalized_data)
data_cleaned['Cluster'] = kmeans.labels_

# Visualize the Clusters
sns.pairplot(data_cleaned, hue='Cluster', diag_kind='kde')
plt.savefig('visualizations/cluster_pairplot.png')
plt.show()
