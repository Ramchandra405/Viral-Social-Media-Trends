# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\CHINTAPALLI SIVA\Downloads\Viral_Social_Media_Trends.csv')


"""# Objective-1: Distribution Analysis"""
plt.figure(figsize=(18, 5))

# Views
plt.subplot(1, 3, 1)
sns.histplot(df['Views'], kde=True, color='skyblue')
plt.title('Views Distribution')

# Likes
plt.subplot(1, 3, 2)
sns.histplot(df['Likes'], kde=True, color='lightgreen')
plt.title('Likes Distribution')

# Shares
plt.subplot(1, 3, 3)
sns.histplot(df['Shares'], kde=True, color='salmon')
plt.title('Shares Distribution')

plt.tight_layout()
plt.show()


"""# Objective-2: Correlation Analysis"""
correlation_data = df[['Views', 'Likes', 'Shares', 'Comments']]

# Compute correlation matrix
correlation_matrix = correlation_data.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Plot the heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Correlation Between Views, Likes, Shares, and Comments")
plt.tight_layout()
plt.show()


"""# Objective-3: Outlier Detection"""
plt.figure(figsize=(12, 5))

# Views Outliers
plt.subplot(1, 2, 1)
sns.boxplot(x=df['Views'], color='lightblue')
plt.title("Outlier Detection - Views")

# Shares Outliers
plt.subplot(1, 2, 2)
sns.boxplot(x=df['Shares'], color='lightcoral')
plt.title("Outlier Detection - Shares")

plt.tight_layout()
plt.show()


"""# Objective-4: Content Type Insights"""
content_summary = df.groupby('Content_Type').agg(
    avg_likes=('Likes', 'mean'),
    avg_shares=('Shares', 'mean'),
    avg_comments=('Comments', 'mean')
).reset_index()

plt.figure(figsize=(14, 5))

# Likes by Content Type
plt.subplot(1, 3, 1)
sns.barplot(data=content_summary, x='Content_Type', y='avg_likes', hue='Content_Type', legend=False)
plt.title('Average Likes by Content Type')
plt.ylabel('Average Likes')
plt.xlabel('Content Type')

# Shares by Content Type
plt.subplot(1, 3, 2)
sns.barplot(data=content_summary, x='Content_Type', y='avg_shares', hue='Content_Type', legend=False)
plt.title('Average Shares by Content Type')
plt.ylabel('Average Shares')
plt.xlabel('Content Type')

# Comments by Content Type
plt.subplot(1, 3, 3)
sns.barplot(data=content_summary, x='Content_Type', y='avg_comments', hue='Content_Type', legend=False)
plt.title('Average Comments by Content Type')
plt.ylabel('Average Comments')
plt.xlabel('Content Type')

plt.tight_layout()
plt.show()


"""# Objective-5: Regional Analysis"""
region_summary = df.groupby('Region').agg(
    total_views=('Views', 'sum'),
    avg_likes=('Likes', 'mean')
).reset_index()

plt.figure(figsize=(14, 5))

# Total Views by Region
plt.subplot(1, 2, 1)
sns.barplot(data=region_summary, x='Region', y='total_views', hue='Region', legend=False)
plt.title('Total Views by Region')
plt.ylabel('Total Views')
plt.xlabel('Region')

# Average Likes by Region
plt.subplot(1, 2, 2)
sns.barplot(data=region_summary, x='Region', y='avg_likes', hue='Region', legend=False)
plt.title('Average Likes by Region')
plt.ylabel('Average Likes')
plt.xlabel('Region')

plt.tight_layout()
plt.show()
