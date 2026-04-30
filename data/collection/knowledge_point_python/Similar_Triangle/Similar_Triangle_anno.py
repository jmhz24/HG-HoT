def Similar_Triangles_proportion(proportion, segment_1=None, segment_2=None):
    #This function uses the property that the corresponding sides of similar triangles are proportional.
    if segment_1:
        return segment_1 * (1 / proportion)
    else:
        return segment_2 * proportion

def Similar_Triangles_equal_angle(angle):
    #This function uses the property that in two similar triangles, all corresponding angles are equal.
    return angle