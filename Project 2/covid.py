import math
import collections
import csv
import re


def avgAge (file):


    # open the write file
    

    # open the read file (which will be the same as the write file)

        with open(file) as covidResults1:
            reader = csv.DictReader(covidResults1)
            for row in reader:
                
                if re.search('-', row['age']):
                    match = re.split(r"\D", row['age'])
                    sum = 0
                    length = len(range(int(match[0]), int(match[1])))
                    if length > 0:
                        for i in range(int(match[0]), int(match[1])):
                            sum += i
                        avg = round(sum/length)
                        row['age'].replace(row['age'], str(avg))
                        print(avg)
                    else:
                        row['age'].replace(row['age'], str(match[0]))
                        print(match[0])
                else:
                    print(row['age'])
                        
                
    #struggling to update the vals in the CSV not sure why but everytime I write the file it clears the CSV lmao                   


    # iterate through the rows checking the age
        # use regex .split() and then set those two values as start and end
        # iterate through that range and find the sum of those values
        # get out of that loop and repalce the age range with the avg
    
    

def main():
    avgAge('covidTrain.csv')
main()
