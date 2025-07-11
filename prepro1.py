from nltk.tokenize import word_tokenize as wt
txt="this is a test sentence. this is another test sentence."
t=wt(txt)
print(len(t))