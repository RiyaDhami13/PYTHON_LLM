# Import the function for loading Hugging Face pipelines
from transformers import pipeline

review = "The food was good, but service at the restaurant was a bit slow"

# Load the pipeline for text classification
classifier = pipeline(task="text-classification", model=model_name)

# Pass the customer review to the model for prediction
prediction = classifier(review)
print(prediction)