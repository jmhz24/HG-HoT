def Right_Triangle_Hypotenuse_Median(hypotenuse=None, median=None):
    # This function uses the property that in a right triangle, the length of the median on the hypotenuse is equal to half the length of the hypotenuse.
    if hypotenuse:
        return (1 / 2) * hypotenuse
    else:
        return 2 * median