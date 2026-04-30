def Perpendicular_Bisector_perpendicular():
    return 90

def Perpendicular_Bisector_supplementary_angles_90(angle):
    return 90 - angle

def Perpendicular_Bisector_equal_line(line):
    return line

def Perpendicular_Bisector_bisect(whole_line=None, half_line=None):
    if whole_line:
        return (1 / 2) * whole_line
    else:
        return 2 * half_line