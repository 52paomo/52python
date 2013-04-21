#!/usr/bin/python

## find all occurrences of sub-strings in the whole text 
## which consist of even number of same word characters

# ASSUMPTION: we're ONLY interested in matching alphanumeric characters and underscore
# TODO(halazi): how to match non-alphanumeric chars (e.g. space, line break)?

import re
from pprint import pprint

s = "Today iss thhhe last daa of SpringBreeeeeek"

# Steps to develop the regex matching pattern:
# 1. Match occurrences of sub-string which consists of exactly TWO copies of the same char.
#    e.g. 'aa', 'bb', but not 'aaaa', 'bbbb'.
#--> Pattern = r"((\w)\2)", why?
#    a.) outer parentheses correspond to group(1)
#    b.) inner parentheses correspond to group(2)
#    c.) '\w' matches any alphanumeric char, i.e. [a-zA-Z0-9_]
#    d.) '\2' means matches the content of the group of the same number.
#        In this case, '\w\w' where '\w' occurs TWICE consecutively
#
# 2. Match even number of the same char, i.e. repeated occurrences of pattern #1
#    e.g., 'aa', 'bb', 'aaaa', 'bbbb', but not 'aaa', 'bbb'
#--> Pattern = r"(((\w)\3)\2*)"
#    a.) we need one more level of nested parenthese, hence bumping '\2' to '\3'
#    b.) '((\w)\3)' is group(2). We're looking for repeated occurrences of group(2), e.g.
#        no/zero repeat ==> matches 'aa', 'bb'
#        one repeat     ==> matches 'aaaa', 'bbbb'
#        two repeats    ==> matches 'aaaaaa', 'bbbbbb'
match = re.findall(r"(((\w)\3)\2*)", s)
for t in match:
    # t = [group(1), group(2), group(3)], e.g. ['eeeeee', 'ee', 'e']
    # where '\w' matches 'e', '((\w)\3)' matches 'ee'
    pprint(t[0])
