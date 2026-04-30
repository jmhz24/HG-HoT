import math

def Right_Triangle_pythagorean_theorem_add(leg_a=None, leg_b=None):
    return math.sqrt(leg_a ** 2 + leg_b ** 2)

def Right_Triangle_pythagorean_theorem_minus(leg_a=None, hypotenuse_c=None):
    return math.sqrt(hypotenuse_c ** 2 - leg_a ** 2)