import math
import collections
import csv
import re

# git add - A, commit -m"message", push (to add files to REPO)
# git pull (to get files from REPO)

def findPercentage (file):
    
    typeToLevelDict = {}

    # how to read from a CSV
    with open(file) as pokedex:
        reader = csv.DictReader(pokedex, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            if row['type'] not in typeToLevelDict.keys():
                typeToLevelDict[row['type']] = []
                typeToLevelDict[row['type']].append(row['level'])
            else:
                typeToLevelDict[row['type']].append(row['level'])

    
    print(typeToLevelDict.items())
    countOfFirePokemon = len([i for i in typeToLevelDict["fire"]])

    countOfFirePokemon40 = len([i for i in typeToLevelDict["fire"] if float(i) > 40])

    percentage = (countOfFirePokemon40/countOfFirePokemon) * 100

    accurate_percentage = round(percentage)
    with open("pokemon1.txt", "w") as f:
        f.write(f"Percentage of fire type pokemon over level 40 is {accurate_percentage}")


def MostFrequentElement(lis):
    return max(set(lis), key = lis.count)
     
def missingType(file):
    WeaknessToTypeDict = {}

    with open(file) as pokedex:
        csv_reader = csv.DictReader(pokedex, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row['weakness'] not in WeaknessToTypeDict.keys() and row['type'] != "NaN":
                WeaknessToTypeDict[row['weakness']] = []
                WeaknessToTypeDict[row['weakness']].append(row['type'])
            elif row['type'] != "NaN":
                WeaknessToTypeDict[row['weakness']].append(row['type'])
        
    print(WeaknessToTypeDict)
    
    with open(file, 'r+') as out:
        csv_reader = csv.DictReader(out, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row['type'] == "NaN":
                print(row['weakness'])
                MostCommonElement = MostFrequentElement(WeaknessToTypeDict[row['weakness']])
                print(MostCommonElement)
                row['type'].replace("NaN", MostCommonElement)
    #need to figure out how to replace value in csv


def missingVals():
    pass

def personalityDict(file):
    typeToPersonality = {}
    with open(file, "r") as pokedex:
        csv_reader = csv.DictReader(pokedex, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row['type'] not in typeToPersonality.keys():
                typeToPersonality[row['type']] = []
                typeToPersonality[row['type']].append(row['personality'])
            else:
                typeToPersonality[row['type']].append(row['personality'])
        
    del typeToPersonality['NaN']
    sorted_dict = {}
    for key in sorted(typeToPersonality):
        sorted_dict[key] = sorted(typeToPersonality[key]) 
    
    with open("pokemon4.txt", "w") as output:
        output.write("Pokemon type to personality mapping:\n")
        for key in sorted_dict.keys():
            output.write(f"{key} : {sorted_dict[key]} \n")
    
    
    

def avgHitPoints(file):
    HitPoints = []

    with open(file, "r") as pokedex:
        csv_reader = csv.DictReader(pokedex, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row['stage'] == '3.0' and not math.isnan(float(row['hp'])):
                HitPoints.append(float(row['hp']))
    print(HitPoints)
    averageHP = sum(HitPoints) / len(HitPoints)
    print(averageHP)

    with open("pokemon5.txt", "w") as output:
        output.write(f"Average hit point for pokemon of stage 3.0 = {round(averageHP)}")





def main():
    #findPercentage("pokemonTrain.csv")
    missingType("pokemonTrain.csv")
    personalityDict("pokemonTrain.csv")
    #avgHitPoints("pokemonTrain.csv")
main()    
