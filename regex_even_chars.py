#!/usr/bin/python

## find all occurrences of sub-strings in the whole text 
## which consist of even number of same word characters

import re

s = "Today iss thhhe last daa of SpringBreeeeeek"

match = re.findall(r"(((\w)\3)\2*)", s)
for t in match:
    print t[0]
#print "group 1 -> ", match.group(1)
#print "group 2 -> ", match.group(2)
