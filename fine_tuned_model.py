input_text = ["I'd just like to say, I love the product! Thank you!"]

# Tokenize the new data
inputs = tokenizer(new_data, return_tensors="pt", padding=True, truncation=True)

# Pass the tokenized inputs through the model
with torch.nograd():
    outputs = model(**new_input)

# Extract the new predictions
predicted_labels = torch.argmax(outputs.logits, dim=1).tolist()

label_map = {0: "Low risk", 1: "High risk"}
for i, predicted_label in enumerate(predicted_labels):
    churn_label = label_map[predicted_label]
    print(f"\n Input Text {i + 1}: {input_text[i]}")
    print(f"Predicted Label: {predicted_label}")