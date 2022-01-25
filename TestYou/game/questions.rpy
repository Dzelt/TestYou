
# All the question is here (Bank Questions)

label question1:
    "Question 1"
    show school :
         ease 1.0 truecenter
    "Which child who was to become a famous film star went to school locally?"
    menu:
        "David Niven":
            play sound wrong
            "Wrong. Niven attended Heatherdown Preparatory School and Stowe School."
            $ PlayerScore -= 3
        "Charlie Chaplin":
            play sound true
            "Correct! Chaplin was sent to Lambeth Workhouse when he was seven years old. The council housed him at the Central London District School for paupers."
            $ PlayerScore += 5
        "Gracie Fields":
            play sound wrong
            "Wrong. She  gave up her job in the local cotton mill, where she was a half-timer, spending half a week in the mill and the other half at school."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide school with easeouttop
    return

label question2:
    "Question 2"
    show ealing at truecenter with easeinleft
    "What was the name of the architect of Ealing Town Hall?"
    menu:
        "Charles Jones":
            play sound true
            "Corrct! He is an American actor, gardener, photographer and composer."
            $ PlayerScore += 5
        "John Soane":
            play sound wrong
            "Incorrect. Sir John Soane RA FSA FRS was an English architect who specialised in the Neo-Classical style."
            $ PlayerScore -= 3
        "Walter Dickens":
            play sound wrong
            "Wrong. He became an officer cadet in the East India Company's Presidency armies just before the Indian Rebellion of 1857."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide ealing with easeouttop
    return

label question3:
    "Question 3"
    show acton at truecenter with easeinright
    "Which of the following was not once a major industry in Acton?"
    menu:
        "Margarine works":
            play sound true
            "Correct. Margarine works is not a major industry in Acton."
            $ PlayerScore += 5
        "Laundries":
            play sound wrong
            "Wrong. Acton was known as Soapsuds Island because of the large number of laundries in one place."
            $ PlayerScore -= 3
        "Engineering works":
            play sound wrong
            "Wrong. Acton was one of the largest concentrations of industry, particularly automobile, in the South of England."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide acton with easeouttop
    return

label question4:
    "Question 4"
    show mps at truecenter with easeinbottom
    "Which of these MPs once lived in Greenford?"
    menu:
        "Winston Churchill":
            play sound wrong
            "Wrong. He served as Prime Minister of the United Kingdom from 1940 to 1945, during the Second World War, and again from 1951 to 1955."
            $ PlayerScore -= 3
        "Oswald Mosley":
            play sound true
            "Correct. He is 6th Baronet was a British politician who rose to fame in the 1920s as a Member of Parliament and later in the 1930s."
            $ PlayerScore += 5
        "Geoffrey Howe":
            play sound wrong
            "Wrong.  He was a British Conservative politician who served as Deputy Prime Minister of the United Kingdom from 1989 to 1990."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide mps with easeouttop
    return

label question5:
    "Question 5"
    show animal at truecenter with easeinleft
    "Which animals once raced in Northolt?"
    menu:
        "Horses":
            play sound true
            "Correct. Horse is the animals raced in Northolt."
            $ PlayerScore += 5
        "Dogs":
            play sound wrong
            "Incorrect. Dogs do not raced."
            $ PlayerScore -= 3
        "Whippets":
            play sound wrong
            "Incorrect. Whippets is a species of dogs and dogs not reced."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide animal with easeouttop
    return

label question6:
    "Question 6"
    show rectory at truecenter with easeinbottom
    "Which decade was Perivale’s ancient rectory demolished?"
    menu:
        "1960s":
            play sound wrong
            "Wrong. The answer is 1950s."
            $ PlayerScore -= 3
        "1970s":
            play sound wrong
            "Wrong. The answer is 1950s."
            $ PlayerScore -= 3
        "1950s":
            play sound true
            "Correct! The neighbouring fifteenth-century Rectory House was demolished in 1958."
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    hide rectory with easeouttop
    return

label question7:
    "Question 7"
    show twyford at truecenter with easeinright
    "What was Twyford Abbey originally built as?"
    menu:
        "An abbey":
            play sound wrong
            "Wrong. The answer is a house."
            $ PlayerScore -= 3
        "A house":
            play sound true
            "Correct! West Twyford (also known as Twyford Abbey) is a small residential area forming a northeastern corner of the London Borough of Ealing."
            $ PlayerScore += 5
        "A castle":
            play sound wrong
            "Wrong. The answer is a house."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide twyford with easeouttop
    return

