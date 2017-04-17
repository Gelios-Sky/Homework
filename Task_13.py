cathetet_1=int(input("Enter value of first cathet"))
cathetet_2=int(input('Enter value of second cathet'))
def triagle_square_perimeter(cathetet_1,cathetet_2):
    import math
    hypotenuse=(math.sqrt(cathetet_1 * cathetet_1 + cathetet_2 * cathetet_2))
    triagle_square=(cathetet_1*cathetet_2)/2
    triale_perimeter=hypotenuse+cathetet_1+cathetet_2
    return triagle_square,triale_perimeter
square,perimeter=triagle_square_perimeter(cathetet_1, cathetet_2)
#print (triagle_square_perimeter(4,6))
#print(int(input("Enter value of catethets")))
#print(triagle_square_perimeter (int(input('Enter value of cathets'),int(input("")))))
#cathets=int(input('Enter value of catets'))
#triagle_square_perimeter(int(input("Enter value of first cathet"))),int(input("Enter value of second cathet"))
#print(int(input("Enter value of second cathet")))
print("Square and perimeter of triangle with sides %d, %d is equal to %.2f, %.2f" % (cathetet_1, cathetet_2, square, perimeter))