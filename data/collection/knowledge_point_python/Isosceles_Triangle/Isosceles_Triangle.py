def Isosceles_Triangle_equal_line(line):
    return line

def Isosceles_Triangle_equal_angle(angle):
    return angle

def Isosceles_Triangle_perpendicular():
    return 90

def Isosceles_Triangle_supplementary_angles_90(angle):
    return 90 - angle

def Isosceles_Triangle_bisector(whole_angle=None, half_angle=None):
    if whole_angle:
        return (1 / 2) * whole_angle
    else:
        return 2 * half_angle

def Isosceles_Triangle_exterior_angle(exterior_angle_of_vertex_angle):
    return (1 / 2) * exterior_angle_of_vertex_angle

def Isosceles_Triangle_calculate_base_angle(vertex_angle):
    return (1 / 2) * (180 - vertex_angle)

def Isosceles_Triangle_calculate_vertex_angle(base_angle):
    return 180 - (2 * base_angle)