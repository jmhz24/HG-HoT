import math

def Trigonometric_Functions_sin(degree):
    return math.sin(math.radians(degree))

def Trigonometric_Functions_cos(degree):
    return math.cos(math.radians(degree))

def Trigonometric_Functions_tan(degree):
    return math.tan(math.radians(degree))

def Trigonometric_Functions_arcsin(value):
    if -1 <= value <= 1:
        return math.degrees(math.asin(value))
    else:
        raise ValueError("Input must be in the range [-1, 1]")

def Trigonometric_Functions_arccos(value):
    if -1 <= value <= 1:
        return math.degrees(math.acos(value))
    else:
        raise ValueError("Input must be in the range [-1, 1]")

def Trigonometric_Functions_arctan(value):
    return math.degrees(math.atan(value))