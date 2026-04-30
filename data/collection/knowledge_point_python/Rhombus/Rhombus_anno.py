def Rhombus_equal_line(line):
    # This function uses the property that a rhombus is a type of quadrilateral where all four sides are of equal length and the diagonals of a rhombus bisect each other, and the segments they divide are equal in length.
    return line

def Rhombus_perpendicular():
    # This function uses the property that the two diagonals of a rhombus intersect each other at right angles.
    return 90

def Rhombus_supplementary_angles_90(angle):
    # This function uses the property that in a right triangle formed by the diagonals of a rhombus and its other sides, the sum of the angles other than the right angle equals 90 degrees.
    return 90 - angle

def Rhombus_equal_angle(angle):
    # This function uses the property that the opposite angles of a rhombus are equal.
    return angle

def Rhombus_bisect(whole_line_angle=None, half_line_angle=None):
    # This function uses the property that in a rhombus, the relationship between the bisected angles and lines, and the entire angles and lines.
    if whole_line_angle:
        return (1 / 2) * whole_line_angle
    else:
        return 2 * half_line_angle