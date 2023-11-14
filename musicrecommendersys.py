'''
Names: Ryan Connolly, Karlo Medina, Madelyn Pagkalinawan
I pledge my honor that I have abided by the Stevens Honor System
CS 115 Group Project Part 2
'''

PREF_FILE = 'musicrex-store.txt'

def loadUsers(fileName): #ryan
    '''read in file of stored users' preferences from the file. returns dictionary
    of user names and their preferences. Ryan completed this.'''

    pass

def getPrefs(userName, userDict): #ryan
    '''returns list of user's preferred artists. If system already knows ab
    user, gets info from the dict and asks user if they'd like to provide
    additional preferences. if user is new, asks for their preferences. Ryan
    completed this.'''
    pass

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

def findBestUser(currUser, prefs, userDict): #karlo
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



    

