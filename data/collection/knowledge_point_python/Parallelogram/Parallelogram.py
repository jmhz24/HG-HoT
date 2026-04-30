def Parallelogram_equal_line(line):
    return line

def Parallelogram_equal_angle(angle):
    return angle

def Parallelogram_supplementary_angles_180(angle):
    return 180 - angle

def Parallelogram_diagonals_bisect(diagonal=None, half_diagonal=None):
    if diagonal:
        return (1 / 2) * diagonal
    else:
        return 2 * half_diagonal