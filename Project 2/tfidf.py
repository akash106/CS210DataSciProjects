import math
import collections
import csv
import re


def preproc(file):

    # open file
    preprocFile = open(file)
    preprocFileW = open('preproc.txt', 'w')
    for line in preprocFile:

        str1 = line  
    
    # clean up the string

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

    # remove suffixes which have ly, ing, ment        

        suffixList = ['ly', 'ing', 'ment']

        for suffix in suffixList:
            str1 = re.sub(suffix + r'\b', '', str1)

        preprocFileW.write(str1)
    
 
def calcTFIDF():
    pass

def main():
    
    with open('tfidf_docs.txt') as docs:
        for line in docs:
            preproc(line.strip())


main()

