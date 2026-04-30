import math

def Square_equal_line(line):
    return line

def Square_equal_angle(angle):
    return angle

def Square_perpendicular():
    return 90

def Square_supplementary_angles_90(angle):
    return 90 - angle

def Square_bisect(whole_line_angle=None, half_line_angle=None):
    if whole_line_angle:
        return (1 / 2) * whole_line_angle
    else:
        return 2 * half_line_angle

def Square_calculate_area(side_length):
    return side_length ** 2

def Square_calculate_side_length_based_area(area):
    return math.sqrt(area)

def Square_calculate_perimeter(side_length):
    return 4 * side_length

def Square_calculate_side_length_based_perimeter(perimeter):
    return (1 / 4) * perimeter