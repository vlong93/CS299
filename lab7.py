# Author: Vivian Long
# Assignment: Lab 7
# Completed:

# Problem 1
x = 1
data = list()
while x > 0:
    x = float(input("Enter a number (0 to quit): "))
    if x > 0:
        data.append(x)

print("Initial list:", data)
print("Size of list:", len(data))

high = data[0]
for i in data[1:]:
    if i > high:
        high = i

print("Max of list:", high)

newList = list()
for j in data:
    if j >= 25:
        newList.append(j)

print("New list:", newList)


'''
Problem 1 output:
Enter a number (0 to quit): 25
Enter a number (0 to quit): 35.5
Enter a number (0 to quit): 15
Enter a number (0 to quit): 45.5
Enter a number (0 to quit): 55
Enter a number (0 to quit): 30.2
Enter a number (0 to quit): 49.4
Enter a number (0 to quit): 21.1
Enter a number (0 to quit): 41.8
Enter a number (0 to quit): 37
Enter a number (0 to quit): 0
Initial list: [25.0, 35.5, 15.0, 45.5, 55.0, 30.2, 49.4, 21.1, 41.8, 37.0]
Size of list: 10
Max of list: 55.0
New list: [25.0, 35.5, 45.5, 55.0, 30.2, 49.4, 41.8, 37.0]
'''

