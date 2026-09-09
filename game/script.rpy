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

    e "You came back. I wasn't sure you would."
    e "The lights have been flickering for an hour, and the front door is unlocked."
    e "Before we pretend everything is normal, choose what we do with the note on the table."

    menu:
        "Read the note out loud.":
            jump listen

        "Follow the muddy footprints outside.":
            jump outside

        "Hide the note and lock the door.":
            jump stay


label listen:
    e "It says, 'You promised you would tell me before midnight.'"
    e "I don't remember making that promise. Do you?"

    menu:
        "Ask Eileen to write down everything she remembers.":
            jump ending_letter

        "Tell her the promise can wait until she feels safe.":
            jump ending_listener

        "Ask who she thinks left the note.":
            jump ending_honest


label outside:
    scene bg with dissolve
    show eileen at eileen_fit

    e "The footprints stop at the old greenhouse."
    e "There is a light moving behind the glass."

    menu:
        "Circle around and look for another entrance.":
            jump ending_walk

        "Call the person named in the note.":
            jump ending_call

        "Go back inside and wait for the light to disappear.":
            jump stay


label stay:
    show eileen at eileen_fit

    e "The lock clicks into place, but the light keeps flickering."
    e "If we stay, we need a plan before the next knock."

    menu:
        "Search the house for anything that explains the note.":
            jump ending_talk

        "Turn off every light and listen.":
            jump ending_book

        "Ask Eileen what she has been hiding from you.":
            jump ending_honest


label ending_letter:
    e "Eileen writes until the page is crowded with crossed-out names."
    e "At the bottom, she finds a sentence in her own handwriting: 'Do not open the greenhouse.'"
    return


label ending_listener:
    e "You sit beside her while the house settles around you."
    e "Then the knocking starts again, softer this time, from inside the room."
    return


label ending_honest:
    e "Eileen looks toward the locked hallway."
    e "'I heard the voice before,' she says. 'It sounded exactly like you.'"
    return


label ending_walk:
    e "Behind the greenhouse, you find a second set of footprints leading back to the house."
    e "They are fresh, and neither of you made them."
    return


label ending_call:
    e "The call connects without ringing."
    e "A voice whispers, 'You should not have brought Eileen home.'"
    return


label ending_talk:
    e "Behind a stack of old books, you find a photograph of this room."
    e "In the photograph, someone is standing behind Eileen."
    return


label ending_book:
    e "The house goes silent. Even the clock stops."
    e "In the dark, Eileen whispers, 'Whatever you hear, do not answer me.'"
    return