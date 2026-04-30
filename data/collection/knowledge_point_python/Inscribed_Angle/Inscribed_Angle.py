def Inscribed_Angle_same_arc_equal_angles(angle):
    return angle

def Inscribed_Angle_diameter_angle():
    return 90

def Inscribed_Angle_supplementary_angles_90(angle):
    return 90 - angle

def Inscribed_Angle_supplementary_angles_180(angle):
    return 180 - angle

def Inscribed_Angle_relationship_with_central_angle(central_angle=None, inscribed_angle=None):
    if central_angle:
        return 1/2 * central_angle
    else:
        return 2 * inscribed_angle