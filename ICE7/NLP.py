import  nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.util import ngrams
from collections import Counter
from nltk import pos_tag, ne_chunk
import numpy

#nltk.download('all')
tokenizer = nltk.download('punkt')
fp = open("test.txt")
data = fp.read()

#to tokenize input text into sentences

#print('\n-----\n'.join(tokenizer.tokenize(data)))# splits text into sentences

#to tokenize the tokenized sentences into words

tokens = nltk.wordpunct_tokenize(data)
text = nltk.Text(tokens)
words = [w.lower() for w in text]
print(data)    #to print the tokens

#for a in data:
    #print (a)
for synset in wn.synsets(tokens[30]):
    for lemma in synset.lemmas():
       print(lemma.name())

stemmer=PorterStemmer()
print(stemmer.stem(tokens[38]))



lemmetizer= nltk.WordNetLemmatizer()
print(lemmetizer.lemmatize('Breathing',pos='v'))

print(pos_tag(words))





print (nltk.ngrams('hey all li lee', 3))


# nltk.download('all')
print (nltk.ne_chunk(pos_tag(nltk.wordpunct_tokenize("heya ola hows it"))))