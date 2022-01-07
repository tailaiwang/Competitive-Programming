streamerDict = {}
categoryDict = {}

initial = ["Ninja", "100000", "Fortnite", "Pokimane", "40000", "Valorant"]
topStreamer = [0,0]
for i in range (0, len(initial), 3):
    name = initial[i]
    viewCount = int(initial[i+1])
    category = initial[i + 2]
    streamerDict[name]=[name, viewCount, category]
    if categoryDict.get(category) == None:
        categoryDict[category] = viewCount
    else:
        categoryDict[category] = categoryDict[category] + viewCount
    if viewCount > topStreamer[1]:
        topStreamer = [name, viewCount]


commands = ["StreamerOnline", "Bugha", "75000", "Fortnite", "StreamerOnline", "Tenzo", "30000", "Valorant", "ViewsInCategory", "Fortnite", "TopStreamerInCategory", "Valorant"]
curCommand = 0
while (curCommand < len(commands)):
    if (commands[curCommand] == "StreamerOnline"):
        name = commands[curCommand + 1]
        viewCount = int(commands[curCommand + 2])
        category = commands[curCommand + 3]
        streamerDict[name]=[name, viewCount, category]
        if categoryDict.get(category) == None:
            categoryDict[category] = viewCount
        else:
            categoryDict[category] = categoryDict[category] + viewCount
        if viewCount > topStreamer[1]:
            topStreamer = [name, viewCount]
        curCommand += 4
    elif (commands[curCommand] == "UpdateViews"):
        name = commands[curCommand + 1]
        viewCount  = int(commands[curCommand + 2])
        category = commands[curCommand + 3]
        if streamerDict[name][2] == category:
            oldViewCount = streamerDict[name][1]
            streamerDict[name] = [name, viewCount, category]
            categoryDict[category] = categoryDict[category] - oldViewCount + viewCount
        if viewCount > topStreamer[1]:
            topStreamer = [name, viewCount]
        curCommand += 4
    elif (commands[curCommand] == "UpdateCategory"):
        name = commands[curCommand + 1]
        oldCat = commands[curCommand + 2]
        newCat = commands[curCommand + 3]
        if streamerDict[name][2] == oldCat:
            oldViewCount = streamerDict[name][1]
            streamerDict[name] = [name, oldViewCount, newCat]
            categoryDict[oldCat] = categoryDict[oldCat] - oldViewCount
            if categoryDict.get(newCat) == None:
                categoryDict[newCat] = oldViewCount
            else:
                categoryDict[newCat] = oldViewCount + categoryDict[newCat]
        curCommand += 4
    elif (commands[curCommand] == "StreamerOffline"):
        name = commands[curCommand + 1]
        category = commands[curCommand + 2]
        if streamerDict[name][2] == category:
            oldViewCount = streamerDict[name][1]
            streamerDict.pop(name)
            categoryDict[category] = categoryDict[category] - oldViewCount
            if (name == topStreamer[0]):
                curBiggest = [0,0]
                for key,value in streamerDict.items():
                    if value[1] > curBiggest[1]:
                        curBiggest = [value[0], value[1]]
                topStreamer = curBiggest
        curCommand += 3
    elif (commands[curCommand] == "ViewsInCategory"):
        category = commands[curCommand + 1]
        if categoryDict.get(category) == None:
            print(0)
        else:
            print(categoryDict[category])
        curCommand += 2
    elif (commands[curCommand] == "TopStreamerInCategory"):
        category = commands[curCommand+1]
        curBiggest = [0,0]
        for key,value in streamerDict.items():
            if value[2] == category:
                if value[1] > curBiggest[1]:
                    curBiggest = [value[0], value[1]]
        if (curBiggest[0] ==0):
            print("null")
        else:
            print(curBiggest[1], curBiggest[0])
        curCommand += 2
    elif (commands[curCommand] == "TopStreamer"):
        if (topStreamer[0] == 0):
            print("null")
        else:
            print(topStreamer[1], topStreamer[0])
        curCommand += 1
        
