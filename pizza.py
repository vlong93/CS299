# Pizza Ordering


def getSize():
    count = 0
    print("Choose the size of the pizza (10, 12, 14 or 16): ")
    print("""
    Pizza Size (inches) \tCost
    10" \t$10.99
    12" \t$12.99
    14" \t$14.99
    16" \t$16.99
    """)

    while count < 3:
        size = input().lower()
        if size != '10' and size != '12' and size != '14' and size != '16':
            print("Invalid choice. Try again: ")
            count += 1
        else:
            return size
    else:
        print("Sorry, try again later.")
        return -1


def getCrust():
    print("Choose the crust of the pizza (1, 2, or 3): ")
    print("""
    1. Hand-tossed
    2. Thin crust (extra $1)
    3. Deep dish (extra $2)
    """)
    crust = input()

    if crust == '1':
        upcharge = 0
    elif crust == '2':
        upcharge = 1
    elif crust == '3':
        upcharge = 2
    else:
        upcharge = 0

    return upcharge


def applyDiscount():
    coupon = input("Please enter a coupon code if any: ")
    if coupon == "Holiday10":
        discount = 0.1
    elif coupon == "Winter20":
        discount = 0.2
    elif coupon == "VIPmax":
        discount = 0.25
    else:
        discount = 0

    return discount


def cost(size, upcharge, discount, taxRate = 0.085):
    total = (float(size) + 0.99 + float(upcharge)) * (1 - float(discount)) * (1 + taxRate)

    return total


def main():
    size = getSize()
    upcharge = getCrust()
    discount = applyDiscount()
    try:
        taxRate = float(input("Enter the tax rate if not 8.5%: "))
    except ValueError:
        taxRate = 0.085

    print("Your total cost is: $", round(cost(size, upcharge, discount, taxRate), 2))

main()
