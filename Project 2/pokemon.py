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
           for typeOf, level in row.items():
                if typeOf not in typeToLevelDict.keys():
                    typeToLevelDict[typeOf] = [];
                    typeToLevelDict[typeOf].append(level)
                else:
                    typeToLevelDict[typeOf].append(level)

    countOfFirePokemon = len([i for i in typeToLevelDict['type'] if i == 'fire'])

    countOfFirePokemon40 = len([i for i in typeToLevelDict['level'] if float(i) > 40 and typeToLevelDict['type'] == 'fire'])

    print(countOfFirePokemon40)  
    #countOfFirePokemon40 = len([i for i in typeToLevelDict['level'] and typeToLevelDict['type'] if i == 'fire' and i > 40])         

    

        
    

            
    
    

    
    pass
    # create a dict of type to level then while going through the dict count the number of fire type of pokemon and the ones above 40
    

def missingType():
    pass

def missingVals():
    pass

def personalityDict():
    pass

def avgHitPoints():
    pass

def main():
    findPercentage("pokemonTrain.csv")
main()    
