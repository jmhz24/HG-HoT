def Parallel_Lines_Proportion(proportion, segment_1=None, segment_2=None):
    if segment_1:
        return segment_1 * (1 / proportion)
    else:
        return segment_2 * proportion