def Right_Triangle_30_Angle(hypotenuse=None, opposite=None):
    # This function uses the property that the length of the side opposite the 30 degree Angle is half the length of the hypotenuse.
    if hypotenuse:
        return (1 / 2) * hypotenuse
    else:
        return 2 * opposite