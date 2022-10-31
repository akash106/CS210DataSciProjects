import math
import collections
import csv
import re

# all contributors
#zc285
#ass209
#kap401
#arb295

def avgAge (file):

    with open(file, "r") as inp:
        reader = csv.DictReader(inp.readlines())
        

    with open("covidResult.csv", 'w') as out:
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
        

    with open("covidResult.csv", 'w') as out:
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
    
def missingLongLat (file):
    latitude = {}
    longitude = {}
    with open(file) as covidData:
        reader = csv.DictReader(covidData, delimiter=',')
        next(reader)
        for row in reader:
            if row['province'] not in latitude.keys() and row['latitude'] != "NaN":
                latitude[row['province']] = []
                latitude[row['province']].append(float(row['latitude']))
            elif row['latitude'] != "NaN":
                latitude[row['province']].append(float(row['latitude']))
            if row['province'] not in longitude.keys() and row['longitude'] != "NaN":
                longitude[row['province']] = []
                longitude[row['province']].append(float(row['longitude']))
            elif row['longitude'] != "NaN":
                longitude[row['province']].append(float(row['longitude']))
        covidData.close()
        #now just have to write it to a file

    for i in latitude.keys():
        latitude[i] = round((sum(latitude[i]) / len(latitude[i])), 2)
        print(latitude[i])
    
    for i in longitude.keys():
        longitude[i] = round((sum(longitude[i]) / len(longitude[i])), 2)
        print(longitude[i])
        
        
    

    with open(file, "r") as inp:
        reader = csv.DictReader(inp.readlines())

    with open('covidResult.csv', 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:
            
            if row['latitude'] == "NaN":
                
                row['latitude'] = latitude[row['province']]

            if row['longitude'] == "NaN":
                 row['longitude'] = longitude[row['province']]

            writer.writerow(row)   
        covidData.close()    


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

    with open("covidResult.csv", 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:
            if row['city'] == "NaN":
                frequentCity = MostFrequentElement(provToCityDict[row['province']])
                row['city'] = frequentCity
                #print(row['city'])
                writer.writerow(row)
            else:
                writer.writerow(row)
        

def missingSymptoms(file):
    
    provToSympDict = {}

    with open(file) as inp:
        reader = csv.DictReader(inp, delimiter= ',')
        for row in reader:
            if row['province'] not in provToSympDict.keys() and row['symptoms'] != "NaN":
                provToSympDict[row['province']] = []
                if re.search(';', row['symptoms']):
                    symptomsList = re.split(r'; |;', row['symptoms'])
                    for i in symptomsList:
                        provToSympDict[row['province']].append(i)
                else:
                    provToSympDict[row['province']].append(row['symptoms'])
            elif row['symptoms'] != "NaN":
                if re.search(';', row['symptoms']):
                    symptomsList = re.split(r'; |;', row['symptoms'])
                    for i in symptomsList:
                        provToSympDict[row['province']].append(i)
                else:
                    provToSympDict[row['province']].append(row['symptoms'])

    with open(file, "r") as inp:
        reader = csv.DictReader(inp.readlines())

    with open("covidResult.csv", 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:
            if row['symptoms'] == "NaN":
                frequentSymptom = MostFrequentElement(provToSympDict[row['province']])
                row['symptoms'] = frequentSymptom
                #print(row['city'])
                writer.writerow(row)
            else:
                writer.writerow(row)


def main():
    avgAge('covidTrain.csv')
    changeDate('covidResult.csv')
    missingCity('covidResult.csv')
    missingSymptoms('covidResult.csv')
    missingLongLat('covidResult.csv')
main()
