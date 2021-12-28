# You should use deez website to use code: https://www.reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json

#Square

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
turn_left()
move()
turn_left()
turn_around()
move()
turn_left()
turn_around()
move()
turn_left()
turn_around()
move()



#Jump

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#    for step in range(1, 5): jump() #Jump 5 times  ------x
#    Same but we using while loop now                     |
#                                                         V
########################################################################################
number_of_hurdles = 6                                                                  #
#                                                                                      #
while number_of_hurdles > 0: # If number of hurdles lower than 0, stop the loop        #
    jump()                                                                             #
    number_of_hurdles -= 1 #Every cycle in will substract 1 from nummber_of_hurdles    #
########################################################################################