def Golden_Ratio_proportion(proportion, segment_1=None, segment_2=None):
    # This function uses the property that all corresponding sides have the same proportional relationship.
    if segment_1:
        return segment_1 * (1 / proportion)
    else:
        return segment_2 * proportion