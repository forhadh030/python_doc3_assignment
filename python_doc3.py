import Area
import Circumference

def your_input():
    response = input("Hello user, please type 'h' for house or 'c' for circle: ")

    if response == 'h':
        print("Hello Owner, I am here to tell you the square footage of your house!\n")
        length = int(input("Please enter the length of your house: "))
        width = int(input("Please enter the width of your house: "))

        return Area.house(length, width)

    elif response == 'c':
        print("Hello Stranger, I am here to tell you the circumference of a cirle!\n")
        radius = int(input("Please enter the radius of the cirlce: "))

        return Circumference.circle(radius)
    
    else:
        print("Please select the option listed")

print(your_input())