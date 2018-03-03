# Author: Vivian Long
# Assignment: Exam 3, Part II
# Date: 3/2/2018

# Task 1
def getData(n):
    scores = []
    count = 0
    while count < n:
        s = float(input("Enter a score: "))
        scores.append(s)
        count += 1
    return scores


def calAverage(scores):
    if len(scores) == 0:
        average = 0
    sum = 0
    for i in scores:
        sum += i
    average = sum / len(scores)
    return average


def main1():
    scores = getData(10)
    print("Average:", calAverage(scores))


main1()

'''
Enter a score: 5
Enter a score: 4.5
Enter a score: 9.5
Enter a score: 6.5
Enter a score: 4
Enter a score: 5
Enter a score: 4.2
Enter a score: 2
Enter a score: 1
Enter a score: 3.8
Average: 4.55
'''


# Task 2
list1 = [5, 4.5, "9.5", "AAA", 3.5, 4, 5.0, 4.2, 2.0, "-1.0", 3.8, 4.6, True]

def numList(alist):
    blist = []
    for i in alist:
        try:
            if type(i) == int:
                blist.append(i)
            elif type(i) == float:
                blist.append(i)
        except (TypeError, ValueError):
            alist.remove(i)
    return blist


def filterData(scoreList):
    for i in scoreList:
        if not 1 <= i <= 5:
            scoreList.remove(i)
    return scoreList


def main2():
    print(numList(list1))
    scores = getData(10)
    print(filterData(scores))

main2()


'''
[5, 4.5, 3.5, 4, 5.0, 4.2, 2.0, 3.8, 4.6]

Enter a score: 5
Enter a score: 4.5
Enter a score: 9.5
Enter a score: 6.5
Enter a score: 4
Enter a score: 5
Enter a score: 4.2
Enter a score: 2
Enter a score: 1
Enter a score: 3.8
[5.0, 4.5, 6.5, 4.0, 5.0, 4.2, 2.0, 1.0, 3.8]
'''