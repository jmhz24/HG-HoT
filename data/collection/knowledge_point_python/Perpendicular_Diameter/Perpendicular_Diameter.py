def Perpendicular_Diameter_perpendicular():
    return 90

def Perpendicular_Diameter_supplementary_angles_90(angle):
    return 90 - angle

def Perpendicular_Diameter_equal_line_arc(line_arc):
    return line_arc

def Perpendicular_Diameter_equal_angle(inscribed_angle_or_central_angle):
    return inscribed_angle_or_central_angle

def Perpendicular_Diameter_bisect(chord_arc=None, half_chord_arc=None):
    if chord_arc:
        return (1 / 2) * chord_arc
    else:
        return 2 * half_chord_arc