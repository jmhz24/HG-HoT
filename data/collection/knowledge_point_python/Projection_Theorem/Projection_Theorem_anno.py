import math

def Projection_Theorem(right_angle_side=None, hypotenuse=None):
    # This function uses the property that in a right-angled triangle, each leg is the geometric mean between the projection of that leg on the hypotenuse and the hypotenuse itself.
    if right_angle_side:
        return right_angle_side ** 2 / 2
    else:
        return math.sqrt(2 * hypotenuse)