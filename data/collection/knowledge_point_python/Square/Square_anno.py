import math

def Square_equal_line(line):
    # This function uses the property that all sides of a square are equal in length; the diagonals are equal in length, lines bisected by a perpendicular bisector are equal in length.
    return line

def Square_equal_angle(angle):
    # This function uses the property that all angles of a square are equal, the angles bisected by an angle bisector are equal.
    return angle

def Square_perpendicular():
    # This function uses the property that every angle in a square is a right angle; the diagonals of a square are perpendicular to each other.
    return 90

def Square_supplementary_angles_90(angle):
    # This function uses the property that in a right triangle formed by the diagonals of a square and its other sides, the sum of the angles other than the right angle equals 90 degrees.
    return 90 - angle

def Square_bisect(whole_line_angle=None, half_line_angle=None):
    # This function uses the property that the in a square, the relationship between the bisected angles and lines, and the entire angles and lines.
    if whole_line_angle:
        return (1 / 2) * whole_line_angle
    else:
        return 2 * half_line_angle

def Square_calculate_area(side_length):
    # This function uses the property that the in a square, calculate the area of a square given its side length.
    return side_length ** 2

def Square_calculate_side_length_based_area(area):
    # This function uses the property that the in a square, calculate the side length of a square given its area.
    return math.sqrt(area)

def Square_calculate_perimeter(side_length):
    # This function uses the property that calculate the perimeter of the square given the side length.
    return 4 * side_length

def Square_calculate_side_length_based_perimeter(perimeter):
    # This function uses the property that calculate the side length of a square given its perimeter.
    return (1 / 4) * perimeter