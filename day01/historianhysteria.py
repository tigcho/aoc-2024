import pandas as pd
from collections import Counter

file = "input"
data = pd.read_csv(file, names=["leftList", "rightList"], sep='\s+')
leftList = data["leftList"].tolist()
rightList = data["rightList"].tolist()

def calcTotalDist(leftList, rightList):
    leftList.sort()
    rightList.sort()

    totalDist = sum(abs(l - r) for l, r in zip(leftList, rightList))
    return totalDist

totalDist = calcTotalDist(leftList, rightList)
print("Total distance: ", totalDist)

def calcSimScore(leftList, rightList):
    rightCount = Counter(rightList)
    simScore = sum(num * rightCount[num] for num in leftList)
    return simScore

simScore = calcSimScore(leftList, rightList)
print("Similarity score: ", simScore)
