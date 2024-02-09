import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
# Step 1: Import Necessary Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Collect Relevant Datasets
# Assume you have a CSV file with movie reviews and sentiment labels (positive/negative)
# Replace 'your_dataset.csv' with the path to your dataset
dataset_path = 'combined_dataset.csv'
df = pd.read_csv(dataset_path, on_bad_lines='skip')

# Step 3: Data Preprocessing
# Assume the dataset has columns 'text' for the review and 'sentiment' for the label
X = df['text']
y = df['sentiment']

# Step 4: Feature Engineering
# Using simple Bag of Words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Step 5: Model Selection
# Using Naive Bayes classifier as an example
model = MultinomialNB()

# Step 6: Training the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Step 7: Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2%}')
print('Classification Report:\n', report)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Collect Relevant Datasets
# Assume you have a CSV file with movie reviews and sentiment labels (positive/negative)
# Replace 'your_dataset.csv' with the path to your dataset
dataset_path = 'combined_dataset.csv'
df = pd.read_csv(dataset_path, on_bad_lines='skip')

# Step 3: Data Preprocessing
# Assume the dataset has columns 'text' for the review and 'sentiment' for the label
X = df['text']
y = df['sentiment']

# Step 4: Feature Engineering
# Using simple Bag of Words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Step 5: Model Selection
# Using Naive Bayes classifier as an example
model = MultinomialNB()

# Step 6: Training the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Step 7: Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2%}')
print('Classification Report:\n', report)
