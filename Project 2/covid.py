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
                        
def changeDate(file):
    
    with open(file, "r") as inp:
        reader = csv.DictReader(inp.readlines())
        

    with open("covidTrain.csv", 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:

            seprea = '.'

            symptomsList = re.split(r'[.]', row['date_onset_symptoms'])
            symptomsList[0], symptomsList[1] = symptomsList[1], symptomsList[0]
            row['date_onset_symptoms'] = seprea.join(symptomsList)

            hospitalList = re.split(r'[.]', row['date_admission_hospital'])
            hospitalList[0], hospitalList[1] = hospitalList[1], hospitalList[0]
            row['date_admission_hospital'] = seprea.join(hospitalList)
            #print(row['date_admission_hospital'])
            confirmList = re.split(r'[.]', row['date_confirmation'])
            confirmList[0], confirmList[1] = confirmList[1], confirmList[0]
            row['date_confirmation'] = seprea.join(confirmList)

            writer.writerow(row)
    
def missingLongLat ():
    pass


def MostFrequentElement(lis):
    return max(set(lis), key = lis.count)

def missingCity(file):

    provToCityDict = {}

    with open(file) as inp:
        reader = csv.DictReader(inp, delimiter= ',')
        for row in reader:
            if row['province'] not in provToCityDict.keys() and row['city'] != "NaN":
                provToCityDict[row['province']] = []
                provToCityDict[row['province']].append(row['city'])
            elif row['city'] != "NaN":
                provToCityDict[row['province']].append(row['city'])



    with open(file, "r") as inp:
        reader = csv.DictReader(inp.readlines())

    with open("covidTrain.csv", 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:
            if row['city'] == "NaN":
                frequentCity = MostFrequentElement(provToCityDict[row['province']])
                print(frequentCity)
                row['city'] = frequentCity
                #print(row['city'])
                writer.writerow(row)
            else:
                writer.writerow(row)
        

def missingSymptoms():
    pass
    

def main():
    #avgAge('covidTrain.csv')
    changeDate('covidTrain.csv')
    missingCity('covidTrain.csv')
main()
