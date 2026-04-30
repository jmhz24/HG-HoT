def Triangle_Incenter_bisect_angle(whole_angle=None, half_angle=None):
    # This function uses the property that the angle bisectors of the three interior angles of a triangle meet at a point. This point is called the incenter of the triangle.
    if whole_angle:
        return (1 / 2) * whole_angle
    else:
        return 2 * half_angle

def Triangle_Incenter_equal_distance(line):
    # This function uses the property that the distance from the incenter to each of the three sides of the triangle is equal.
    return line

def Triangle_Incenter__perpendicular():
    # This function uses the property that the line connecting the incenter of a triangle to each side of the triangle is perpendicular to the corresponding side.
    return 90
