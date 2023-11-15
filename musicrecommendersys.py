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

    newPref = ''
    if userName in userMap:
        prefs = userMap[userName]
        print("OMG! You've used this system before!")
        print("Your preferences are: ")
        for artist in prefs:
            print(artist)
        
        print("Please enter another artist you love, or just press Enter: ")
        newPref = input("to see your recommendations: ")
    
    else:
        prefs = []
        print("Welcome newbie!")
        newPref = input("Please enter the name of an artist you love: ")

        while newPref != "":
            prefs.append(newPref.strip().title())
            print("Please enter another artist you love, or just press Enter to see your recommendations.")
            newPref = input("to see your recommendations: ")

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

    recommendations = list(set(recommendations) - set(prefs))

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
        if set(userDict[user]) <= set(prefs):
            continue  
        score = numMatches(prefs, userDict[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user

    return bestUser

def drop(L1, L2): #madelyn
    '''returns new list that contains only the elements in list 2 that are not
    in list 1. Maddy completed this'''
    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            print("Skip", L1[i])
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            L.append(L2[j])
            j += 1
    return L

def numMatches(L1, L2): #madelyn
    '''returns number of elements that match in the 2 lists. Maddy completed this'''
    count = 0
    for i in L1:
        if i in L2:
            count += 1
    return count
    

def saveUserPrefs(userName, prefs, userDict, fileName): #madelyn
    '''writes all of user prefs to the file. Maddy completed this'''
    userDict[userName] = prefs
    with open(fileName, 'w') as file:
        for user in userDict:
            save = str(user) + ": " + ','.join(userDict[user]) + '\n'
            file.write(save)


def showMostPopularArtists(userDict): #Karlo
    artist_likes = {}

    for user, preferences in userDict.items():
        if not preferences or (len(preferences) == 1 and preferences[0] == 'private_mode'):
            continue

        for artist in preferences:
            artist_likes[artist] = artist_likes.get(artist, 0) + 1

    sorted_artists = sorted(artist_likes.items(), key=lambda x: x[1], reverse=True)

    if sorted_artists:
        print("Top 3 Most Popular Artists:")
        for i in range(min(3, len(sorted_artists))):
            print(sorted_artists[i][0])
    else:
        print("Sorry, no artists found.")

def howPopularIsMostPopularArtist(userDict): #Karlo
    '''Print the number of likes the most popular artist received.'''
    artist_likes = {}

    for preferences in userDict.values():
        if not preferences or (len(preferences) == 1 and preferences[0] == 'private_mode'):
            continue

        for artist in preferences:
            artist_likes[artist] = artist_likes.get(artist, 0) + 1

    sorted_artists = sorted(artist_likes.items(), key=lambda x: x[1], reverse=True)

    if sorted_artists:
        print(f"Number of likes for the most popular artist: {sorted_artists[0][1]}")
    else:
        print("Sorry, no artists found.")
def whichUserLikesTheMostArtists(userDict, currUser): #Karlo
    '''Print the full name(s) of the user(s) who like(s) the most artists.'''
    user_likes = {}

    for user, preferences in userDict.items():
        if not userDict[user]['private_mode']:
            user_likes[user] = len(preferences)

    sorted_users = sorted(user_likes.items(), key=lambda x: x[1], reverse=True)

    if sorted_users:
        print("User(s) who like(s) the most artists:")
        for user, _ in sorted_users:
            print(user)
    else:
        print("Sorry, no user found.")

def saveAndQuit(userDict, fileName): #Karlo
    '''Save the current database to the file and exit the program.'''
    with open(fileName, 'w') as file:
        for user, preferences in userDict.items():
            save_line = f"{user}: {','.join(preferences)}\n"
            file.write(save_line)
    
    print("Database saved. Exiting program.")
    exit()

def loadUsers(fileName): #Karlo, Maddie, Ryan
    try:
        file = open(fileName, 'r')
        userDict = {}
        for line in file:
            # read and parse line 1
            [userName, artists] = line.strip().split(':')
            artistList = artists.split(",")
            artistList.sort()
            userDict[userName] = artistList
        file.close()
        return userDict
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found. Creating an empty user dictionary.")
        return {}

def main(): #ryan
    '''main recommendation function'. Ryan completed this.'''
    '''main recommendation function'. Ryan completed this.'''
    userDict = loadUsers(PREF_FILE)
    print("Welcome to your music recommendation system!")

    userName_input = input("Please enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
    private_mode = userName_input.endswith('$')
    userName = userName_input.rstrip('$')

    print("Welcome, ", userName)

    while True:
        print("\nEnter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")

        choice = input("Enter your choice: ")

        if choice == 'e':
            prefs = getPrefs(userName, userDict)
            saveUserPrefs(userName, prefs, userDict, PREF_FILE)
        elif choice == 'r':
            prefs = userDict.get(userName, [])
            recs = getRecs(userName, prefs, userDict)
        elif choice == 'p':
            showMostPopularArtists(userDict)
        elif choice == 'h':
            howPopularIsMostPopularArtist(userDict)
        elif choice == 'm':
            whichUserLikesTheMostArtists(userDict, userName)
        elif choice == 'q':
            saveAndQuit(userDict, PREF_FILE)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()

    

