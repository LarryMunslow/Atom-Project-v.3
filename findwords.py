# This program will search input text content and count the words that match
# positive and negative word lists

# open the postive and negative list files and store the data into a structure.
# The list will need to store the word and a count field. The count field is
# always a positive number.
# imports
import sys
import matplotlib.pyplot as plt
import re
# data structures and classes
# wordElement class.
class WordElement():
    "Stores word and count"
    def __init__(self, word, n):
        self.word = word
        self.count = n

    def __iter__(self):
        return iter(self.word)

    def increment_count(self):
        self.count +=1

# store for positive words with count
positive_word_count = []

# store for neutral words with count
total_word_count = []

# store for negative words with count
negative_word_count = []

# store for optimistic words with count
optimistic_word_count = []

# store for innocent words with count
innocent_word_count = []
#
# end of data structure definitions
#

def findwrd(obj, line):
    """ find a word and count it """
    sentence_words = line.split()
    for wrd in sentence_words:
        wrd = wrd.strip()
        wrd = wrd.lower()
        print "{0}".format(obj.word)
        if wrd.find(obj.word) != -1:
            obj.increment_count()
# variable to hold positive words and count field
# read and count words in contents file
#file = open("content.txt")
#for wrd in file.read():
#    if wrd not in total_word_count:
#        total_word_count[wrd] = 1
#    else:
#        total_word_count[wrd] += 1
#    for k,v in total_word_count.itsoms():
#        print k,v


# read positive.rtf
#pf = open('positive.txt', 'rt')
# loop reading each line
#for i, line in enumerate(pf):
#    data = line.strip()
#    positive_word_count.append(WordElement(data, 0))

# debug lines below to show word in lists
#for i in range(0,3):
#    print "%d: %s" % (i, positive_word_count[i].word)


# read negative.rtf
#pf = open('negative.txt', 'rt')
# loop reading each line
#for i, line in enumerate(pf):
#    data = line.strip()
#    negative_word_count.append(WordElement(data, 0))

# loop reading each line
#for i, line in enumerate(pf):
#    data = line.strip()
#    total_word_count.append(WordElement(data,0))

# read optimisism.rtf
pf = open('optimism.rtf', 'rt')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    optimistic_word_count.append(WordElement(data, 0))

# read innocence.rtf
pf = open('innocence.rtf', 'rt')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    innocent_word_count.append(WordElement(data, 0))


# debug lines below to show word in lists
#for i in range(0,3):
#    print "%d: %s" % (i, negative_word_count[i].word)

# search for a string
#searchfile('content.rtf', 'This')
pcontent = open('content.txt', 'rt')




# look for positive words first
#[findwrd(obj, line) for x, obj in enumerate(positive_word_count) for line
# in pcontent]
for line in pcontent:
    sentence_words = line.split()
    for wrd in sentence_words:
        wrd = wrd.strip()
        wrd = wrd.lower()
        #print "{0}".format(wrd)
        #for obj in positive_word_count:
            #print "    {0}".format(obj.word)
        #    if wrd.find(obj.word) != -1:
        #        obj.increment_count()
        #for newobj in negative_word_count:
        #    if wrd.find(newobj.word) != -1:
        #        newobj.increment_count()
        for newobj1 in optimistic_word_count:
            if wrd.find(newobj1.word) != -1:
                newobj1.increment_count()
        for newobj2 in innocent_word_count:
            if wrd.find(newobj2.word) != -1:
                newobj2.increment_count()
        #for newobj1 in total_word_count:
        #    if wrd.find(newobj1.word) != -1:
        #        newobj1.increment_count()


#for obj in positive_word_count:
#    if obj.count > 0:
#        print "{0}".format(obj.word)
#        print "{0}".format(obj.count)

#for obj in negative_word_count:
#    if obj.count > 0:
#        print "{0}".format(obj.word)
#        print "{0}".format(obj.count)

for obj in optimistic_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

for obj in innocent_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

for obj in total_word_count:
    if obj.count > 0:
        print "{0}".format(obj.count)

# sum all the counts
#positive_total_count = 0
#negative_total_count = 0
optimistic_total_count = 0
innocent_total_count = 0
total_doc_count = 0

#for obj in positive_word_count:
#    positive_total_count += obj.count

#print " Total Positive count is {0}".format(positive_total_count)

#for obj in negative_word_count:
#    negative_total_count += obj.count

#print " Total Negative count is {0}".format(negative_total_count)

for obj in optimistic_word_count:
    optimistic_total_count += obj.count

print " Total Optimistic count is {0}".format(optimistic_total_count)

for obj in innocent_word_count:
    innocent_total_count += obj.count

print " Total Innocent count is {0}".format(innocent_total_count)

for obj in total_word_count:
    total_doc_count += obj.count

print "  Total document count is {0}".format(total_doc_count)

#plot stuff
