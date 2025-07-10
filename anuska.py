import nltk

# Download only the most commonly used modules
nltk.download('punkt')                     # Tokenizer
nltk.download('stopwords')                 # Stopword list
nltk.download('wordnet')                   # WordNet Lemmatizer
nltk.download('averaged_perceptron_tagger')# Part-of-speech tagger
nltk.download('maxent_ne_chunker')         # Named Entity Recognition
nltk.download('words')                     # English word list for NER

print("All selected NLTK modules downloaded successfully.")