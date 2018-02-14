# Author: Vivian Long
# Assignment: Exam 2
# Date: 2/14/2018


def occupancyRate(occupied, totalRooms):
    occRate = occupied / totalRooms
    return occRate


def main():
    floors = int(input("Enter number of floors: "))
    totalRooms = 0
    totalOccupied = 0

    for i in range(floors):
        rooms = int(input("Enter number of rooms on floor: "))
        totalRooms += rooms
        occupied = int(input("Enter number of occupied rooms on floor: "))
        totalOccupied += occupied

    rate = occupancyRate(totalOccupied, totalRooms)

    print("The hotel has", totalRooms, "rooms,", totalOccupied,
          "room are occupied, and the occupancy rate is", rate, end='.')


def getNumbers(numFloors):
    numRooms = 0
    numOccupied = 0
    if 0 < numFloors <= 100:
        try:
            for i in range(numFloors):
                rooms = int(input("Enter number of rooms on floor: "))
                if 0 < rooms <= 200:
                    numRooms += rooms
                else:
                    print("Invalid input.")
                    return
                occupied = int(input("Enter number of occupied rooms on floor: "))
                if occupied <= rooms:
                    numOccupied += occupied
                else:
                    print("Invalid input.")
                    return

            return numRooms, numOccupied

        except ValueError:
            print("Enter a valid number.")
            return
    else:
        print("Invalid value for number of floors. Try again.")
        return


main()
