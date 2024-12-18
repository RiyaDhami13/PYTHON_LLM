# Instantiate the pipeline
generator = pipeline(task="text-generation", model="gpt2")

response = "Dear valued customer, I am glad to hear you had a good stay with us."

# Complete the prompt
prompt = f"Customer review:\n{text}\n\nHotel reponse to the customer:\n{response}"

# Complete the model pipeline
outputs = generator(prompt, max_length=150, pad_token_id=generator.tokenizer.eos_token_id, truncation=True)

print(outputs[0]["generated_text"])