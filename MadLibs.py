from tkinter import *


root = Tk()
root.title("MadLibs")
root.configure(background="white")

headerFrame = Frame(root)
headerFrame.pack(fill=X)
mainFrame = Frame(root)
mainFrame.pack()

listWig = []
wigCount = -1

#===================Header===================
headerText = Label(headerFrame, text="MadLibs", bg="#7E7299", fg="#121533", font="none 30 bold")
headerText.pack(fill=X)
#===================Header===================

def exitML():
    root.destroy()
    exit()

def wigList(wig):
    global wigCount
    wigCount += 1
    listWig.append(wig)

def clearScreen():
    global wigCount
    global listWig
    for i in range(0,wigCount+1):
        listWig[i].destroy()
    wigCount = -1
    listWig = []

def checkAnswers():
    global MLPlaying
    global posTotal
    global posLabels
    global posEntries
    global posAnswers
    compAns = posTotal
    for n in range(0, posTotal):
        posAnswers[n] = posEntries[n].get()
        if posAnswers[n] is "":
            FillAllAns = Label(mainFrame, text="Please fill in all boxes", bg="white", fg="red", font="none 16 bold underline")
            FillAllAns.grid(row=posTotal+7, column=0, sticky=N, columnspan=2)
            wigList(FillAllAns)
        else:
            compAns -= 1
        if compAns is 0:
            if MLPlaying is "PrepToFight":
                PrepToFightA()
            if MLPlaying is "Vacations":
                VacationsA()
            if MLPlaying is "Pizza":
                PizzaA()

def crtEntry(prtos):
    global posCount
    global posLabels
    global posEntries
    posCount += 1
    posLabels[posCount] = Label(mainFrame, text=prtos, bg="white", fg="#121533", font="none 12 bold")
    posLabels[posCount].grid(row=posCount+5, column=0, sticky=E)
    wigList(posLabels[posCount])
    posEntries[posCount] = Entry(mainFrame, width=20, bg="grey")
    posEntries[posCount].grid(row=posCount+5, column=1, sticky=W)
    wigList(posEntries[posCount])

#<><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><>PrepToFight<><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><>
def PrepToFightQ():
    clearScreen()
    global MLPlaying
    global posCount
    global posTotal
    global posLabels
    global posEntries
    global posAnswers
    MLPlaying = "PrepToFight"
    posCount= -1
    posTotal = 17
    posLabels = []
    posEntries = []
    posAnswers = []
    for i in range(0, posTotal):
        posLabels.append(str(i))
        posEntries.append(str(i))
        posAnswers.append("")

    #-------------Title-------------
    mlTitle = Label(mainFrame, text="Prepare to Fight!", bg="white", fg="#121533", font="none 16 bold underline")
    mlTitle.grid(row=1, column=0, sticky=N, columnspan=2)
    wigList(mlTitle)

    #-------------Dividers-------------
    divider1 = Label(mainFrame, text="-------------------------------------------------")
    divider1.grid(row=2, columnspan=2)
    wigList(divider1)
    divider2 = Label(mainFrame, text="-------------------------------------------------")
    divider2.grid(row=0, columnspan=2)
    wigList(divider2)

    #-------------Instructions-------------
    fillBoxes1 = Label(mainFrame, text="Please fill in the boxes according to", bg="white", fg="#121533", font="none 12 bold")
    fillBoxes1.grid(row=3, column=0, sticky=N, columnspan=2)
    wigList(fillBoxes1)
    fillBoxes2 = Label(mainFrame, text="the prompted part of speech", bg="white", fg="#121533", font="none 12 bold")
    fillBoxes2.grid(row=4, column=0, sticky=N, columnspan=2)
    wigList(fillBoxes2)

    #-------------Inputs-------------
    crtEntry("Adjective:")
    crtEntry("Verb ending in 'ing':")
    crtEntry("Type of food:")
    crtEntry("Noun:")
    crtEntry("Verb:")
    crtEntry("Number:")
    crtEntry("Verb:")
    crtEntry("Part of the body(plural):")
    crtEntry("Verb:")
    crtEntry("Type of food:")
    crtEntry("Plural noun:")
    crtEntry("Adjective:")
    crtEntry("Adjective:")
    crtEntry("Noun:")
    crtEntry("Noun:")
    crtEntry("Noun:")
    crtEntry("Verb:")

    #-------------Button-------------
    continueBtn = Button(mainFrame, text="Continue", fg="#121533", font="none 12 bold", relief=GROOVE, command=checkAnswers)
    continueBtn.grid(row=posTotal+6, columnspan=2)
    wigList(continueBtn)

