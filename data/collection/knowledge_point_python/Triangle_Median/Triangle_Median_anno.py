def Triangle_Median_relationship_with_third_side(third_line, median_line):
    #This function uses the property that the length of the median in a triangle is half the length of the third side.
    if third_line:
        return (1 / 2) * third_line
    else:
        return 2 * median_line