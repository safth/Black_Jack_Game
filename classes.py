#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 07:32:51 2017

@author: simonboivin
"""

#classe: le joureur, 
class Player(object):

    
    #initialisation des variables!
    def __init__(self,cash):
        self.cash = cash
        self.hand = []
        self.score = 0
        self.bet_amount = 0 
        self.win = False #True si quelquun a gagné
    def add_cash(self,win):
        if win == True:
            self.cash += 2*self.bet_amount
        else:
            self.cash -= self.bet_amount
        self.bet_amount = 0
        
    def Get_score(self):
        self.score = sum(self.hand)
        if self.score > 21 and self.hand.count(11) != 0 : 
            index = self.hand.index(11)
            self.hand[index] =1
            self.score = sum(self.hand)
        return self.score
        
        
    # ask the amount the player want to bet
    #put it in bet_amount
    #reset get_bet to Fales
    def Get_bet_ammount(self):
        while True:
            try:
                val = int(raw_input("you have %s $ left, how do you want to bet? :"  % self.cash))
                break
            except:
                print "invalid number, put a integer"
        self.bet_amount = val
        self.get_bet = False
        
   
# faire un deck de 52 cartes, et le shuffle
class Deck(object):
    def __init__(self):
        import random
        self.cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] * 4
        random.shuffle(self.cards)
        
    #distribut 1 cartes de manieres aléatoire.
    def hit(self):
        return self.cards.pop()
    #reset le deck
    def reset(self):
        import random
        self.cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] * 4
        random.shuffle(self.cards)
       