def PrepToFightA():
    clearScreen()
    global posAnswers

    mlTitle = Label(mainFrame, text="Prepare to Fight!", bg="white", fg="#121533", font="none 16 bold underline")
    mlTitle.grid(row=1, column=0, sticky=N, columnspan=2)
    wigList(mlTitle)

    #-------------Dividers-------------
    divider1 = Label(mainFrame, text="-------------------------------------------------")
    divider1.grid(row=2, columnspan=2)
    wigList(divider1)
    divider2 = Label(mainFrame, text="-------------------------------------------------")
    divider2.grid(row=0, columnspan=2)
    wigList(divider2)

    MLResult = Text(mainFrame, width=80, height=24, wrap=WORD, background="white")
    MLResult.grid(row=3, columnspan=2, sticky=N)
    wigList(MLResult)

    vmlRes = "Mario: what a/an " + posAnswers[0] + " day, eh Luigi? The perfect day for " + posAnswers[1] + " some Koopas. The " + posAnswers[2] + " Kingdom is crawling with them! \n\nLuigi: You're right about that, dear " + posAnswers[3] + ". I hope you're ready to " + posAnswers[4] + ". \n\nMario: Ready? I've waited " + posAnswers[5] + " years to " + posAnswers[6] + " that scoundrel Bowser! \n\nLuigi: Pipe down. He has " + posAnswers[7] + " everywhere. \n\nMario: First, I'll " + posAnswers[8] + " and grab a/an " + posAnswers[9] + ". That'll give me " + posAnswers[10] + ". \n\nLuigi: And I'll grab a/an " + posAnswers[11] + " star. Then I'll be the most " + posAnswers[12] + " plumber of all time. \n\nMario: Remember we're there to rescue Princess " + posAnswers[13] + ", Luigi. Once we do that we'll be heros! \n\nLuigi: Then let's slide down that pipe and save the " + posAnswers[14] + "! \n\nMario: That's the spirit, brother! Get your " + posAnswers[15] + " ready. It's time to " + posAnswers[16] + "!"
    MLResult.insert(END, vmlRes)

    #-------------Button-------------
    menuBTN = Button(mainFrame, text="Menu", fg="#121533", font="none 12 bold", relief=GROOVE, command=menu)
    menuBTN.grid(row=4, column=0, sticky=E)
    wigList(menuBTN)
    quitBTN = Button(mainFrame, text="Quit", fg="#121533", font="none 12 bold", relief=GROOVE, command=exitML)
    quitBTN.grid(row=4, column=1, sticky=W)
    wigList(quitBTN)
#<><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><>PrepToFight<><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><>

