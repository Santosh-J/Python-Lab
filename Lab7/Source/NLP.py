
#importing the modules for nlp
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize # for tokenizing
from nltk.stem import WordNetLemmatizer # for lemmatizing
# file open
file1 = open("test.txt")
#file read
file1 = file1.read()# Use this to read file content as a stream:
print("The words are:")
# print file
print(file1)
#use of stopwords
stop_words = set(stopwords.words("english"))
# split of file!
words = file1.split()
# creation of filtered words
for r in words:
    if not r in stop_words:
         appendFile = open('filtered.txt','a')
         appendFile.write(" "+r)
         appendFile.close()

# tokenizing file
wordss =word_tokenize(file1)
filtered_senten = []
#Appending
for w in wordss:
    if w not in stop_words and not w.isdigit() and len(w)>1:
        filtered_senten.append(w)

print(filtered_senten)
# lemmatizing
print ("Lemmatization:\n")
lemmatize = WordNetLemmatizer()
lemma_words = []
for w in filtered_senten:
    lemma_words.append(lemmatize.lemmatize(w, pos='v'))
print(lemma_words)
# printing the pos  verbs
print("POS verbs are:")

print (nltk.pos_tag(lemma_words))
print("After removing of POS verbs:\n")
for tag in nltk.pos_tag(lemma_words):
    if(tag[1].startswith('VB')):
        lemma_words.remove(tag[0])
print (lemma_words)

#print common words
print ("Common words are:\n")
filedist = nltk.FreqDist(lemma_words)
#use of for loop for frequency in filedist

for w, frequency in filedist.most_common(50):
    print(u'{}-{}'.format(w, frequency))

# most frequent words
print("Top 5 most frequent words:")

for w, frequency in filedist.most_common(5):
    print(u'{}-{}'.format(w, frequency))
# print the most frequent repeated words

fildist = nltk.FreqDist(wordss)
file_repword=[]
for w, frequency in fildist.most_common(5):
    print(u'{}-{}'.format(w, frequency))
    file_repword.append(w)

print("Frequent Words in file are:\n")
# printing of freq words
print (file_repword)







