# Author: Vivian Long
# Assignment: Project 4
# Completed: 2/18/2018


# Return values from file into a list
def initList(inFile):
    inputfile = open(inFile, "r")
    aList = []
    for line in inputfile:
        aList.append(line)

    return aList


# Number of values in list
def getSize(aList):
    length = len(aList)
    return length


# Highest value in list
def getHighest(aList):
    high = aList[0]
    for i in aList[1:]:
        if i > high:
            high = i

    return high


# Lowest value in list
def getLowest(aList):
    low = aList[0]
    for i in aList[1:]:
        if i < low:
            low = i

    return low


# Average of values in list
def getAverage(aList):
    sum = 0
    for i in aList:
        sum += float(i)
    average = sum / len(aList)

    return average


def main():
    aList = initList("ocean_temp.txt")
    print("Size:", getSize(aList))
    print("Max:", getHighest(aList), end='')
    print("Min:", getLowest(aList), end='')
    print("Average:", getAverage(aList))

    return


main()


'''
Output:

Size: 162
Max: 0.65
Min: -0.01
Average: -0.4016049382716049
'''