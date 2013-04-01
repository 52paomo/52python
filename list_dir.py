#!/usr/bin/python

import os
import sys

def List(d):
    filenames = os.listdir(d)
    print filenames

def main():
    List(sys.argv[1])

if __name__ == "__main__":
    main()
