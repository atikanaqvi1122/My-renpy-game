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

    e "Hello, and welcome to my game."
    e "I've been waiting for someone to talk to."
    e "What should we do first?"

    menu:
        "Listen to Eileen's story.":
            jump listen

        "Go outside together.":
            jump outside

        "Stay in the room and make a plan.":
            jump stay


label listen:
    e "There is something I have been afraid to say out loud."
    e "I want tomorrow to feel different from today."

    menu:
        "Encourage her to write it down.":
            jump ending_letter

        "Promise to listen whenever she needs you.":
            jump ending_listener

        "Ask what she really wants.":
            jump ending_honest


label outside:
    scene bg with dissolve
    show eileen at eileen_fit

    e "It's freezing out here, but the air feels good."
    e "Which way should we go?"

    menu:
        "Take the quiet path.":
            jump ending_walk

        "Call someone we trust.":
            jump ending_call

        "Go back inside before it gets dark.":
            jump stay


label stay:
    show eileen at eileen_fit

    e "Much better. It's warm in here."
    e "We can still make tonight matter."

    menu:
        "Make tea and talk until midnight.":
            jump ending_talk

        "Read quietly side by side.":
            jump ending_book

        "Tell Eileen exactly how you feel.":
            jump ending_honest


label ending_letter:
    e "The words come slowly, but they are honest."
    e "By morning, the page feels like a door we can open."
    return


label ending_listener:
    e "You do not try to fix everything. You simply stay."
    e "For Eileen, that is enough to begin again."
    return


label ending_honest:
    e "That was the truth I needed to hear."
    e "We cannot promise an easy tomorrow, but we can face it together."
    return


label ending_walk:
    e "The quiet path leads nowhere special."
    e "Somehow, the walk still feels like a beginning."
    return


label ending_call:
    e "The phone rings once, then someone answers."
    e "The room feels less lonely after that."
    return


label ending_talk:
    e "By midnight, we have laughed at least once."
    e "That small moment becomes our favorite part of the day."
    return


label ending_book:
    e "The silence between us is comfortable now."
    e "When the last page turns, neither of us feels alone."
    return