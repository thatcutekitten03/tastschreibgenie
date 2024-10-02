import words as WordList
import player as PlayerHandler
import genie as Lang
import external as _ThisClient

import requests
r = requests.get('https://raw.githubusercontent.com/thatcutekitten03/thatcutekitten03.github.io/tree/main/ecloud/newest.py')
print (r.text)


# Ändern
Wordlist = WordList.CurrentWordList
SchoolMode = True
ListenToLowerCase = WordList.LowerCase
SaveProfile = True
RequireTutorial = WordList.Tutorial

# NICHT! ÄNDERN (bei fragen.. Fragen.)
CurrentWord = 0
HasTutorialised = 0
NewPlayerName = "$newPlayer"

print("\n" * 100 + "___                                         \n |  _.  _ _|_  _  _ |_  ._ _  o |_   _  ._  \n | (_| _>  |_ _> (_ | | | (/_ | |_) (/_ | | \n")
print("|_         |  _.  _  _  ._     _. ._   _|     |  _. ._  ._  o  _ \n|_) \/   \_| (_| _> (_) | |   (_| | | (_|   \_| (_| | | | | | _> \n    /                                                            ")
with open('_internal/local.profile', 'r') as file:
    LocalData = file.read()
    LocalData = LocalData.lower().split(';')
    if SchoolMode == False:
        print("local.profile:")
        print(LocalData)
    HasIntroduced = LocalData[0]
with open('_internal/tutorial.txt', 'r') as file:
    LocalTutorialData = file.read()
    LocalTutorialData = LocalTutorialData.split(':')
    TutorialText = LocalTutorialData[0].split(";")

def _introduce():
    global PlayerHandler, LocalData, CurrentWord, NewPlayerName
    print(Lang.game_no_profile_found)
    NewPlayerName = input("<TastSchreib Genie> "+ Lang.player_not_yet_added +"\n\n")
    print("\n<TastSchreib Genie> " + Lang.player_greet + NewPlayerName+ "!")
    LocalData[0] = "true;"
    LocalData[1] = NewPlayerName + ";"
    LocalData[2] = str(int(LocalData[2]) + CurrentWord)
    #print(LocalData)
    if SaveProfile == True:
        f = open("_internal/local.profile", "w")
        f.write(''.join(LocalData))
        f.close()
    _tutorial()
def _tutorial():
    global HasTutorialised, RequireTutorial
    
    if RequireTutorial == False: 
        while HasTutorialised == 0:
            InputHandler = input("<TastSchreib Genie> "+ Lang.player_tutorial_question +"\n\n")
            if InputHandler.lower() == Lang.player_tutorial_answer_yes:
                HasTutorialised = 1
            elif InputHandler.lower() == Lang.player_tutorial_answer_no:
                HasTutorialised = 1
                
            else:
                print("\n\n<TastSchreib Genie> " + Lang.player_answer_not_found)
    if RequireTutorial == True:
        _enter_tutorial()
        
def _enter_tutorial():
    print("\n<TastSchreib Genie> "+TutorialText[0])
    print("<TastSchreib Genie> "+TutorialText[1])
    print("<TastSchreib Genie> "+TutorialText[2])
    print("<TastSchreib Genie> "+TutorialText[3])
    print("<TastSchreib Genie> "+TutorialText[4])
    print("<TastSchreib Genie> "+TutorialText[5])
    print("<TastSchreib Genie> "+TutorialText[6] +"\n")
    pass

def _newWord():
    global CurrentWord, Wordlist, LocalData,NewPlayerName
    LocalData[0] = "true;"
    LocalData[1] = NewPlayerName + ";"
    LocalData[2] = str(int(LocalData[2]) + CurrentWord)
    if SaveProfile == True:
        f = open("_internal/local.profile", "w")
        f.write(''.join(LocalData))
        f.close()
    CurrentWord = CurrentWord + 1
    if SchoolMode == False:
        print('[DEBUG] Changin Word!')
    else:
        pass

def _restart():
    print("[DEBUG] Restart Mode Started")
    IouHandler = input(Lang.game_waiting_on_host)

if HasIntroduced == "false":
    _introduce()
else:
    print("<TastSchreib Genie> "+Lang.player_welcome_back+LocalData[1],"!")
    print("<TastSchreib Genie> "+Lang.player_your_hiscore+LocalData[2])

while True:

    if Wordlist[CurrentWord] == "$stop":
        print(Lang.game_ended)
        _restart()

    print("\nDein Wort: ",Wordlist[CurrentWord])
    UserInputHandler = input("            ")
    if ListenToLowerCase == False:     
        if UserInputHandler == Wordlist[CurrentWord]:
            _newWord()
        if UserInputHandler == "$reset":
            f = open("_internal/local.profile", "w")
            f.write('false;resetname')
            f.close()
    else: 
        if UserInputHandler.lower() == Wordlist[CurrentWord].lower():
            _newWord()
