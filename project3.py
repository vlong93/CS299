# Author: Vivian Long
# Assignment: Project 3
# Completed:

print("Fahrenheit (\u00b0F) \t Celsius (\u00b0C) \t Description")
print('{:>14}'.format("-459.67 \u00b0F"), "\t", '{:>15}'.format("-273.15 \u00b0C"),
      "\t", '{:<30}'.format("absolute zero temperature"))
for i in range(-50, 31, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")
print('{:>14}'.format("32 \u00b0F"), "\t", '{:>15}'.format("0 \u00b0C"),
      "\t", '{:<30}'.format("freezing/melting point of water"))
for i in range(40, 61, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")
print('{:>14}'.format("70 \u00b0F"), "\t", '{:>15}'.format("21.11 \u00b0C"),
      "\t", '{:<30}'.format("room temperature"))
for i in range(80, 91, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")
print('{:>14}'.format("98.6 \u00b0F"), "\t", '{:>15}'.format("37 \u00b0C"),
      "\t", '{:<30}'.format("average body temperature"))
for i in range(100, 201, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")
print('{:>14}'.format("212 \u00b0F"), "\t", '{:>15}'.format("100 \u00b0C"),
      "\t", '{:<30}'.format("boiling point of water"))