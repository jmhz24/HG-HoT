def Parallelogram_equal_line(line):
    #This function uses the property that in a parallelogram, each pair of opposite sides is equal in length and the diagonals of a parallelogram bisect each other.
    return line

def Parallelogram_equal_angle(angle):
    #This function uses the property that in a parallelogram, the opposite angles (the angles that are across from each other) are equal.
    return angle

def Parallelogram_supplementary_angles_180(angle):
    #This function uses the property that in a parallelogram, any two consecutive interior angles are supplementary, meaning their sum equals 180 degrees.
    return 180 - angle

def Parallelogram_diagonals_bisect(diagonal=None, half_diagonal=None):
    #This function uses the property that the diagonals of a parallelogram bisect each other.
    if diagonal:
        return (1 / 2) * diagonal
    else:
        return 2 * half_diagonal
