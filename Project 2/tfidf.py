import math
import collections
import csv
import re


def preproc(file):

    # compile regex

    
    # open file
    preprocFile = open(file)
    str1 = preprocFile.readline()
    #print(str1)  

    str1 = re.sub('/\s\s+/g,', '', str1)    
    str1 = re.sub(r'[^a-zA-Z_0-9 ]', '', str1)
    
   

    print(str1)

    #bruh i give up idk how to do regex
    
    # remove all words that are not white space




def calcTFIDF():
    pass

def main():
    
    preproc('test1.txt')



main()