#<><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><>Vacations<><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><>
def VacationsQ():
    clearScreen()
    global MLPlaying
    global posCount
    global posTotal
    global posLabels
    global posEntries
    global posAnswers
    MLPlaying = "Vacations"
    posCount= -1
    posTotal = 19
    posLabels = []
    posEntries = []
    posAnswers = []
    for i in range(0, posTotal):
        posLabels.append(str(i))
        posEntries.append(str(i))
        posAnswers.append("")

    #-------------Title-------------
    mlTitle = Label(mainFrame, text="Vacations", bg="white", fg="#121533", font="none 16 bold underline")
    mlTitle.grid(row=1, column=0, sticky=N, columnspan=2)
    wigList(mlTitle)

    #-------------Dividers-------------
    divider1 = Label(mainFrame, text="-------------------------------------------------")
    divider1.grid(row=2, columnspan=2)
    wigList(divider1)
    divider2 = Label(mainFrame, text="-------------------------------------------------")
    divider2.grid(row=0, columnspan=2)
    wigList(divider2)

    #-------------Instructions-------------
    fillBoxes1 = Label(mainFrame, text="Please fill in the boxes according to", bg="white", fg="#121533", font="none 12 bold")
    fillBoxes1.grid(row=3, column=0, sticky=N, columnspan=2)
    wigList(fillBoxes1)
    fillBoxes2 = Label(mainFrame, text="the prompted part of speech", bg="white", fg="#121533", font="none 12 bold")
    fillBoxes2.grid(row=4, column=0, sticky=N, columnspan=2)
    wigList(fillBoxes2)

    #-------------Inputs-------------
    crtEntry("Adjective:")
    crtEntry("Adjective:")
    crtEntry("Noun:")
    crtEntry("Noun:")
    crtEntry("Plural Noun:")
    crtEntry("Game:")
    crtEntry("Plural Noun:")
    crtEntry("Verb ending in 'ing':")
    crtEntry("Verb ending in 'ing':")
    crtEntry("Plural Noun:")
    crtEntry("Verb ending in 'ing':")
    crtEntry("Noun:")
    crtEntry("Plant:")
    crtEntry("Part of the body:")
    crtEntry("A place:")
    crtEntry("Verb ending in 'ing':")
    crtEntry("Adjective:")
    crtEntry("Number:")
    crtEntry("Plural Noun:")

    #-------------Button-------------
    continueBtn = Button(mainFrame, text="Continue", fg="#121533", font="none 12 bold", relief=GROOVE, command=checkAnswers)
    continueBtn.grid(row=posTotal+6, columnspan=2)
    wigList(continueBtn)

def VacationsA():
    clearScreen()
    global posAnswers

    mlTitle = Label(mainFrame, text="Vacations", bg="white", fg="#121533", font="none 16 bold underline")
    mlTitle.grid(row=1, column=0, sticky=N, columnspan=2)
    wigList(mlTitle)

    #-------------Dividers-------------
    divider1 = Label(mainFrame, text="-------------------------------------------------")
    divider1.grid(row=2, columnspan=2)
    wigList(divider1)
    divider2 = Label(mainFrame, text="-------------------------------------------------")
    divider2.grid(row=0, columnspan=2)
    wigList(divider2)

    MLResult = Text(mainFrame, width=80, height=12, wrap=WORD, background="white")
    MLResult.grid(row=3, columnspan=2, sticky=N)
    wigList(MLResult)

    vmlRes = "A vacation is when you take a trip to some " + posAnswers[0] + " place with your " + posAnswers[1] + " family. Usually you go to some place that is near a/an " + posAnswers[2] + " or up on a/an " + posAnswers[3] + ". A good vacation place is one where you can ride " + posAnswers[4] + " or play " + posAnswers[5] + " or go hunting for " + posAnswers[6] + ". I like to spend my time " + posAnswers[7] + " or " + posAnswers[8] + ". When parents go on a vacation, they spend their time eating three " + posAnswers[9] + " a day, and fathers play golf, and mothers sit around " + posAnswers[10] + ". Last summer, my little brother fell in a/an " + posAnswers[11] + " and got poison " + posAnswers[12] + " all over his " + posAnswers[13] + ". My family is going to go to (the) " + posAnswers[14] + ", and I will practice " + posAnswers[15] + ". Parents need vacations more than kids because parents are always very " + posAnswers[16] + " and because they have to work " + posAnswers[17] + " hours every day all year making enough " + posAnswers[18] + " to pay for the vacation."
    MLResult.insert(END, vmlRes)

    #-------------Button-------------
    menuBTN = Button(mainFrame, text="Menu", fg="#121533", font="none 12 bold", relief=GROOVE, command=menu)
    menuBTN.grid(row=4, column=0, sticky=E)
    wigList(menuBTN)
    quitBTN = Button(mainFrame, text="Quit", fg="#121533", font="none 12 bold", relief=GROOVE, command=exitML)
    quitBTN.grid(row=4, column=1, sticky=W)
    wigList(quitBTN)
