import math

def Right_Triangle_pythagorean_theorem_add(leg_a=None, leg_b=None):
    # This function uses the property that pythagorean theorem, the sum of the squares of the two legs (right-angled sides) of a right triangle is equal to the square of its hypotenuse.
    return math.sqrt(leg_a ** 2 + leg_b ** 2)

def Right_Triangle_pythagorean_theorem_minus(leg_a=None, hypotenuse_c=None):
    # This function uses the property that pythagorean theorem, the sum of the squares of the two legs (right-angled sides) of a right triangle is equal to the square of its hypotenuse.
    return math.sqrt(hypotenuse_c ** 2 - leg_a ** 2)