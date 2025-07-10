# from nltk.tokenize import word_tokenize as wt
# from nltk.tokenize import sent_tokenize as st
# from nltk.probability import FreqDist as fd
# from nltk.corpus import stopwords as sw
# import matplotlib.pyplot as plt

# text="hello i am a good.boy in ev;ery wat. aim"
# tok=wt(text)
# ste=st(text)
# p=fd(tok)
# # p.plt(40)
# # plt.show()
# # print(sw.words("english"))
# lst=[]
# for i in tok:
#     if i not in sw.words("english"):
#         lst.append(i)
# print(lst)
# print(set(tok)-set(lst))
import nltk
nltk.download("wordnet")