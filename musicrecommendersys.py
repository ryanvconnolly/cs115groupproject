'''
Names: Ryan Connolly, Karlo Medina, Madelyn Pagkalinawan
I pledge my honor that I have abided by the Stevens Honor System
CS 115 Group Project Part 2
'''

PREF_FILE = 'musicrex-store.txt'

def loadUsers(fileName): 
    '''read in file of stored users' preferences from the file. returns dictionary
    of user names and their preferences. Ryan completed this.'''

    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        #read and parse line 1
        [userName, artists] = line.strip().split(':')
        artistList = artists.split(",")
        artistList.sort()
        userDict[userName] = artistList
    
    file.close()
    return userDict

def getPrefs(userName, userMap): 
    '''returns list of user's preferred artists. If system already knows ab
    user, gets info from the dict and asks user if they'd like to provide
    additional preferences. if user is new, asks for their preferences. Ryan
    completed this.'''

    #if user info is already in dictionary
    newPref = ''
    if userName in userMap:
        prefs = userMap[userName]
        print("OMG! You've used this system before!")
        print("Your preferences are: ")
        for artist in prefs:
            print(artist)
        
        print("Please enter another artist you love, \ or just press enter: ")
        newPref = input("to see your recommendations: ")
    
    else:
        prefs = []
        print("Welcome newbie!")
        newPref = input("Please enter the name of an artist you love: ")

        while newPref != "":
            prefs.append(newPref.strip().title())
            print("Please enter another another artist you love, \ or just press Enter to see your recommendations.")
            newPref = input("to see your recommendations: ")

    #keep lists in sorted order to compare easily.
    prefs.sort()
    return prefs
              

def getRecs(currUser, prefs, userDict): #karlo
    '''gets recommendations for current user based on users in the
    user dictionary and their preferences. returns list of recommended
    artists. Karlo completed this.'''
    bestUser = findBestUser(currUser, prefs, userDict)

    if bestUser is not None and userDict[bestUser]['private_mode']:
        print("No recommendations available at this time.")
        return []

    recommendations = drop(prefs, userDict[bestUser])

    recommendations = list(set(recommendations) - set(prefs[currUser]))

    recommendations.sort()

    if recommendations:
        for artist in recommendations:
            print(artist)
    else:
        print("No recommendations available at this time.")

def findBestUser(currUser, prefs, userDict): 
    '''finds user whose preferences are the most similar to current user.
    returns best user's name. Karlo completed this.'''
    users = userDict.keys()
    bestUser = None
    bestScore = -1

    for user in users:
        if userDict[user]['private_mode']:
            continue
        if set(prefs[userDict[user]]) <= set(prefs[currUser]):
            continue  
        score = numMatches(prefs, userDict[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user

    return bestUser

def drop(L1, L2): #madelyn
    '''returns new list that contains only the elements in list 2 that are not
    in list 1. Maddy completed this'''
    pass

def numMatches(L1, L2): #madelyn
    '''returns number of elements that match in the 2 lists. Maddy completed this'''
    pass

def saveUserPrefs(userName, prefs, userDict, fileName): #madelyn
    '''writes all of user prefs to the file. Maddy completed this'''
    pass

def main(): #ryan
    '''main recommendation function'. Ryan completed this.'''

    userDict = loadUsers(PREF_FILE)
    print("Welcome to your music recommendation system!")

    userName = input("Please enter your name: ")
    print("Welcome, ", userName)

    prefs = getPrefs(userName, userDict)
    recs = getRecs(userName, prefs, userDict)

    #Print user recommendations
    if len(recs) == 0:
        print("I'm sorry. I have no recommendations for your right now. Please try again later :(")
    else:
        print(userName+',', "Based on your preferences, I believe you might like: ")
        for artist in recs:
            print(artist)

    print("I hope you are happy with your recommendations. I will save your preferences and recommendations for later! \
            Have a great day!")

    saveUserPreferences(userName, prefs, userMap, PREF_FILE)

    if__name__ == '__main__' : main()



    

