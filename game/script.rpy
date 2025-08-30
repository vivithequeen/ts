# The script of the game goes in this file.
$ import random 
# Declare characters used by this game. The color argument colorizes the
# name of the character.


define s = Character(name = "Sofia", color = "#DC143C", voice_tag = "yap.ogg")
define c = Character(name = "CAN", color = "#000000", voice_tag = "yap.ogg")
#DC143C

# The game starts here.

label start:
    play music "TI5OR.ogg"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg intro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show can default

    # These display lines of dialogue.
    c "at ts(the start) there was once a land called HACKCLUB"
    c "ts was a sad land, no joy nor whimsy was apparent in the smiles of the hackclubers"
    c "ts was sad, until a hero came, CAN."
    c "CAN had a vision, an idea, to make ts great again."
    c "ts. dot hackclub. dot com."
    c "A ysws(you shit, we shit), where people send in their amazing, fully working projects and CAN reimagines their imperfect self in a perfect, pure manor."
    menu:
        "okay..?":
            show can sad

            c "ts is amazing!"
        "what is ts?":
            show can happy

            c "im so glad you asked!"

            c "ts is the BEST ysws(you shine, we shine) "
        "who are u":

            c "i am CAN!"

    hide can
    show sofia default  
    s "HAHAHA I HAVE GOT YOU"
    s "TS WILL NEVER HAPPEN, shipwrecked.hackclub.com WAS ALWAYS THE BEST YSWS(you slide, we slide)"
    s "now we shall fight... in the only way possible. ROCK PAPERS SCISSORS!"

    
    $ play = True;
    while(play):
        hide sofia 
        $ rock = renpy.random.randrange(0,3)
        menu:
            
            "rock":# 1
                
                if(rock == 3):
                    show sofia scissors
                    s "SHOOOT YOU WON"
                    $ play = False;
                    jump win
                elif(rock == 1):
                    show sofia rock
                    s "TIE. LETS PLAY AGAIN"
                   
                else:
                    show sofia paper
                    s "HAHA I WIN"
                    $ play = False;
                    jump lose
            "paper":# 2
                if(rock == 1):
                    show sofia rock
                    s "SHOOOT YOU WON"
                    $ play = False;
                    jump win
                elif(rock == 2):
                    show sofia paper
                    s "TIE. LETS PLAY AGAIN"
                    
                else:
                    show sofia rock
                    show sofia scissors
                    s "HAHA I WIN"
                    $ play = False;
                    jump lose
            "scissors": # 3
                if(rock == 2):
                    show sofia paper
                    s "SHOOOT YOU WON"
                    $ play = False;
                    jump win

                elif(rock == 3):
                    show sofia scissors
                    s "TIE. LETS PLAY AGAIN"
                    
                else:
                    show sofia rock
                    s "HAHA I WIN"
                    $ play = False;
                    jump lose
    # This ends the game.

    return


label win:
    hide sofia
    hide can

    show sofia sad 
    s "WAIT NO- YOU DONT KNOW WHAT YOUR DOING, CAN WILL KILL US ALL!!!"
    jump can

label lose:
    hide sofia
    hide can

    show sofia happy 
    s "HAHAHAHAHAHAHAAHA"
    s "GET DESTORYED KID!!"
    jump can

label can:
    hide sofia 
    show can default

    c "YOU MESSED UP NOW!!! WITH SOFIA GONE, ts.hackclub.com HAS ALLOWED ME TO TAKE OVER HACK CLUB!"
    c "ALL OF HACKCLUB WILL NOW BE MINE!!"
    menu:
        "join CAN":
            show can happy
            c "YES! HELP ME TAKE OVER HACKCLUB!!!!!"
            show can happy at left
            show sofia dead at right
            c "with no threats... ts.hackclub.com will be the only ysws(you ts we ts)"

            "ENDING 1 : CAN's ts.hackclub.com"
        "join sofia":
            show can sad
            c "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
            hide can
            show can sad at left
            show sofia happy at right
            s "YES! YOU SHALL BE SAD AND BE GONE"
            show can dead
            c "AHHHHHHHHHHHHHHHHHH *dies*"
            hide can
            show sofia happy at center
            s "now without ts.hackclub.com, shipwrecked.hackclub.com will be the ONLY YSWS(you sketch we sketch)"

            "ENDING 2 : shipwrecked.hackclub.com"
            return

        "revolt aganists CAN and make ts.hackclub.com great again":
            show can sad
            c "NOOOOO"
            hide can
            show sofia sad
            s "NOOOO"
            show can dead at left
            show sofia dead at right

            "with can and sofia sleeping, ts.hackclub.com and shipwrecked.hackclub.com will be combined and be better then all the other ysws(you sleep, we sleep)"
            "ENDING 3 : the good ending"