label question8:
    "Question 8"
    show item at truecenter with easeinleft
    "The Martin Brothers made what domestic items?"
    menu:
        "Pots":
            play sound true
            "Correct. The Martin Brothers – Robert Wallace, Charles, Edwin and Walter – were four brothers and pottery manufacturers in London that produced distinctive stoneware pottery from the 1870s and sporadically through to 1923."
            $ PlayerScore += 5
        "Vacuum cleaners":
            play sound wrong
            "Wrong. The answer is Pots."
            $ PlayerScore -= 3
        "Radio sets":
            play sound wrong
            "Wrong. The answer is Pots."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide item with easeouttop
    return

label question9:
    "Question 9"
    show project at truecenter with easeinbottom
    "What was Brunel’s last major project?"
    menu:
        "The Three Bridges":
            play sound true
            "Correct. He built Maidenhead Bridge across the River Thames, the Wye Bridge at Chepstow, and the Royal Albert Bridge across the River Tamar."
            $ PlayerScore += 5
        "the Wharncliffe Viaduct":
            play sound wrong
            "Wrong. The answer is The Three Bridges."
            $ PlayerScore -= 3
        "Hanwell railway station":
            play sound wrong
            "Wrong. The answer is The Three Bridges."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide project with easeouttop
    return

label question10:
    "Question 10"
    show when at truecenter with easeinright
    "When did Northolt become part of Ealing borough?"
    menu:
        "1926":
            play sound wrong
            "Wrong. The answer is 1928."
            $ PlayerScore -= 3
        "1928":
            play sound true
            "Correct! After the First World War, Ealing, which became a borough in 1901 (the first in Middlesex) began to expand. In 1926, Hanwell, Greenford and Perivale became incorporated into Ealing and these were joined by Northolt in 1928."
            $ PlayerScore += 5
        "1965":
            play sound wrong
            "Wrong. The answer is 1928."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide when with easeouttop
    return

label question11:
    "Question 11"
    show crops at truecenter with easeinright
    "Which crop was Perivale once famous for?"
    menu:
        "Pears":
            play sound wrong
            "Incorrect! The answer is Wheat."
            $ PlayerScore -= 3
        "Rye":
            play sound wrong
            "Incorrect! The answer is Wheat."
            $ PlayerScore -= 3
        "Wheat":
            play sound true
            "Correct. Wheat is the famous crop in Perivale."
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    hide crops with easeouttop
    return

label question12:
    "Question 12"
    show religious at truecenter with easeinleft
    "Which religious building was partly rebuilt with German money?"
    menu:
        "Greenford Methodist church":
            play sound wrong
            "Wrong! The correct one is Ealing Abbey."
            $ PlayerScore -= 3
        "Ealing Abbey":
            play sound true
            "Correct! The church was rebuilt after the reunification of Germany, starting in 1994."
            $ PlayerScore += 5
        "St. Mary’s Norwood":
            play sound wrong
            "Wrong! The correct one is Ealing Abbey."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide religious with easeouttop
    return

label question13:
    "Question 13"
    show space at truecenter with easeinright
    "What is the largest open space in the borough?"
    menu:
        "Horsenden Hill":
            play sound true
            "Correct, It is a hill and open space, located between the Perivale, Sudbury, and Greenford areas of West London.  It is one of the higher eminences in the local area, rising to 85m (276 ft) above sea level, and the summit forms part of the site of an ancient hillfor"
            $ PlayerScore += 5
        "Ealing Common":
            play sound wrong
            "Wrong. Ealing Common is a large open space (approx 47 acres) in Ealing, West London. The Ealing Common Area is bounded by Ealing Town Centre to the west, North Ealing and Hanger Hill to the north, Acton to the east and South Ealing and South Acton to the south."
            $ PlayerScore -= 3
        "Walpole Park":
            play sound wrong
            "Wrong. Walpole Park is a 28 acres (110,000 m2) Grade II municipal park, situated in Ealing (West London). Currently governed by Ealing Council, it was initially the grounds of Pitzhanger Manor, the early 19th-century country home of Sir John Soane."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide space with easeouttop
    return

label question14:
    "Question 14"
    show prime at truecenter with easeinbottom
    "Which former Prime Minister lived in Ealing?"
    menu:
        "Neil Kinnock":
            play sound wrong
            "Wrong. Neil Gordon Kinnock, Baron Kinnock PC (born 28 March 1942) is a Welsh politician. He was born and raised in South Wales."
            $ PlayerScore -= 3
        "Spencer Perceval":
            play sound true
            "Correct! Spencer Perceval KC (1 November 1762 – 11 May 1812) was a British statesman and barrister. He was Prime Minister of the United Kingdom from October 1809 until his assassination in May 1812."
            $ PlayerScore += 5
        "Robert Walpole":
            play sound wrong
            "Wrong. Walpole was born in Houghton, Norfolk, in 1676."
            $ PlayerScore -= 3
    "Your curent score: [PlayerScore]."
    hide prime with easeouttop
    return

