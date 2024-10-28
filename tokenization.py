import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download the 'punkt' resource for tokenization
nltk.download('punkt')

text = "This is a sample sentence and my name is Sarvesh."

# Word tokenization
words = word_tokenize(text)
print(words)

# Sentence tokenization
sentence = sent_tokenize(text)
print(sentence)
