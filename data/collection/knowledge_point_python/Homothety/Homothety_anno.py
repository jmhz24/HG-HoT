def Homothety_proportion(proportion, segment_1=None, segment_2=None):
    # This function uses the property that all corresponding sides have the same proportional relationship.
    if segment_1:
        return segment_1 * (1 / proportion)
    else:
        return segment_2 * proportion

def Homothety_equal_angle(angle):
    # This function uses the property that similar figures are identical in terms of angles, meaning the measure of each angle in one figure is the same as the measure of the corresponding angle in the other figure
    return angle