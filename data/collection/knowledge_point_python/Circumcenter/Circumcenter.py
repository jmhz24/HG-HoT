def Circumcenter_perpendicular():
    return 90

def Circumcenter_supplementary_angles_90(angle):
    return 90 - angle

def Circumcenter_equal_line(line):
    return line

def Circumcenter_bisect(whole_line=None, half_line=None):
    if whole_line:
        return (1 / 2) * whole_line
    else:
        return 2 * half_line

def Circumcenter_equidistant(line):
    return line