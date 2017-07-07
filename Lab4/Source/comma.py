print("Enter the sequence of words:") # ask for sequence of words
s=input()                      # take input
words=[word for word in s.split(",")] # use of split function on the words
print("The sorted sequence of words are:")
print(",".join(sorted(list(set(words))))) # printing the sorted words using join()
