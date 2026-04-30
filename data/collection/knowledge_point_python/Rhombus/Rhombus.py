def Rhombus_equal_line(line):
    return line

def Rhombus_perpendicular():
    return 90

def Rhombus_supplementary_angles_90(angle):
    return 90 - angle

def Rhombus_equal_angle(angle):
    return angle

def Rhombus_bisect(whole_line_angle=None, half_line_angle=None):
    if whole_line_angle:
        return (1 / 2) * whole_line_angle
    else:
        return 2 * half_line_angle