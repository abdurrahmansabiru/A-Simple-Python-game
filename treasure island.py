#Simple game of treasure island
print('WELCOME TO SCARY TREASURE ISLAND')

print('Your mission is to find the hidden treasure on the island')

name = input('Enter your name').lower()
#Choices to start the game
choice=input('Choose your path: right, left  ').lower()

if choice == 'right':
    print('You arrived to a very big lake')
#Ways to cross the river
    method = input('Choose of these to cross the river: boat, plane, ship ')
    if method=='boat':
	    print('Good choice but the boat sank at the middle of the lake')
	
    elif method=='plane':
         print('The fuel of plane finished at the  middle of the lake')
    elif method=='ship':
         print('You arrived to a house with three doors')
	 
    else:
    	print('INVALID INPUT')
    	#Doors to the treasure
    doors = input('Choose one of the three doors: red , blue , gold ').lower()
    
    if doors == 'red':
    	print('You open the door of hazard and it turns you into ash.')
    elif doors=='blue':
    	print('You open the door of an ocean and you die in it.')
    elif doors=='gold':
    	print('Here is your treasure. Hope you enjoy the game. Thank you')
    else:
    	print('Invalid input')
	
elif choice=='left':
	print('You choose the path of a lion and only  your bones remain')


else:
	print('Invalid input')