translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")

# Translate the first input sentence then calucate the BLEU metric for translation quality
translated_output = translator(input_sentence_1)

translated_sentence = translated_output[0]['translation_text']

print("Translated:", translated_sentence)

results = bleu.compute(predictions=[translated_sentence], references=reference_1)
print(results)
