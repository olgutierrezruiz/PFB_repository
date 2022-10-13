#!/usr/bin/env python3
import sys
import math

#Problem Set 5

#Question 1
fav = {'songs':'speed of sound', 'bands':'keane','food':'tacos','shows':'LOR'}		#makes dictionary
print(fav)

#Question 2
print(fav['songs'])

#Question 3
fav_thing = 'shows'
print(fav[fav_thing])

#Question 4
print(fav['food'])

#Qestion 5
fav['organism']='bacteria'			#Adds a key and its value to a dictionary
fav_thing = 'organism'
print(fav[fav_thing])						#Prints the value of fav_thing inside the fav dictionary

#Question 6											
if 'songs' in fav:
	print(fav['songs'])

#Question 7
fav['organism']='fungi'

#Question 8

#Cab be done this way but it is not the way it is asking you to do it, because you need to know what fav_thing is 
user_input = input('Type favorite thing:')		#Asks the user for to input something and 																						 assigns it to the user_input variable	
fav['organism'] = user_input									#changes the value of organism for what t                                              he user input
print(fav[fav_thing])


#This is the actual way o do it
user_input = input('Type favorite thing:')	#Asks the user to input something and makes																							 it user_input	
fav[fav_thing] = user_input									#replaces the value of fav_thing in fav dic																						 tionary for user_input

#Question 9

for key in fav:										#This for loop will print key and its value
	print(key, "\t", fav[key])			#in dictionary separated by tab

