def Inscribed_Angle_same_arc_equal_angles(angle):
    #This function uses the property that inscribed angles subtending the same arc are equal.
    return angle

def Inscribed_Angle_diameter_angle():
    #This function uses the property that the inscribed angle subtended by a diameter is a right angle.
    return 90

def Inscribed_Angle_supplementary_angles_90(angle):
    # This function uses the property that when a point on a circle is connected to both ends of a diameter, the angle formed is a right inscribed angle. In this right triangle, the sum of the two angles other than the right angle adds up to 90 degrees.
    return 90 - angle

def Inscribed_Angle_supplementary_angles_180(angle):
    #This function uses the property that in a cyclic quadrilateral, the opposite angles are supplementary.
    return 180 - angle

def Inscribed_Angle_relationship_with_central_angle(central_angle=None, inscribed_angle=None):
    #This function uses the property that the degree measure of a central angle is twice the degree measure of any inscribed angle subtending the same arc.
    if central_angle:
        return 1/2 * central_angle
    else:
        return 2 * inscribed_angle