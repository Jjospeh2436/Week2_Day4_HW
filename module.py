import math
def HouseSq():
    length = input("What is the length of the house? ")
    width = input("what is the width of the house? ")
    area = length * width
    return area

def Circumference():
    radius = input("what is the radius of the circle? ")
    circum = 2*math.pi()*radius
    return circum