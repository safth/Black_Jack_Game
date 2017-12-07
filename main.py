#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:45:58 2017
BLACKJACK
@author: simonboivin
"""


"""
- You need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- You need to keep track of the players total money.
- You need to alert the player of wins, losses, or busts, etc..
"""
#clear all
#import sys
#sys.modules.clear()

from classes import Player 
from classes import Deck





def Player_turn():
    #get bet
    player.Get_bet_ammount()
    #Give the player 2 Cards
    player.hand.append(deck.hit())
    player.hand.append(deck.hit())
    print "your cards:    %s = %s" % (player.hand, player.Get_score())
    #give the dealer 1 card.
    dealer.hand.append(deck.hit())
    print "Dealers cards: %s = %s" % (dealer.hand, dealer.Get_score()) 
    # si il fait un black jack!
    if player.Get_score() == 21: 
        print "your cards:    %s = %s" % (player.hand, player.Get_score())
        dealer.hand.append(deck.hit()) # le dealer en prend une autre
        print "Dealers cards: %s = %s" % (dealer.hand, dealer.Get_score()) 
        check_winner()        
        
    else:#si il n'a pas un blackjack
        #tout les tours subséquents son loop ici
        while True:
            rep = Hit_or_Stand()
            if rep == 'H':
                player.hand.append(deck.hit())
            else:
                break
            print "your cards:    %s = %s" % (player.hand, player.Get_score())
            print "Dealers cards: %s = %s" % (dealer.hand, dealer.Get_score()) 
            #check if player exceed 21
            if check_21():#check the winner and give the money
                break #break #ronde terminé!
                    
def Dealer_turn():
    if player.win == False: # le dealer ne joue pas si le joueur a deja perdu en excedant 21
        while dealer.Get_score() < 17:
            dealer.hand.append(deck.hit())
            print "Dealers cards: %s = %s" % (dealer.hand, dealer.Get_score()) 
            #check if dealer exceed 21
            if check_21():#check the winner and give the money
                break #break #ronde terminé!
        #on regarde qui gagne si le dealer n'a pas excd 21       
        if not player.win:
            check_winner()
            
                    
                        
                    

     
def Hit_or_Stand():
    while True:
        val = raw_input("do you want to Hit or Stand?? (H/S)").upper()
        if val == "H" or val == "S":
            return val
            break         
        else:
            print "insert a valid choice!"
            

def replay():  
    print "you have %s $" % player.cash  
    choice=''
    while not (choice=='y' or choice=='n'):
        choice = raw_input('wanna play again? (y/n)').lower()
    if choice=='y':
        return True
    if choice=='n':
        return False
    
#check who win and tell the object who receive cash5
def check_winner():
    if dealer.Get_score() > 21:
        print "Player win!!!"      
        player.add_cash(True)
        return True 
    elif player.Get_score() > 21:
        print "Dealer win!!!"      
        player.add_cash(False)
        return True                     
    elif dealer.Get_score() < player.Get_score() and player.Get_score() <= 21:
       print "player win" 
       player.add_cash(True)
       return True
    elif dealer.Get_score() > player.Get_score(): 
       print "Dealer win"      
       player.add_cash(False)
       return True
    elif dealer.Get_score() == player.Get_score():
        print "it's a tie"
        return True
    else:
        return False
    
def check_21():
    if dealer.Get_score() > 21:
        print "Player win!!!"      
        player.add_cash(True)
        player.win==True    
        return True 
    elif player.Get_score() > 21:
        print "Dealer win!!!"      
        player.add_cash(False)
        player.win==True
        return True                  
    
def reset():
   deck.reset()
   player.win = False
   player.hand=[]
   dealer.hand=[]
"""
##############################    
##############################
###  on commence la game   ###       
##############################    
##############################        
"""          
player = Player(cash = 1000)
dealer = Player(cash = 0)
deck = Deck()

while True: # tout le temps de la game
    reset()
    Player_turn()
    Dealer_turn()
    if not replay():
        print " FIN "
        print " tu repars avec la somme de %s $$$" % player.cash
        break







 
    