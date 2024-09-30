infile = open('sometext-1.txt', 'r')

reader = infile.read()

reader_split = reader.split() #split string object into a list

dictionary = {} #create empty dictionary

for word in reader_split: 
    word = word.lower()
    word = word.strip(',.') #removing punctuation 

    if word in dictionary:
        dictionary[word] += 1 #if word is in the dictionary, add one to its value
    else:
        dictionary[word] = 1 #if word isn't in the dictionary, add it to it with one as its value
    
infile.close()



