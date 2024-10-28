#Sentence & Words Tokenization

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt_tab')
text = "This is smaple sentence and my name Sarvesh"
words = word_tokenize(text)
print(words)
sentence = sent_tokenize(text)
print(sentence)