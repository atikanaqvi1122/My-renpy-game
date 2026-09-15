# The script of the game goes in this file.

# ----------------------------------------------------------------------
# CHARACTERS
# ----------------------------------------------------------------------
define e = Character("Eileen", color="#000000", who_size=42, who_bold=True)

# ----------------------------------------------------------------------
# IMAGES
# ----------------------------------------------------------------------
image bg = Transform("images/background.jfif", zoom=1.4, xalign=0.5, yalign=0.5)
image eileen happy = "eileen_happy.png"
image eileen neutral = "eileen_neutral.png"
image eileen worried = "eileen_worried.png"
image eileen scared = "eileen_scared.png"

transform eileen_fit:
    zoom 0.8
    xalign 0.88
    yalign 1.0

# ----------------------------------------------------------------------
# AUDIO
# Place these three files in game/audio/. If they aren't .ogg, change
# the extension below to match (.mp3 and .wav also work in Ren'Py).
#   audio/nottense.ogg  - calm loop for the opening scene
#   audio/tense.ogg     - unsettling loop once things start going wrong
#   audio/moretense.ogg - most intense loop, for the final confrontation
# ----------------------------------------------------------------------
define audio.calm = "audio/tense.ogg"
define audio.tense = "audio/nottense.ogg"
define audio.moretense = "audio/moretense.ogg"

# ----------------------------------------------------------------------
# VARIABLES
# suspicion tracks how paranoid/aggressive the player's choices are.
# trust tracks how much they chose to stay close to Eileen.
# ----------------------------------------------------------------------
default suspicion = 0
default trust = 0

# ----------------------------------------------------------------------
# START
# ----------------------------------------------------------------------
label start:

    play music audio.calm fadein 2.0 loop

    scene bg with dissolve
    show eileen neutral at eileen_fit

    e "I wanted to tell you this somewhere beautiful. It makes the story easier to say."
    e "When I was little, I came here every afternoon and told the garden one thing I had never told anyone else."
    e "I thought the trees were listening. I did not know someone was answering."

    menu:
        "Tell me what happened next.":
            $ trust += 1
            jump story

        "Why did you bring me here?":
            $ trust += 2
            jump story

        "This sounds like a story you made up.":
            $ suspicion += 1
            jump story

label story:
    show eileen happy at eileen_fit
    e "At first, the answers were small. A missing key. A song I had forgotten. Things only I could have known."
    e "Then one afternoon, the voice said my name before I had said anything at all."
    e "It sounded like you."

    menu:
        "I believe you. Keep going.":
            $ trust += 2
            jump secret

        "What did the voice say?":
            $ trust += 1
            jump secret

        "You should have stopped listening.":
            $ suspicion += 1
            jump secret

label secret:
    play music audio.tense fadein 1.5 loop
    show eileen worried at eileen_fit
    e "Here is the part I have never told anyone."
    e "The voice did not just know my secrets. It knew yours."
    e "It told me you would come here tonight, and it asked me to choose what to do with you."

    menu:
        "What did it ask you to do?":
            $ trust += 1
            jump answer

        "Was the voice really mine?":
            $ suspicion += 2
            jump answer

        "We are leaving. Right now.":
            $ trust += 1
            jump answer

label answer:
    show eileen scared at eileen_fit
    e "It asked me to repeat the secret you told me the first time we met."
    e "I remember the secret, but I cannot say it out loud. Not here."

    if suspicion >= 2:
        e "Please do not look behind me. It gets closer when you are afraid."
    else:
        e "I thought I could protect you by telling you the truth. Now I am not sure."

    menu:
        "Take Eileen's hand and tell her to breathe.":
            $ trust += 2
            jump confrontation

        "Ask Eileen to say the secret anyway.":
            $ suspicion += 2
            jump confrontation

        "Tell Eileen you already know who is answering.":
            $ suspicion += 2
            jump confrontation

label confrontation:
    play music audio.moretense fadein 2.0 loop

    if suspicion >= 3:
        show eileen scared at eileen_fit
        e "Eileen steps away from you. 'That is not what I told you,' she says."
        e "Her voice changes on the last word, and suddenly it sounds exactly like yours."
        jump ending_bad

    elif trust >= 3:
        show eileen happy at eileen_fit
        e "Eileen holds your hand until her breathing slows."
        e "'Thank you for listening,' she says. 'Now the secret belongs to both of us.'"
        jump ending_good

    else:
        show eileen worried at eileen_fit
        e "Eileen looks at you for a long moment. Neither of you says the secret."
        jump ending_ambiguous

label ending_bad:
    stop music fadeout 1.0
    "Eileen looks past you. The garden is quiet, but another voice answers from the trees."
    return

label ending_good:
    stop music fadeout 2.0
    "The voice fades. Eileen stays beside you, and the garden becomes quiet again."
    return

label ending_ambiguous:
    stop music fadeout 2.0
    "You leave together, but Eileen keeps looking back at the place where the voice began."
    return
