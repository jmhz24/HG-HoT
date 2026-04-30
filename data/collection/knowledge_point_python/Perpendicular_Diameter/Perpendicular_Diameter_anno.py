def Perpendicular_Diameter_perpendicular():
    # This function uses the property that a diameter or radius is perpendicular to a chord.
    return 90

def Perpendicular_Diameter_supplementary_angles_90(angle):
    # This function uses the property that in a right triangle formed by a diameter or radius perpendicular to a chord, and the chord along with another radius, the sum of the two angles other than the right angle is 90 degrees.
    return 90 - angle

def Perpendicular_Diameter_equal_line_arc(line_arc):
    # This function uses the property that a chord or an arc that is perpendicular to a diameter or radius is bisected by it.
    return line_arc

def Perpendicular_Diameter_equal_angle(inscribed_angle_or_central_angle):
    # This function uses the property that the two angles at the inscribed angles or the two central angles corresponding to a perpendicular diameter are equal.
    return inscribed_angle_or_central_angle

def Perpendicular_Diameter_bisect(chord_arc=None, half_chord_arc=None):
    # This function uses the property that in a circle, the diameter that is perpendicular to a chord bisects the chord and its arc.
    if chord_arc:
        return (1 / 2) * chord_arc
    else:
        return 2 * half_chord_arc