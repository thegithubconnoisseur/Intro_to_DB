positive_integer = int(input("Enter the size of the pattern: "))

i = 1

while i <= positive_integer:

    for values in range(positive_integer):
        print("*", end = "")
    print()
    i += 1