#<><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><>Vacations<><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><>

#<><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><>Pizza Pizza<><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><>
def PizzaQ():
    clearScreen()
    global MLPlaying
    global posCount
    global posTotal
    global posLabels
    global posEntries
    global posAnswers
    MLPlaying = "Pizza"
    posCount= -1
    posTotal = 15
    posLabels = []
    posEntries = []
    posAnswers = []
    for i in range(0, posTotal):
        posLabels.append(str(i))
        posEntries.append(str(i))
        posAnswers.append("")

    #-------------Title-------------
    mlTitle = Label(mainFrame, text="Pizza Pizza", bg="white", fg="#121533", font="none 16 bold underline")
    mlTitle.grid(row=1, column=0, sticky=N, columnspan=2)
    wigList(mlTitle)

    #-------------Dividers-------------
    divider1 = Label(mainFrame, text="-------------------------------------------------")
    divider1.grid(row=2, columnspan=2)
    wigList(divider1)
    divider2 = Label(mainFrame, text="-------------------------------------------------")
    divider2.grid(row=0, columnspan=2)
    wigList(divider2)

    #-------------Instructions-------------
    fillBoxes1 = Label(mainFrame, text="Please fill in the boxes according to", bg="white", fg="#121533", font="none 12 bold")
    fillBoxes1.grid(row=3, column=0, sticky=N, columnspan=2)
    wigList(fillBoxes1)
    fillBoxes2 = Label(mainFrame, text="the prompted part of speech", bg="white", fg="#121533", font="none 12 bold")
    fillBoxes2.grid(row=4, column=0, sticky=N, columnspan=2)
    wigList(fillBoxes2)

    #-------------Inputs-------------
    crtEntry("Adjective:")
    crtEntry("Nationality:")
    crtEntry("Person:")
    crtEntry("Noun:")
    crtEntry("Adjective:")
    crtEntry("Noun:")
    crtEntry("Adjective:")
    crtEntry("Adjective:")
    crtEntry("Plural noun:")
    crtEntry("Noun:")
    crtEntry("Number:")
    crtEntry("Shapes:")
    crtEntry("Food:")
    crtEntry("Food:")
    crtEntry("Number:")

    #-------------Button-------------
    continueBtn = Button(mainFrame, text="Continue", fg="#121533", font="none 12 bold", relief=GROOVE, command=checkAnswers)
    continueBtn.grid(row=posTotal+6, columnspan=2)
    wigList(continueBtn)

def PizzaA():
    clearScreen()
    global posAnswers

    mlTitle = Label(mainFrame, text="Pizza Pizza", bg="white", fg="#121533", font="none 16 bold underline")
    mlTitle.grid(row=1, column=0, sticky=N, columnspan=2)
    wigList(mlTitle)

    #-------------Dividers-------------
    divider1 = Label(mainFrame, text="-------------------------------------------------")
    divider1.grid(row=2, columnspan=2)
    wigList(divider1)
    divider2 = Label(mainFrame, text="-------------------------------------------------")
    divider2.grid(row=0, columnspan=2)
    wigList(divider2)

    MLResult = Text(mainFrame, width=80, height=7, wrap=WORD, background="white")
    MLResult.grid(row=3, columnspan=2, sticky=N)
    wigList(MLResult)

    vmlRes = "Pizza was invented by a  " + posAnswers[0] + " " + posAnswers[1] + " chef named " + posAnswers[2] + ". To make a pizza, you need to take a lump of " + posAnswers[3] + ", and make a thin, round " + posAnswers[4] + " " + posAnswers[5] + ". Then you cover it with " + posAnswers[6] + " sauce, " + posAnswers[7] + " cheese, and fresh chopped " + posAnswers[8] + ". Next you have to bake it in a very hot " + posAnswers[9] + ". When it is done, cut it into " + posAnswers[10] + " " + posAnswers[11] + ". Some kids like " + posAnswers[12] + " pizza the best, but my favorite is the " + posAnswers[13] + " pizza. If I could, I would eat pizza " + posAnswers[14] + " times a day!"
    MLResult.insert(END, vmlRes)

    #-------------Button-------------
    menuBTN = Button(mainFrame, text="Menu", fg="#121533", font="none 12 bold", relief=GROOVE, command=menu)
    menuBTN.grid(row=4, column=0, sticky=E)
    wigList(menuBTN)
    quitBTN = Button(mainFrame, text="Quit", fg="#121533", font="none 12 bold", relief=GROOVE, command=exitML)
    quitBTN.grid(row=4, column=1, sticky=W)
    wigList(quitBTN)
