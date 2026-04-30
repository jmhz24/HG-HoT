import math

def Right_Triangle_pythagorean_theorem_add(leg_a=None, leg_b=None):
    # This function uses the property that pythagorean theorem, the sum of the squares of the two legs (right-angled sides) of a right triangle is equal to the square of its hypotenuse.
    return math.sqrt(leg_a ** 2 + leg_b ** 2)

def Right_Triangle_pythagorean_theorem_minus(leg_a=None, hypotenuse_c=None):
    # This function uses the property that pythagorean theorem, the sum of the squares of the two legs (right-angled sides) of a right triangle is equal to the square of its hypotenuse.
    return math.sqrt(hypotenuse_c ** 2 - leg_a ** 2)

def Right_Triangle_supplementary_angles_90(angle):
    # This function uses the property that in a right triangle, the sum of the two angles other than the right angle equals 90 degrees.
    return 90 - angle

def Right_Triangle_medians(hypotenuse=None, median=None):
    # This function uses the property that in a right triangle, the length of the segment from the midpoint of the hypotenuse to the right-angle vertex is half the length of the hypotenuse.
    if hypotenuse:
        return (1 / 2) * hypotenuse
    else:
        return 2 * median