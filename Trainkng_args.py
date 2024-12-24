# Set up an instance of TrainingArguments
training_args = TrainingArguments(
  output_dir="./finetuned",

  # Set the evaluation strategy to epoch,
  evaluation_strategy ="epoch",

  # Specify the number of epochs
  num_train_epochs=3,

  learning_rate=2e-5,

  # Set the batch sizes

  per_device_train_batch_size=3,
  per_device_eval_batch_size=3,
  weight_decay=0.01
)