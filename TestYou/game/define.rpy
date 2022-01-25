

define audio.BGM2 = "audio/BGM2.ogg"
define audio.true = "audio/Correct choosing.ogg"
define audio.wrong = "audio/Wrong choosing.ogg"
define audio.clap = "audio/clapping.ogg"
define audio.rolling = "audio/Drum Roll.ogg"
define audio.aww = "audio/aww.ogg"
define audio.fun = "audio/FunShine.mp3"

image credits = Image("images/title/credit.jpg")
image bg = Image("images/bg.png")
image school = Image("images/School.jpg")
image ealing = Image("images/Ealing.jpg")
image acton = Image("images/Acton.png")
image mps = Image("images/Mps.png")
image rectory = Image("images/Rectory.jpg")
image twyford = Image("images/Twyford.jpg")
image crops = Image("images/crops.jpg")
image religious = Image("images/religious.jpg")
image prime = Image("Images/prime.jpg")
image animal = Image("Images/Animal.jpg")
image item = Image("Images/Item.jpg")
image project = Image("Images/Project.jpg")
image when = Image("images/When.png")
image space = Image("Images/Space.jpg")
image composer = Image("Images/Composer.jpg")
image natural = Image("Images/Natural.jpg")
image medicine = Image("Images/Medicine.jpg")
image gen = Image("Images/Gen.jpg")
image seasons = Image("Images/Seasons.jpg")
image com = Image("Images/Com.jpg")

label credits:
    hide bg
    stop music fadeout 1.0
    play sound fun
    scene credit with dissolve
    pause
    stop sound fadeout 1.0
    return

label variable:
    $ PlayerScore = 0
    $ PlayerName = ""
    return

label scoring:
    stop music fadeout 1.0
    play sound rolling
    call screen scoreInit() with dissolve
    stop sound fadeout 1.0
    if PlayerScore <= 0:
        play sound aww
    else:
        play sound clap
    call screen score("[PlayerScore]")
    stop sound fadeout 1.0
    return
