# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:17:05 2022

@author: Aqeel Ahmed
"""

cube = -27
#cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
#cube = 0.25
epsilon = 0.01
num_guesses= 0

low = 0
high = cube


guess = (high + low)/2.0
while abs(guess**3-cube) >= epsilon:
    
    if cube>0:
        if guess**3 < cube:
            
            # look only in upper half search space
            low = guess
        else:
            # look only in lower half search space
            high = guess
        # next guess is halfway in search space
    else: # for Negative Values 
        if  guess**3 > cube:
            
            low=guess
        else:
            high=guess
        
    guess = (high + low)/2.0
    num_guesses+= 1
print('num_guesses =',num_guesses)
print(guess, 'is close to the cube root of', cube)