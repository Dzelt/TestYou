
# The game starts here.

label splashscreen:
    $ renpy.movie_cutscene("images/title/splash.ogv")
    return

label start:
    call variable from _call_variable
    call screen welcome("Hello and welcome to this mini quiz game where you can test your local knowledge and science knowledge . Do you think you are smart enough to call yourself a prodigy? Do you believe that this world has limited knowledge which no one is able to gain all? See for yourself and earn the highest points possible. The total points you gain will determine how smart you are. Each correct answer provides 5 points while the wrong answer will deduct 3 points. It is possible that your total points reach a negative number. \n\nOnce you are ready, click Close to Begin and good luck.") with dissolve
    scene bg with dissolve
    stop music fadeout 1.0
    play music BGM2 fadein 1.0
    call question1 from _call_question1
    call question2 from _call_question2
    call question3 from _call_question3
    call question4 from _call_question4
    call question5 from _call_question5
    call question6 from _call_question6
    call question7 from _call_question7
    call question8 from _call_question8
    call question9 from _call_question9
    call question10 from _call_question10
    call question11 from _call_question11
    call question12 from _call_question12
    call question13 from _call_question13
    call question14 from _call_question14
    call question15 from _call_question15
    call question16 from _call_question16
    call question17 from _call_question17
    call question18 from _call_question18
    call question19 from _call_question19
    call question20 from _call_question20
    call scoring from _call_scoring
    call credits from _call_credits
    pause
    return
