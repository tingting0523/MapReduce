#!/usr/bin/env python
import sys
import re

#--- get all lines from stdin ---
for line in sys.stdin:  
    #--- remove leading and trailing whitespace---
    line = line.strip() 
    
    #--- split the line into words ---
    words = line.split() 
    
    if len(words) != 2:
        continue  
    
    word, count = words[0], words[1]
    
    word = re.sub(r'^[^\w]+|[^\w]+$', '', word)  

    if '--' in word:  
        parts = re.split(r'[^\w\']+', word)  
    else:
        parts = [word]
    
    for part in parts:
        if part:  
            print('%s\t%s' % (part.lower(), count)) 
