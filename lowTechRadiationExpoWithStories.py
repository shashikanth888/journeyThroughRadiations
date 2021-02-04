# -*- coding: utf-8 -*-

# code has been tested on macOS Mojave 10.14.6 (18G95), MacBook Air (13-inch, 2017)
# However the changes to port to other OS's such as Windows will be *minor* (only 2 unavoidably operating system dependent 
# function calls to clear screen and input buffer have to be changed).

# the indentations and formatting of the text has to be (currently) manually modified according to different screens. 

# So, if you press Enter 1 too many times, the program will assume the Enter was meant for the next question and won't give you a chance to answer the next question again. 

from __future__ import print_function, unicode_literals
import sys, termios # for flushing input buffers. For MAC OS. 
import pygame  # Load the popular external library
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from examples import custom_style_3
from ascii_graph import Pyasciigraph
import os # to clean screen in linux, mac
import time


#---------------------------------------------------------------- initiliazations ---------------------------------------------------------------------------------
def shiftAsciiToRight(asciiArt, noSpaces):
    """
    Receives ascii art as string. 
    Right shifts each line of ascii art by noSpaces
    Returns right shifted ascii art
    """
    ret = ""
    asciiArt = asciiArt.rstrip('\n')
    for line in asciiArt.split('\n'):
        ret += " " * noSpaces
        ret += line
        ret += "\n"
    ret = ret.rstrip('\n') # to get rid of the extra new line in the end
    return ret


os.system("clear") #use this for linux
#os.system("cls") #use this for windows

# initialize directories
asciiArtDir = "asciiArt/"
audioDir = "audio/"

