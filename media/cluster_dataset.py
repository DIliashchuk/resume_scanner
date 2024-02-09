import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

dataset = pd.read_csv('combined_dataset.csv', on_bad_lines='skip')

# Assuming the column containing resume text is named 'Text'
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(dataset['Text'])

# Apply K-means clustering
num_clusters = 5  # You can adjust the number of clusters based on your needs
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
dataset['Cluster'] = kmeans.fit_predict(X)

# Save the clustered dataset
dataset.to_csv('clustered_dataset.csv', index=False)





# on_bad_lines='skip'