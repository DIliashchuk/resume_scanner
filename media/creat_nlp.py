import spacy
import pandas as pd
from spacy.training.example import Example
import random

# Load the dataset
dataset_path = "combined_dataset.csv"  # Replace with the actual path
df = pd.read_csv(dataset_path, on_bad_lines='skip')

# Create a blank English model
nlp = spacy.blank("en")

# Define the pipeline components
ner = nlp.add_pipe("ner", last=True)

# Assuming your dataset has labeled entities, create training examples
training_data = []

for index, row in df.iterrows():
    text = row["Text"]
    entities = []  # Replace this with your actual labeled entities if available

    example = Example.from_dict(nlp.make_doc(text), {"entities": entities})
    training_data.append(example)

# Define the training configuration
config = {
    "Crf": {"c1": 0.1, "c2": 0.1},
    "ner": {
        "batch_size": 16,
        "epochs": 10,
        "learning_rate": 0.001,
        "dropout": 0.5,
        "gold_fraction": 0.25,
    },
}

# Train the spaCy model without minibatch
nlp.begin_training()
for epoch in range(config["ner"]["epochs"]):
    losses = {}
    random.shuffle(training_data)

    for example in training_data:
        nlp.update([example], drop=config["ner"]["dropout"], losses=losses)

    print(losses)

# Save the trained model to disk
output_dir = "/Users/dmytroiliashchuk/LearnML/ML_AI/resume_project/media"  # Replace with the desired output directory
nlp.to_disk(output_dir)
