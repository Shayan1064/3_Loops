print("1: For Square")
print("2: For Triangle")
print("3: For Rectangle")

choice = int(input("Enter Your choice: "))

# Square
if choice == 1:
    n = int(input("Enter size of square: "))
    for i in range(n):
        print("* " * n)

# Triangle (Half Pyramid)
elif choice == 2:
    n = int(input("Enter height of triangle: "))
    for i in range(1, n+1):
        print("* " * i)

# Rectangle
elif choice == 3:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    for i in range(rows):
        print("* " * cols)

else:
    print("Invalid choice!")
