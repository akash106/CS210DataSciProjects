import math
import collections
import csv
import re


def preproc(file):

    # compile regex

    
    # open file
    preprocFile = open(file)
    str1 = preprocFile.readline()
    print(str1)  

    str1 = re.sub('http', '', str1)
    str1 = re.sub("[\W]{1,}",' ',str1) 
    str1 = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', str1)
    
    print(str1)
    
   

    

    #bruh i give up idk how to do regex
    
    # remove all words that are not white space




def calcTFIDF():
    pass

def main():
    
    preproc('test1.txt')



main()

