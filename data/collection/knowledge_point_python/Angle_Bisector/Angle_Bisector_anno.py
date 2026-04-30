def Angle_Bisector_bisect_angle(whole_angle=None, half_angle=None):
    #This function uses the property that the relationship between the angles divided by an angle bisector.
    if whole_angle:
        return (1 / 2) * whole_angle
    else:
        return 2 * half_angle

def Angle_Bisector_equal_angle(angle):
    #This function uses the property that the two angles divided by an angle bisector are equal.
    return angle