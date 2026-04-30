def Parallel_Lines_Proportion(proportion, segment_1=None, segment_2=None):
    #This function uses the property that when two lines are intersected by a set of parallel lines, the corresponding segments cut off on these lines are proportional in length.
    if segment_1:
        return segment_1 * (1 / proportion)
    else:
        return segment_2 * proportion