import math

def Projection_Theorem(right_angle_side=None, hypotenuse=None):
    if right_angle_side:
        return right_angle_side ** 2 / 2
    else:
        return math.sqrt(2 * hypotenuse)