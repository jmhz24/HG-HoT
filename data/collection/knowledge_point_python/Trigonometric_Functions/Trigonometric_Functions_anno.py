import math

def Trigonometric_Functions_sin(degree):
    # Function to calculate the sine of an angle in degree
    return math.sin(math.radians(degree))

def Trigonometric_Functions_cos(degree):
    # Calculate cosine of an angle in degree
    return math.cos(math.radians(degree))

def Trigonometric_Functions_tan(degree):
    # Calculate tangent of an angle in degree
    return math.tan(math.radians(degree))

def Trigonometric_Functions_arcsin(value):
    # Calculate arc sine (inverse sine) and return in degrees
    if -1 <= value <= 1:
        return math.degrees(math.asin(value))
    else:
        raise ValueError("Input must be in the range [-1, 1]")

def Trigonometric_Functions_arccos(value):
    # Calculate arc cosine (inverse cosine) and return in degrees
    if -1 <= value <= 1:
        return math.degrees(math.acos(value))
    else:
        raise ValueError("Input must be in the range [-1, 1]")

def Trigonometric_Functions_arctan(value):
    # Calculate arc tangent (inverse tangent) and return in degrees
    return math.degrees(math.atan(value))