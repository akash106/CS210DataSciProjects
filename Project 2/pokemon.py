from cmath import nan
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
    typeToWeaknessDict = {}

    with open(file) as pokedex:
        csv_reader = csv.reader(pokedex, delimiter=',')
        
        for row in csv_reader:
            if row['type'] not in typeToWeaknessDict.keys() and row['weakness'] != nan:
                typeToWeaknessDict[row['type']] = []
                typeToWeaknessDict[row['type']].append(row['weakness'])
            elif row['weakness'] != nan:
                typeToWeaknessDict[row['type']].append(row['weakness'])
    
    with open(file, "w") as pokedex:
        csv_reader = csv.reader(pokedex, delimiter=',')
        for row in csv_reader:
            if row['weakness'] == nan:
                mostCommonWeakness = MostFrequentElement(typeToWeaknessDict[row['type']])
                row['weakness'] = mostCommonWeakness
    
    return



def missingVals():
    pass

def personalityDict():
    pass

def avgHitPoints():
    pass

def main():
    findPercentage("pokemonTrain.csv")
    #missingType("pokemonTrain.csv")
main()    
