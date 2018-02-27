# Author: Vivian Long
# Assignment: Lab 7
# Completed:

import sys

# Problem 1
# Step 1
x = 1
data = list()
while x > 0:
    x = float(input("Enter a score (0 to quit): "))
    if x > 0:
        data.append(x)

print("Initial list:", data)
print("Size of list:", len(data))

# Step 2
high = data[0]
for i in data[1:]:
    if i > high:
        high = i

print("Max of list:", high)

# Step 3
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


# Problem 2
# Step 1
names = list()
while len(names) < len(data):
    n = input("Enter a name: ")
    names.append(n)

# Step 2
d = dict(zip(names, data))
print("Dictionary:", d)

# Step 3
name = input("Enter a name to search: ")
if name not in d:
    print("Name not found.")
else:
    print(name, "Score:", d[name])

# Step 4
d["Alice"] = 56.6
print("Adding Alice...\n", d)

# Step 5
del d["Mary"]
print("Deleting Mary...\n", d)


'''
Problem 2 output:
Enter a score (0 to quit): 25
Enter a score (0 to quit): 35.5
Enter a score (0 to quit): 15
Enter a score (0 to quit): 45.5
Enter a score (0 to quit): 55
Enter a score (0 to quit): 30.2
Enter a score (0 to quit): 49.4
Enter a score (0 to quit): 21.1
Enter a score (0 to quit): 41.8
Enter a score (0 to quit): 37
Enter a score (0 to quit): 0
Initial list: [25.0, 35.5, 15.0, 45.5, 55.0, 30.2, 49.4, 21.1, 41.8, 37.0]
Size of list: 10
Max of list: 55.0
New list: [25.0, 35.5, 45.5, 55.0, 30.2, 49.4, 41.8, 37.0]
Enter a name: Mary
Enter a name: Ted
Enter a name: Bob
Enter a name: Sally
Enter a name: Sara
Enter a name: Tom
Enter a name: Alex
Enter a name: Jordan
Enter a name: Robert
Enter a name: Kim
Dictionary: {'Mary': 25.0, 'Ted': 35.5, 'Bob': 15.0, 'Sally': 45.5, 'Sara': 55.0, 'Tom': 30.2, 'Alex': 49.4, 'Jordan': 21.1, 'Robert': 41.8, 'Kim': 37.0}
Enter a name to search: Ted
Ted Score: 35.5
Adding Alice...
 {'Mary': 25.0, 'Ted': 35.5, 'Bob': 15.0, 'Sally': 45.5, 'Sara': 55.0, 'Tom': 30.2, 'Alex': 49.4, 'Jordan': 21.1, 'Robert': 41.8, 'Kim': 37.0, 'Alice': 56.6}
Deleting Mary...
 {'Ted': 35.5, 'Bob': 15.0, 'Sally': 45.5, 'Sara': 55.0, 'Tom': 30.2, 'Alex': 49.4, 'Jordan': 21.1, 'Robert': 41.8, 'Kim': 37.0, 'Alice': 56.6}

'''