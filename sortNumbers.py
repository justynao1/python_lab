# sortowanie liczb
def random():
    import random
    randomList = random.sample(range(1,999), 50)
    #randomList.sort(reverse=True)
    print(randomList)
    for i in range(len(randomList)):
        for j in range(i + 1, len(randomList)):
            if randomList[i] < randomList[j]:
                randomList[i], randomList[j] = randomList[j], randomList[i]
    print(randomList)
#random()