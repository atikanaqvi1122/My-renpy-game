# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")

transform eileen_fit:
    zoom 0.55
    xalign 0.5
    yalign 1.0


# The game starts here.


label start:

    scene bg with dissolve
    show eileen at eileen_fit

    e "Hello, and welcome to my game!"
    e "I've been waiting for someone to talk to."


    menu:
        "Go outside.":
            jump outside

        "Stay in this room.":
            jump stay

label outside:
    scene bg with dissolve
    show eileen at eileen_fit

    e "It's freezing out here!"
    return

label stay:
    show eileen at eileen_fit

    e "Much better. It's warm in here."
    return