# begin playing music 2 seconds after begin presenting
time.sleep(2)
pygame.mixer.init()
pygame.mixer.music.load(audioDir + "matrixIntro.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)

# do not show game introduction until first 25 seconds of music has passed. 
# time.sleep(25)


fixedIntro = """
                                               Welcome traveler, to Journey Through the Radiations!

                                               Explore different cities, and enjoy new experiences. 

                                                                    But beware! 
                                        Every decision you make inflicts on you various level of radiation. 

                                                          Have fun. Hope you survive. :)
"""
fixedIntro += "\n" + "-"*127 + "\n\n"
print (fixedIntro)

inp = input() # Will have to press any character to begin game
fixedIntro = """
                                                    Journey Through the Radiations!
"""
fixedIntro += "\n" + "-"*127 + "\n\n"



#---------------------------------------------------------------- question 1  ---------------------------------------------------------------------------------
os.system("clear")
print (fixedIntro)
questions1 = [

    {
        'type': 'list',
        'name': 'province',
        'qmark': '¯\_(ツ)_/¯',
        'message': 'Which city you want to work in?',
        'choices': ['Vancouver', 'Toronto', 'Montreal', 'Victoria', 'Ottawa', 'Fredericton', 'Charlottetown', 'Whitehorse', 'Edmonton' , 'Halifax'],
        'filter': lambda val: val.lower()
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers1 = prompt(questions1, style=custom_style_3)

# For the protype storyline, regardless of answer given, we will assume it was Montreal. Similarly with other questions. 
with open(asciiArtDir + "quebecFlag.txt", "r") as f:
	quebecFlag = f.read()
print (shiftAsciiToRight(quebecFlag, 12))
time.sleep(3)


#---------------------------------------------------------------- question 2  ---------------------------------------------------------------------------------
os.system('clear');
print (fixedIntro)
questions2 = [

    {
        'type': 'list',
        'name': 'job',
        'message': 'Bienvenue au Quebec! :) What do you want to work as?',
        'choices': ['Dentist', 'Pilot', 'Farmer', 'Astronaut'],
        'filter': lambda val: val.lower()
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers2 = prompt(questions2, style=custom_style_3)

with open(asciiArtDir + "dentist.txt", "r") as f:
	dentist = f.read()
print (shiftAsciiToRight(dentist, 12))
time.sleep(3)

#---------------------------------------------------------------- question 3  ---------------------------------------------------------------------------------
os.system('clear');
print (fixedIntro)
questions3 = [
    {
        'type': 'list',
        'message': "    Month 1:    Hello Doctor! Let's find you a hobby?",
        'name': 'activities',
        'choices': [
            {
                'name': 'Learn how to cook'
            },
            {
                'name': 'Start smoking'
            },
            {
                'name': 'Read novels'
            }
        ]
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers3 = prompt(questions3, style=custom_style_3)

with open(asciiArtDir + "chef.txt", "r") as f:
	chef = f.read()
print (shiftAsciiToRight(chef, 12))
time.sleep(3)

#---------------------------------------------------------------- question 4  ---------------------------------------------------------------------------------
os.system('clear');
print (fixedIntro)
questions4 = [
    {
        'type': 'list',
        'message': """      Month 3:    Good News! You've been offered a position in Bécancour. Would you like to take it?""",
        'name': 'activities',
        'choices': [
            {
                'name': 'Yes'
            },
            {
                'name': 'No'
            }
        ]
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers4 = prompt(questions4, style=custom_style_3)

with open(asciiArtDir + "fireworks.txt", "r") as f:
	fireworks = f.read()
with open(asciiArtDir + "runningManWithSuitcase.txt", "r") as f:
	runningManWithSuitcase = f.read()
print (shiftAsciiToRight(fireworks, 12))
print ("\n\n")
print (shiftAsciiToRight(runningManWithSuitcase, 12))

time.sleep(3)

#---------------------------------------------------------------- question 5  ---------------------------------------------------------------------------------
os.system('clear');
print (fixedIntro)
questions5 = [
    {
        'type': 'list',
        'message': """ Month 5: You just learned that a colleague has cancer due to prolonged exposure to radioactivity near your village. What do you want to do?
                """,
        'name': 'activities',
        'choices': [
            {
                'name': 'Pack up and leave the city immediately'
            },
            {
                'name': 'Speak to the ones in charge about a graded approach to solving radioactivity issues'
            },
            {
                'name': "Do nothing"
            }
        ]
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers5 = prompt(questions5, style=custom_style_3)

with open(asciiArtDir + "runningManFromBiohazard.txt", "r") as f:
	runningManFromBiohazard = f.read()
print (shiftAsciiToRight(runningManFromBiohazard, 12))

time.sleep(4.2)

#---------------------------------------------------------------- question 6  ---------------------------------------------------------------------------------
os.system('clear');
print (fixedIntro)
questions6 = [
    {
        'type': 'list',
        'message': """      Month 7:    You probably won't find a job for a few months. What will you do with the extra time?""",
        'name': 'activities',
        'choices': [
            {
                'name': 'Learn how to play an instrument'
            },
            {
                'name': 'Watch television for hours'
            },
            {
                'name': 'Search for a new job'
            }
        ]
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers6 = prompt(questions6, style=custom_style_3)

with open(asciiArtDir + "watchTvInBed.txt", "r") as f:
	watchTvInBed = f.read()
print (shiftAsciiToRight(watchTvInBed, 12))
time.sleep(4)

#---------------------------------------------------------------- question 7  ---------------------------------------------------------------------------------
os.system('clear');
print (fixedIntro)
questions7 = [
    {
        'type': 'list',
        'message': """      Month 9:    After 2 months of in front of a TV, what would you like to do?""",
        'name': 'activities',
        'choices': [
            {
                'name': 'Switch careers'
            },
            {
                'name': 'Switch cities'
            },
            {
                'name': 'Continue to watch TV'
            }
        ]
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers7 = prompt(questions7, style=custom_style_3)


#---------------------------------------------------------------- question 8 assuming want to choose new career -------------------------------------------------------------------------------
os.system('clear');
print (fixedIntro)

questions2 = [

    {
        'type': 'list',
        'name': 'job',
        'message': 'What do you want to work as now?',
        'choices': ['Dentist', 'Pilot', 'Farmer', 'Astronaut'],
        'filter': lambda val: val.lower()
    }
]
termios.tcflush(sys.stdin, termios.TCIOFLUSH)
answers2 = prompt(questions2, style=custom_style_3)

with open(asciiArtDir + "farm.txt", "r") as f:
	farm = f.read()
print (shiftAsciiToRight(farm, 12))
time.sleep(3)

os.system('clear');
print (fixedIntro)
print("""
        Month 12:
        Good news! Turns out farming doesn't expose you to as much radiation as being a dentist. 
        
        It's been an interesting year. Let's see how your body has fared.
        
        Press Enter to Continue.
    """)

inp = input()


#---------------------------------------------------------------- informative stats  ---------------------------------------------------------------------------------
while (True):
    #print('\n\n')
    os.system('clear');
    print (fixedIntro)
    
    provRads = [('Montreal', 1.6), ("St John's", 1.6), ('Victoria', 1.8), ('Toronto', 1.8), ('Frederiction', 1.8), ('Charlottetown', 1.8),
            ('Whitehorse', 1.9),
            ('Iqaluit', 1.9), ('Edmonton', 2.4), ('Halifax', 2.5), ('Yellowknife', 3.1), ('Regina', 3.5), ('Winnipeg', 4.1)
            ]
    provRadsBar = Pyasciigraph(float_format='{:,.5f}')
    for line in provRadsBar.graph('Background radiations of every province', provRads):
        print(line)
    print('\n\n')

    # show plot for relative radiations of each activity
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    inp = input()
    actRads = [('Eating banana / red meat / carrots', 0.1825), ('Sleeping next to someone', 5e-05),
               ('Watch TV', 1.000000e-02),
               ('Smoking cigarettes', 13), ('Using natural gas at home', 9e-02),
               ('Using soaps / shampoos / other consumer products', 11)
               ]
    actRadsBar = Pyasciigraph(float_format='{:,.5f}')
    for line in actRadsBar.graph('Radiations exposure from every activity', actRads):
        print(line)

    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    inp = input()
    os.system('clear');
    print (fixedIntro)

    print("""
        The following is the result of your journey.
    """)

    # show plot for total radiations you have accumulated compared to increasing risk of cancer
    totalRadSuffered = [("You've suffered", 17.882), ("Increased risk of cancer", 100)]
    totalRadSufferedBar = Pyasciigraph(float_format='{:,.2f}')
    for line in totalRadSufferedBar.graph('Do you have health? How much did you suffer? (in mSv)', totalRadSuffered):
        print(line)

    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    inp = input()
    print ("\n\n")
    print ("                                Would you like to see these again? (y/n)")

    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    choice = input()
    if choice == "n":
        break
    else:
        continue


#---------------------------------------------------------------- end  ---------------------------------------------------------------------------------
with open(asciiArtDir + "thankYou.txt", "r") as f:
	thankYou = f.read()
print (shiftAsciiToRight(thankYou, 12))
pygame.mixer.music.fadeout(100000);



