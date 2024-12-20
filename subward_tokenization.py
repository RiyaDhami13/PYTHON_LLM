# Complete the function
def tokenize_function(data):
    return tokenizer(data["interaction"], 
                     return_tensors="pt", 
                     padding=True, 
                     truncation=True, 
                     max_length=64)

# Tokenize row by row
tokenized_by_row = train_data.map(tokenize_function,batched=False)

print(tokenized_by_row)

# Tokenize by batches
tokenized_batches = train_data.map(tokenize_function,batched=True)

print(tokenized_by_row)


