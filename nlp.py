corpus=""""" Hello Welcome, to Krish Naik's NLP Tutorials.
Please do watch the entrie course! to become expert in NLP.
"""

print(corpus)

from nltk.tokenize import sent_tokenize

sent_tokenize(corpus)

documents=sent_tokenize(corpus)
type(documents)

for i in documents:
    print(i)


from nltk.tokenize import word_tokenize

word_tokenize(corpus)