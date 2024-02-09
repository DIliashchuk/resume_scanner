import pandas as pd
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Step 1: Load the dataset
df = pd.read_csv("combined_dataset.csv")
# Preprocess the data as needed

# Step 2: Split the dataset
train_data = df.sample(frac=0.8, random_state=42)
test_data = df.drop(train_data.index)

# Step 3: Tokenize the text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_data['text'])
train_sequences = tokenizer.texts_to_sequences(train_data['text'])
test_sequences = tokenizer.texts_to_sequences(test_data['text'])

# Step 4: Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=100),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Step 5: Train the model
model.fit(train_sequences, train_data['label'], epochs=10, batch_size=32, validation_data=(test_sequences, test_data['label']))

# Step 6: Evaluate the model
loss, accuracy = model.evaluate(test_sequences, test_data['label'])
print(f"Test loss: {loss}, Test accuracy: {accuracy}")

# Step 7: Make predictions
new_resume = ["Your new resume text here"]
new_sequences = tokenizer.texts_to_sequences(new_resume)
padded_sequences = pad_sequences(new_sequences, maxlen=max_sequence_length)  # adjust maxlen as needed
predictions = model.predict(padded_sequences)
