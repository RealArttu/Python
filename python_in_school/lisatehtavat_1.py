from math import sqrt


def distance():
    # File lisatehtavat_1, Tehtava 1
    # Ask for user input for the x,y values
    x1 = int(input("Enter x1: "))

    y1 = int(input("Enter y1: "))

    x2 = int(input("Enter x2: "))

    y2 = int(input("Enter y2: "))

    # Calculate the distance between the two points
    distance = sqrt((x2-x1)**2 + (y2-y1)**2)

    # Output the distance
    print(distance)

distance()

# Code that doesn't work lol§
def celsius_to_fahrenheit():
    celsius = int(input("Enter °C: ")) # User input celsius
    fahrenheit = celsius/100 # First part to convert celsius to fahrenheit
    result = fahrenheit - 32/180 # Second part to convert celsius to fahrenheit
    print(f"{celsius}°C is {result}°F") # Output the result

#celsius_to_fahrenheit()



