# Author: Vivian Long
# Assignment: Lab 6
# Completed: 2/13/2018

from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv

try:
    # Task 2
    infilename = askopenfilename()
    outfilename = asksaveasfilename()

    infile = open(infilename, "r")
    outfile = open(outfilename, "w")

    for line in infile:
        line = line.rsplit()

        # Task 1
        for i in range(len(line)):
            fahr = float(line[i])
            celc = fahr * (9 / 5) + 32
            # print(i + 1, ("%.2f" % round(celc, 2)))
            outfile.write(str(i + 1) + ": " + str("%.2f" % celc) + "\n")

    infile.close()
    outfile.close()

    # Task 3
    outfile = open("oceantemps.txt", "w")
    with open("ocean_temp.csv", "r") as csvfile:
        oceantemp = csv.reader(csvfile, delimiter=',')

        for row in oceantemp:
            outfile.write(row[0] + "\n")

    outfile.close()

except IOError:
    print("Error: File not found.")

except ValueError as exception:
    print("Error:", str(exception))
