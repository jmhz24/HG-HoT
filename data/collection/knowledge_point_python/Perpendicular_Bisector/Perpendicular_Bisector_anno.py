def Perpendicular_Bisector_perpendicular():
    # This function uses the property that a perpendicular bisector intersects another line or line segment at a 90-degree angle, meaning the angle formed at their point of intersection is a right angle.
    return 90

def Perpendicular_Bisector_supplementary_angles_90(angle):
    # This function uses the property that in a right-angled triangle formed by a perpendicular bisector and the other sides of the triangle, the sum of the two angles other than the right angle equals 90 degrees.
    return 90 - angle

def Perpendicular_Bisector_equal_line(line):
    # This function uses the property that two lines that are bisected by a perpendicular bisector are equal in length.
    return line

def Perpendicular_Bisector_bisect(whole_line=None, half_line=None):
    # This function uses the property that the relationship between lines that are parallel to a perpendicular bisector.
    if whole_line:
        return (1 / 2) * whole_line
    else:
        return 2 * half_line