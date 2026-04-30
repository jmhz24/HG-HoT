def Equilateral_Triangle_equal_line(line):
    return line

def Equilateral_Triangle_equal_angle():
    return 60

def Equilateral_Triangle_perpendicular():
    return 90

def Equilateral_Triangle_supplementary_angles_90(angle):
    return 90 - angle

def Equilateral_Triangle_bisector(whole_angle=None, half_angle=None):
    if whole_angle:
        return (1 / 2) * whole_angle
    else:
        return 2 * half_angle