def Circumcenter_perpendicular():
    # This function uses the property that the circumcenter of a triangle is the point where the perpendicular bisectors of the sides of the triangle intersect.
    return 90

def Circumcenter_supplementary_angles_90(angle):
    # This function uses the property that in a right-angled triangle formed by a perpendicular bisector and the other sides of the triangle, the sum of the two angles other than the right angle equals 90 degrees.
    return 90 - angle

def Circumcenter_equal_line(line):
    # This function uses the property that the circumcenter of a triangle is the point where two lines that are bisected by a perpendicular bisector are equal in length.
    return line

def Circumcenter_bisect(whole_line=None, half_line=None):
    # This function uses the property that the circumcenter of a triangle is the point where the relationship between lines that are bisected to a perpendicular bisector.
    if whole_line:
        return (1 / 2) * whole_line
    else:
        return 2 * half_line

def Circumcenter_equidistant(line):
    # This function uses the property that the circumcenter of a triangle is equidistant from all three vertices of the triangle.
    return line