label question15:
    "Question 15"
    show composer at truecenter with easeinleft
    "Which famous composer died in Ealing?"
    menu:
        "Edward Elgar":
            play sound wrong
            "Wrong.  Elgar died on 23 February 1934 at the age of seventy-six and was buried next to his wife at St Wulstan's Roman Catholic Church in Little Malvern."
            $ PlayerScore -= 3
        "Frederick Delius":
            play sound wrong
            "Wrong. She chose St Peter's church, Limpsfield, Surrey as the site for the grave."
            $ PlayerScore -= 3
        "Gustav Holst":
            play sound true
            "Correct! Holst died in London on 25 May 1934, at the age of 59, of heart failure following an operation on his ulcer."
            $ PlayerScore += 5
    "Your curent score: [PlayerScore]."
    hide composer with easeouttop
    return

label question16:
    "Question 16"
    show natural at truecenter with easeinright
    "Oil, natural gas and coal are examples of …"
    menu:
        "Geothermal resources":
            play sound wrong
            "Wrong! this Geothermal is energy form heat inside the earth into electricity."
            $ PlayerScore -=3
        "Renewable resources":
            play sound wrong
            "Incorrect! Natural gas and coal are not renewable resources."
            $ PlayerScore -=3
        "Fossil fuels":
            play sound true
            "Correct! Fossil fuels are made from decomposing plants and animals. These fuels are found in the Earth's crust and contain carbon and hydrogen, which can be burned for energy."
            $ PlayerScore +=5
    "Your curent score: [PlayerScore]."
    hide natural with easeouttop
    return

label question17:
    "Question 17"
    show medicine at truecenter with easeinbottom
    "A scientist is conducting a study to determine how well a new medication treats ear infections. The scientist tells the participants to put 10 drops in their infected ear each day. After two weeks, all participants' ear infections had healed."
    "Which of the following changes to the design of this study would most improve the ability to test if the new medication effectively treats ear infections?"
    menu:
        "Create a second group of participants with ear infections who use 15 drops a day":
            play sound wrong
            "Wrong! The answer is create a second group of participants with ear infections who do not use any ear drops"
            $ PlayerScore -=3
        "Have participants use ear drops for only one week":
            play sound wrong
            "Wrong! The answer is create a second group of participants with ear infections who do not use any ear drops"
            $ PlayerScore -=3
        "Create a second group of participants with ear infections who do not use any ear drops":
            play sound true
            "Correct! This to compare the effect for those who did not use the ear drop. This way we can distinguish the difference between using and not using an ear drop."
            $ PlayerScore +=5
    "Your curent score: [PlayerScore]."
    hide medicine with easeouttop
    return

label question18:
    "Question 18"
    show gen at truecenter with easeinleft
    "Which of the following is an example of genetic engineering?"
    menu:
        "Growing a whole plant from a single cell":
            play sound wrong
            "Wrong!  The answer is Inserting a gene into plants that makes them resistant to insects"
            $ PlayerScore -=3
        "Inserting a gene into plants that makes them resistant to insects":
            play sound true
            "Correct! Genetic engineering is the process of using recombinant DNA (rDNA) technology to alter the genetic makeup of an organism."
            $ PlayerScore +=5
        "Attaching the root of one type of plant to the stem of another type of plant":
            play sound wrong
            "Wrong!  The answer is Inserting a gene into plants that makes them resistant to insects"
            $ PlayerScore -=3
    "Your curent score: [PlayerScore]."
    hide gen with easeouttop
    return

label question19:
    "Queestion 19"
    show seasons at truecenter with easeinright
    "What is the main cause of seasons on the Earth?"
    menu:
        "The distance between the Earth and the sun":
            play sound wrong
            "Incorrect! The answer is The tilt of the Earth's axis in relation to the sun"
            $ PlayerScore -=3
        "The tilt of the Earth's axis in relation to the sun":
            play sound true
            "Correct! When the earth's axis points towards the sun, it is summer for that hemisphere. When the earth's axis points away, winter can be expected."
            $ PlayerScore +=5
        "The speed that the Earth rotates around the sun":
            play sound wrong
            "Incorrect! The answer is The tilt of the Earth's axis in relation to the sun."
            $ PlayerScore -=3
    "Your curent score: [PlayerScore]."
    hide seasons with easeouttop
    return

label question20:
    "Question 20"
    show com at truecenter with easeinbottom
    "The time a computer takes to start has increased dramatically. One possible explanation for this is that the computer is running out of memory."
    menu:
        "Hypothesis":
            play sound true
            "Correct! Hypothesis is an idea or theory that is not proven but that leads to further study or discussion."
            $ PlayerScore +=5
        "Conclusion":
            play sound wrong
            "Incorrect! The answer is Hypothesis."
            $ PlayerScore -=3
        "Experiment":
            play sound wrong
            "Incorrect! The answer is Hypothesis."
            $ PlayerScore -=3
    "Your curent score: [PlayerScore]."
    hide com with easeouttop
    return
