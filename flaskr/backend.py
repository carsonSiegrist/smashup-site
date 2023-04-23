import json
import random


class Backend:


    def __init__(self):
        self.maxFactions = 95 #Only 95 unique factions exist

    
    def getAllFactions(self):
        with open("static/sets.json") as f: #sets here refers to Smash Up terminology, not data type
            setsDict = json.load(f)

        #Combine all values into one list
        values = list()
        for value in setsDict.values():
            values.extend(value)

        return values #keys represent the set the factions are from, values are factions themselves

    #Generates decksPerPlayer random decks per playerCount. (Total random decks = playerCount * decksPerPlayer)
    def allRandom(self, playerCount):
        decks = self.getAllFactions()
        random.seed() #Defaults to seeding with system time
        
        outDecks = []
        for player in range(playerCount):
            deck1 = random.choice(decks)
            decks.remove(deck1)
            deck2 = random.choice(decks)
            decks.remove(deck2)
            
            outDecks.append((deck1, deck2))
        
        return outDecks

        
