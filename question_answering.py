question = "Who painted the Mona Lisa?"

# Define the appropriate model
qa = pipeline(task="question-answering", model="distilbert-base-uncased-distilled-squad")

output = qa(question=question, context=text)
print(output['answer'])