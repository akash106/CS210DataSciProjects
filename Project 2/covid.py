import math
import collections
import csv
import re


def avgAge (file):


    # open the write file
   

    # open the read file (which will be the same as the write file)


    with open(file, "r") as inp:
        reader = csv.DictReader(inp.readlines())
        

    with open("covidTrain.csv", 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:
                if re.search('-', row['age']):
                    match = re.split(r"\D", row['age'])
                    sum = 0
                    length = len(range(int(match[0]), int(match[1])))
                    if length > 0:
                        for i in range(int(match[0]), int(match[1])):
                            sum += i
                        avg = round(sum/length)
                        row['age'] = str(avg)
                        writer.writerow(row)
                        #print(row['age'])
                    else:
                        #print(row['age'])
                        row['age'] = str(match[0])
                        writer.writerow(row)
                else:
                    writer.writerow(row)
                        
     
    
    

def main():
    avgAge('covidTrain.csv')
main()
