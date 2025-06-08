def upper_triangle(rows):
    print("Upper Triangle:")
    for i in range(rows):
        for j in range(rows):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def lower_triangle(rows):
    print("Lower Triangle:")
    for i in range(rows):
        for j in range(rows):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()

def pyramid(rows):
    print("Pyramid:")
    for i in range(rows):
      
        for j in range(rows - i - 1):
            print(" ", end=" ")
       
        for k in range(2 * i + 1):
            print("*", end=" ")
        print()
    print()

# Main Program:
rows = int(input("Enter number of rows: "))
print()
upper_triangle(rows)
lower_triangle(rows)
pyramid(rows)