#<><><><><><><><><><><><><><><><><><><><><>
#<><><><><><><><>Pizza Pizza<><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><>



#===================Menu===================
def menu():
    clearScreen()
    global MLPlaying
    #-------------Greeting-------------
    greetingText = Label(mainFrame, text="Welcome to the MadLibs Game!", bg="white", fg="#121533", font="none 12 bold")
    greetingText.grid(row=1, column=0, sticky=N)
    wigList(greetingText)

    #-------------Instructions-------------
    menuEXPL1 = Label(mainFrame, text="Instructions: you will be given multiple parts of speech.", bg="white", fg="#121533", font="none 12 bold")
    menuEXPL1.grid(row=2, column=0, sticky=N)
    wigList(menuEXPL1)
    menuEXPL2 = Label(mainFrame, text="Fill in each with a word that fits. After you are done, the", bg="white", fg="#121533", font="none 12 bold")
    menuEXPL2.grid(row=3, column=0, sticky=N)
    wigList(menuEXPL2)
    menuEXPL3 = Label(mainFrame, text="words will be put in a story for you to read.", bg="white", fg="#121533", font="none 12 bold")
    menuEXPL3.grid(row=4, column=0, sticky=N)
    wigList(menuEXPL3)

    #-------------Divider-------------
    menuLine1 = Label(mainFrame, text="-------------------------------------------------")
    menuLine1.grid(row=5)
    wigList(menuLine1)
    menuLine = Label(mainFrame, text="-------------------------------------------------")
    menuLine.grid(row=0)
    wigList(menuLine)

    #-------------MadLib List-------------
    menuMLOpts = Label(mainFrame, text="Pick one of these MadLibs:", fg="#121533", font="none 12 bold")
    menuMLOpts.grid(row=6)
    wigList(menuMLOpts)

    PrepFightMuBtn = Button(mainFrame, text="PREPARE TO FIGHT!", fg="#121533", font="none 12 bold", relief=GROOVE, command=PrepToFightQ)
    PrepFightMuBtn.grid(row=7)
    wigList(PrepFightMuBtn)

    VacationsMuBtn = Button(mainFrame, text="Vacations", fg="#121533", font="none 12 bold", relief=GROOVE, command=VacationsQ)
    VacationsMuBtn.grid(row=8)
    wigList(VacationsMuBtn)

    PizzaPizzaBtn = Button(mainFrame, text="Pizza Pizza", fg="#121533", font="none 12 bold", relief=GROOVE, command=PizzaQ)
    PizzaPizzaBtn.grid(row=9)
    wigList(PizzaPizzaBtn)

    quitBTN = Button(mainFrame, text="Quit", fg="#121533", font="none 12 bold", relief=GROOVE, command=exitML)
    quitBTN.grid(row=11,)
    wigList(quitBTN)

    divider1 = Label(mainFrame, text="-------------------------------------------------")
    divider1.grid(row=10, columnspan=2)
    wigList(divider1)
    divider2 = Label(mainFrame, text="-------------------------------------------------")
    divider2.grid(row=12, columnspan=2)
    wigList(divider2)
#===================Menu===================

menu()


root.mainloop()


