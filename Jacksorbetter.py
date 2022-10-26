from asyncio.windows_events import NULL
from hashlib import new
import random, itertools, functools,re
from tabnanny import check
from time import sleep
from unittest.loader import VALID_MODULE_NAME
from winreg import EnableReflectionKey

class Intro:
    def introduction(self):
        print("***JACKS OR BETTER***")
        sleep(0.75)

class Bank:
    def getBank(self):
        userBank = input("Enter your bankroll: ")
        return userBank

class Cards:
    def deck(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        deck = [(value, card) for card in self.suits for value in self.value]
        return deck

    def shuffle(self):
        newDeck = Cards.deck(self)
        random.shuffle(newDeck)
        return newDeck

class Dealing:
    def initialDeal(self,deck):
        cardsShown = [];dealIter = 0;x = 0
        while dealIter < 5:
            cardsShown.append(deck[x])
            deck.remove(deck[x])
            dealIter += 1
            x += 1
        return cardsShown,deck

class Interface:
    def output(self,table):
        firstCard = table[0][0]
        secondCard = table[0][1]
        thirdCard = table[0][2]
        fourthCard = table[0][3]
        fifthCard = table[0][4]
        hand = [firstCard,secondCard,thirdCard,fourthCard,fifthCard]
        return hand   

class Keepcard:
    def holding(self,hand,shuffleDeck):
        card = [];x = 0
        keep = input("[Y]es or [N]o ").upper()
        if(keep == "Y"):
            card.append(hand)
        else:
            card.append(shuffleDeck[x])
            shuffleDeck.remove(shuffleDeck[x])
            x += 1
        return card           

class Ranks:
    def suitsRanks(self,userHeld):
        ranks = [];suits = [];x = 0;y = 0
        while(x < 5):
            ranks.append(userHeld[x][0][0])
            x += 1
            while(y < 5):
                suits.append(userHeld[y][0][1])  
                y += 1
        return ranks,suits
           
    def match(self,userHeld):
        rankSuit = Ranks().suitsRanks(userHeld)
        x =0;y = 1;b = 0;match = [];suits = []
        #print(rankSuit[1][x])
        while(y < 5):
            if(rankSuit[0][x] == rankSuit[0][y]):
                match.append(rankSuit[0][x]);match.append(rankSuit[0][y])
                y += 1
                if(y == 5):
                    x += 1
                    y = x + 1
            elif(rankSuit[0][x] != rankSuit[0][y]):
                y += 1
                if(y == 5):
                    x += 1
                    y = x + 1
        num = int(len(match))
        
        return num
    
    def faceConversion(self,userHeld):
        x = 0;y = 0;newFaces = []
        suits = Ranks().suitsRanks(userHeld)
        for n in suits[0]:
            if(n == "Jack"):
                n = 11
                newFaces.append(n)
            elif(n == "Queen"):
                n = 12
                newFaces.append(n)
            elif(n == "King"):
                n = 13
                newFaces.append(n)
            elif(n == "Ace"):
                n = 14
                newFaces.append(n)
            else:
                newFaces.append(n)
        return newFaces

    def checkStraight(self,checkStr):
        rankList = []
        for n in checkStr:
                rankList.append(int(n))
        return sorted(rankList) == list(range(min(rankList), max(rankList)+1))
    
    def checkFlush(self,userHeld):
        x = 0;y = 0;suit = []
        while(x < 5):
            suit.append(userHeld[x][0][1])
            x += 1
        return suit
        
        
    def pairs(self,length):
        if(length == 12):
            b = 5
        elif(length == 8):
            b = 4
        elif(length == 6):
            b = 3
        elif(length == 4):
            b = 2
        else:
            b = 0
        return b

    def jacksBetter(self,userHeld):
        rankSuit = Ranks().suitsRanks(userHeld) 
        x = 0;j = 0;q = 0;k = 0;a = 0;b = 0
        while(x < 5):
            if(rankSuit[0][x] == "Jack"):
                j +=1
                if(j == 2):
                    print("Jacks or better!")
                    b += 1
                    return b    

            elif(userHeld[x][0][0] == "Queen"):
                q +=1
                if(q == 2):
                    print("Jacks or better!")
                    b += 1
                    return b

            elif(userHeld[x][0][0] == "King"):
                k +=1
                if(k == 2):
                    print("Jacks or better!")
                    b += 1
                    return b 

            elif(userHeld[x][0][0] == "Ace"):
                a +=1
                if(a == 2):
                    print("Jacks or better!")
                    b += 1
                    return b
            x += 1    

class Bankupdated:
    def result(self,userBank,userHeld,value):
        rankList = []
        if(value == 1):
            userBank += 5
        elif(value == 2):
            print("Two Pair!")
            userBank += 10
        elif(value == 3):
            print("Three of a kind!")
            userBank += 15
        elif(value == 4):
            print("Full House!")
            userBank += 45
        elif(value == 5):
            print("Four of a kind!")
            userBank += 125
        else:
            checkStr = Ranks().faceConversion(userHeld)
            straight = Ranks().checkStraight(checkStr)
            if(straight == True):
                suit = Ranks().checkFlush(userHeld)
                if(all(val == suit[0] for val in suit)):
                    if(min(straight) == 10):
                        print("Royal Flush!")
                        userBank += 4000
                    else:
                        print("Straight Flush!")
                        userBank += 250
                else:
                    print("Straight!")
                    userBank += 20
            
            elif(straight == False):
                suit = Ranks().checkFlush(userHeld)
                if(all(val == suit[0] for val in suit)):
                    print("Flush!")
                else:
                    userBank == userBank
        return userBank    

class Main:
    def mainFunction(self):
        Intro().introduction()
        userBank = int(Bank().getBank())
        while(userBank > 0):
            userHeld = []
            x = 0
            userBank -= 5
            shuffleDeck = Cards().shuffle()
            table = Dealing().initialDeal(shuffleDeck)          #Outputs the original 5 card hand
            updatedDeck = table[1]
            print("*****YOUR HAND*****")
            hand = Interface().output(table)
            print(hand,"\nSelect cards to hold:")
            while(x < 5):                                       #Loop to choose which cards to hold/not hold
                held = Keepcard().holding(hand[x],shuffleDeck)
                userHeld.append(held)
                x += 1
            
            print(userHeld)
            length = Ranks().match(userHeld)
            value = Ranks().pairs(length)
            Ranks().faceConversion(userHeld)
            if(value == 0):
                value = Ranks().jacksBetter(userHeld)
            userBank = Bankupdated().result(userBank,userHeld,value)
            print("$",userBank,"\n")
              
Main().mainFunction()