from nltk.tokenize import word_tokenize
from nltk import sent_tokenize as st
from nltk.probability import FreqDist as fr
import matplotlib.pyplot as plt

text = "Hello, world! This is a test."
tokens = word_tokenize(text)
print(tokens)
print(st(text))
p=fr(tokens)
print(p.most_common(3))
p.plot(40)
plt.show()