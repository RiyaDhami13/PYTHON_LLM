question = "Who painted the Mona Lisa?"

# Define the appropriate model
qa = pipeline(task="question-answering", model="gpt2")

input_text = f"Context: {text}\n\nQuestion: {question}\n\nAnswer:"

output = qa({"context": text, "question": question}, max_length=150)
print(output['answer'])


question = "Who painted the Mona Lisa?"

# Define the appropriate model
qa = pipeline(task="question-answering", model="distilbert-base-uncased-distilled-squad")

output = qa(question=question, context=text)
print(output['answer'])