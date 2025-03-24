# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 11:46:24 2025

@author: veerk
"""
import random

number = random.randint(1,100) 
guess = 0

while guess != number:
    guess = int(input("Enter guess number :"))
    if (guess < number):
       print ("Guess higher !")
  
    elif(guess>number):
        print("guess Lower!")

else:
    print("you won")

    
  