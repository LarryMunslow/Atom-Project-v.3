# This program will search input text content and count the words that match
# positive and negative word lists

#
# open the postive and negative list files and store the data into a structure.
# The list will need to store the word and a count field. The count field is
# always a positive number.
# imports
import sys
import matplotlib as mpl
import re
import string
import glob, os
# import collections

#

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

# store for optimistic words with count
#optimistic_word_count = []

# store for WarEvent words with count
War_word_count = []

# store for religious words with count
#religious_word_count = []

# store for nostalgic words with count
#nostalgia_word_count = []
#
# end of data structure definitions
#
def exact_match(phrase, word):
    b = r'(\s|^|$)'
    return re.match(b + word + b, phrase)

# variable to hold positive words and count field

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

# debug lines below to show word in lists
#for i in range(0,3):
#    print "%d: %s" % (i, negative_word_count[i].word)

# read optimisism.rtf
#pf = open('optimism.rtf', 'rt')
# loop reading each line
#for i, line in enumerate(pf):
#    data = line.strip()
#    optimistic_word_count.append(WordElement(data, 0))

# read War.rtf
pf = open('War.rtf')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    War_word_count.append(WordElement(data, 0))

# read religious.rtf
#pf = open('religious.rtf')
# loop reading each line
#for i, line in enumerate(pf):
#    data = line.strip()
#    religious_word_count.append(WordElement(data, 0))

# read nostalgia.rtf
#pf = open('nostalgia.rtf')
# loop reading each line
#for i, line in enumerate(pf):
#    data = line.strip()
#    nostalgia_word_count.append(WordElement(data, 0))


# search for a string
#searchfile('content.rtf', 'This')
pcontent = open('content.txt', 'rt')

# look for positive words first
#[findwrd(obj, line) for x, obj in enumerate(positive_word_count) for line
# in pcontent]
for line in pcontent:
    sentence_words = line.split()
    for wrd in sentence_words:
        wrd = wrd.strip('.,!?:;()_-')
        wrd = wrd.lower()
        #print "{0}".format(wrd)

        #for newobj in optimistic_word_count:
        #    if exact_match(wrd, newobj.word) != None:
        #        newobj.increment_count()
        for newobj1 in War_word_count:
            if exact_match(wrd, newobj1.word) != None:
                newobj1.increment_count()
        #for newobj2 in religious_word_count:
        #    if exact_match(wrd, newobj2.word) != None:
        #        newobj2.increment_count()
        #for newobj3 in nostalgia_word_count:
        #    if exact_match(wrd, newobj3.word) != None:
        #        newobj3.increment_count()

#for obj in optimistic_word_count:
#    if obj.count > 0:
#        print "{0}".format(obj.word)
#        print "{0}".format(obj.count)

for obj in War_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

#for obj in religious_word_count:
#    if obj.count > 0:
#        print "{0}".format(obj.word)
#        print "{0}".format(obj.count)

#for obj in nostalgia_word_count:
#    if obj.count > 0:
#        print "{0}".format(obj.word)
#        print "{0}".format(obj.count)


#optimistic_total_count = 0
War_total_count = 0
#religious_total_count = 0
#nostalgia_total_count = 0

#for obj in optimistic_word_count:
#    optimistic_total_count += obj.count

#print " Total Optimistic count is {0}".format(optimistic_total_count)

for obj in War_word_count:
    War_total_count += obj.count

print " Total War count is {0}".format(War_total_count)

#for obj in religious_word_count:
#    religious_total_count += obj.count

#print " Total Religious count is {0}".format(religious_total_count)

#for obj in nostalgia_word_count:
#    nostalgia_total_count += obj.count

#print " Total Nostalgia count is {0}".format(nostalgia_total_count)

#plot stuff
