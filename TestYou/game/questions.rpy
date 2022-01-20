
# All the question is here (Bank Questions)

label question1:
    "Question 1"
    show body :
        ease 1.0 truecenter
    "In which part of your body would you find the cruciate ligament?"
    menu:
        "Knee":
            $ PlayerScore += 5
        "Elbow":
            $ PlayerScore -= 3
        "Arm pit":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide body
    return

label question2:
    "Question 2"
    "What is the name of the main antagonist in the Shakespeare play Othello?"
    menu:
        "Emilia":
            $ PlayerScore -= 3
        "Iago":
            $ PlayerScore += 5
        "Blanca":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question3:
    "Question 3"
    "What element is denoted by the chemical symbol Sn in the periodic table?"
    menu:
        "Tin":
            $ PlayerScore += 5
        "Vanadium":
            $ PlayerScore -= 3
        "Ferum":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question4:
    "Question 4"
    "What is the name of the 1976 film about the Watergate scandal, starring Robert Redford and Dustin Hoffman?"
    menu:
        "Old Farm":
            $ PlayerScore -= 3
        "Yesterday Incident":
            $ PlayerScore -= 3
        "All the President’s Men":
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    return

label question5:
    "Question 5"
    "How many of Henry VIII’s wives were called Catherine?"
    menu:
        "5":
            $ PlayerScore -= 3
        "3":
            $ PlayerScore += 5
        "2":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question6:
    "Question 6"
    "What was the most popular girls name in the UK in 2019?"
    menu:
        "Samantha":
            $ PlayerScore -= 3
        "Olivia ":
            $ PlayerScore += 5
        "Alice":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question7:
    "Question 7"
    "Which comedian was the second permanent host of Never Mind the Buzzcocks after Mark Lamarr?"
    menu:
        "John Aboud":
            $ PlayerScore -= 3
        "Pamela Adlon":
            $ PlayerScore -= 3
        "Simon Amstell":
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    return

label question8:
    "Question 8"
    "Which popular video game franchise has released games with the subtitles World At War and Black Ops?"
    menu:
        "Call of Duty":
            $ PlayerScore += 5
        "Blackzone":
            $ PlayerScore -= 3
        "God of war":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question9:
    "Question 9"
    "In what US State is the city Nashville?"
    menu:
        "Tennessee":
            $ PlayerScore += 5
        "New York":
            $ PlayerScore -= 3
        "Utah":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question10:
    "Question 10"
    "Which rock band was founded by Trent Reznor in 1988?"
    menu:
        "AC/DC":
            $ PlayerScore -= 3
        "The Beatles":
            $ PlayerScore -= 3
        "Nine Inch Nails":
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    return

label question11:
    "Question 11"
    "What is the currency of Denmark?"
    menu:
        "Peso":
            $ PlayerScore -= 3
        "Rand":
            $ PlayerScore -= 3
        "Krone":
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    return

label question12:
    "Question 12"
    "Which Tennis Grand Slam is played on a clay surface?"
    menu:
        "Australian Open":
            $ PlayerScore -= 3
        "The French Open":
            $ PlayerScore += 5
        "Wimbledon":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question13:
    "Question 13"
    "In which European country would you find the Rijksmuseum?"
    menu:
        "Netherlands":
            $ PlayerScore += 5
        "Belgium":
            $ PlayerScore -= 3
        "Germany":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question14:
    "Question 14"
    "How many films have Al Pacino and Robert De Niro appeared in together?"
    menu:
        "Five":
            $ PlayerScore -= 3
        "Four":
            $ PlayerScore += 5
        "Three":
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    return

label question15:
    "Question 15"
    "What was the old name for a Snickers bar before it changed in 1990?"
    menu:
        "Guylian":
            $ PlayerScore -= 3
        "Patchi":
            $ PlayerScore -= 3
        "Marathon":
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    return
