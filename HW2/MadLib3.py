def getKeys(formatString):
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key)
    return set(keyList)
 
def addPick(cue, dictionary):
    promptFormat = "Enter Word "
    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response
    
def getUserPicks(cues):
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks

def tellStory(storyFormat):
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)

def main():
    filename=input('Enter the filename: ')
    originalStoryFormat=''
    f=open(filename,'r')
    for line in f:
        originalStoryFormat=originalStoryFormat+line.strip()
        tellStory(originalStoryFormat)
        input("Press Enter to end the program.")
main()
