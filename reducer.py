#!/usr/bin/env python
import sys
# maps words to their counts
word2count = {}
# input comes from STDIN
for line in sys.stdin:
 # remove leading and trailing whitespace
    line = line.strip()
 # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
 # convert count (currently a string) to int
    try:
        word, count = line.split('\t', 1)
    except ValueError:
        continue

    try:
        count = int(count)
    except ValueError:
        continue

    if word in word2count:
        word2count[word] += count
    else:
        word2count[word] = count
        
# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    #print '%s\t%s'% ( word, word2count[word] )
    print('%s\t%s' % (word, word2count[word]))