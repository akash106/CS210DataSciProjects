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

    str1 = re.sub(r'http://\S+ | https://\S+', '', str1)
    str1 = re.sub("[\W]{1,}",' ',str1) 
    str1 = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', str1)
    str1 = str1.lower()


    # get rid of stopword
    stopList = []
    stopWords = open('stopwords.txt')
    for line in stopWords:
        stopList.append(line.strip())
    

    for stopWord in stopList:
        str1 = re.sub(r'\b'+ stopWord + r'\b\s+', '', str1)

    suffixList = ['ly', 'ing', 'ment']

    for suffix in suffixList:
        str1 = re.sub(suffix + r'\b', '', str1)

    

    
       
    print(str1)
    

    #bruh i give up idk how to do regex
    
    # remove all words that are not white space




def calcTFIDF():
    pass

def main():
    
    preproc('test1.txt')



main()

