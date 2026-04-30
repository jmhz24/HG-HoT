def Isosceles_Triangle_equal_line(line):
    # This function uses the property that in an isosceles triangle, the lengths of the two legs (usually referring to the two sides other than the base) are equal
    return line

def Isosceles_Triangle_equal_angle(angle):
    # This function uses the property that in an isosceles triangle, the base angles (the angles formed at the base where the two equal sides intersect) are equal and angle bisector divides an angle into two parts of equal measure.
    return angle

def Isosceles_Triangle_perpendicular():
    # This function uses the property that an isosceles triangle has a line of symmetry that passes through the vertex and is perpendicular to the base.
    return 90

def Isosceles_Triangle_supplementary_angles_90(angle):
    # This function uses the property that in a right triangle formed by the perpendicular bisector of the base of an isosceles triangle and the other sides of the triangle, the sum of the two angles other than the right angle equals 90 degrees.
    return 90 - angle

def Isosceles_Triangle_bisector(whole_angle=None, half_angle=None):
    # This function uses the property that in an isosceles triangle, the median to the base, which is also the perpendicular bisector of the base, serves as the angle bisector of the vertex angle.
    if whole_angle:
        return (1 / 2) * whole_angle
    else:
        return 2 * half_angle

def Isosceles_Triangle_exterior_angle(exterior_angle_of_vertex_angle):
    # This function uses the property that in an isosceles triangle, the base angle (the angle between a leg and the base) is half of the exterior angle of the vertex angle (the angle between the two legs).
    return (1 / 2) * exterior_angle_of_vertex_angle

def Isosceles_Triangle_calculate_base_angle(vertex_angle):
    # This function uses the property that in an isosceles triangle, given the vertex angle, calculate the base angles.
    return (1 / 2) * (180 - vertex_angle)

def Isosceles_Triangle_calculate_vertex_angle(base_angle):
    # This function uses the property that in an isosceles triangle, given one base angle, calculate the vertex angle.
    return 180 - (2 * base_angle)