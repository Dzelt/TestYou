
# The game starts here.

label start:
    call variable
    call screen welcome("Hello and welcome to this mini quiz game. Do you think you are smart to call yourself a prodigy? Do you believe that this world has limitless knowledge which no one is able to gain all? See for yourself and earn the highest points possible. Earn at least 50 points to pass. Each correct answer provides 5 points while the wrong answer will deduct 3 points. It is possible that your total points reach a negative number. \n\nOnce you are ready, click Close to Begin and good luck.")
    call question1
    pause
    return

label variable:
    $ PlayerScore = 0
    $ PlayerName = ""
    return
