def Equilateral_Triangle_equal_line(line):
    # This function uses the property that in an equilateral triangle, all three sides are of equal length.
    return line

def Equilateral_Triangle_equal_angle():
    # This function uses the property that in an equilateral triangle, all the interior angles are equal, with each angle measuring 60 degrees.
    return 60

def Equilateral_Triangle_perpendicular():
    # This function uses the property that an equilateral triangle has a line of symmetry that passes through the vertex and is perpendicular to the base.
    return 90

def Equilateral_Triangle_supplementary_angles_90(angle):
    # This function uses the property that in a right-angled triangle formed by a perpendicular bisector and the other sides of the triangle, the sum of the two angles other than the right angle equals 90 degrees.
    return 90 - angle

def Equilateral_Triangle_bisector(whole_angle=None, half_angle=None):
    # This function uses the property that in an equilateral triangle, the median to the base, which is also the perpendicular bisector of the base, serves as the angle bisector of the vertex angle.
    if whole_angle:
        return (1 / 2) * whole_angle
    else:
        return 2 * half_angle