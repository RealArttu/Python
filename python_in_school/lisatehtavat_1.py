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

#distance()

# Celsius to fahrenheit converter
def celsius_to_fahrenheit():
    celsius = int(input("Enter °C: ")) # User input celsius
    fahrenheit = celsius * 1.8 + 32 # Calculate fahrenheit
    print(f"{celsius}°C is {fahrenheit}°F") # Output the result

celsius_to_fahrenheit()

