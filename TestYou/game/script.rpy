
# The game starts here.

label start:
    call variable
    call screen welcome("Hello and welcome to this mini quiz game. Do you think you are smart to call yourself a prodigy? Do you believe that this world has limitless knowledge which no one is able to gain all? See for yourself and earn the highest points possible. Earn at least 50 points to pass. Each correct answer provides 5 points while the wrong answer will deduct 3 points. It is possible that your total points reach a negative number. \n\nOnce you are ready, click Close to Begin and good luck.")
    call question1
    call question2
    call question3
    call question4
    call question5
    call question6
    call question7
    call question8
    call question9
    call question10
    call question11
    call question12
    call question13
    call question14
    call question15

    pause
    return

label variable:
    $ PlayerScore = 0
    $ PlayerName = ""
    return
