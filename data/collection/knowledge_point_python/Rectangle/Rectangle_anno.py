def Rectangle_equal_line(line):
    # This function uses the property that in a rectangle, opposite sides are equal in length and the two diagonals of a rectangle are equal in length.
    return line

def Rectangle_perpendicular():
    # This function uses the property that all four interior angles of a rectangle are right angles, meaning each angle measures 90 degrees.
    return 90

def Rectangle_bisect(whole_line=None, half_line=None):
    # This function uses the property that in a rectangle, the relationship between the bisected line and the entire line.
    if whole_line:
        return (1 / 2) * whole_line
    else:
        return 2 * half_line

def Rectangle_calculate_area(length, width):
    # This function uses the property that calculate the area of the rectangle given the length and width.
    return length * width

def Rectangle_calculate_length_or_width_based_area(area, length_or_width):
    # This function uses the property that calculate the width (or length) of a rectangle given its area and length (or width).
    return area / length_or_width

def Rectangle_calculate_perimeter(length, width):
    # This function uses the property that calculate the perimeter of the rectangle given the length and width.
    return 2 * (length + width)

def Rectangle_calculate_length_or_width_based_perimeter(perimeter, length_or_width):
    # This function uses the property that calculate the width (or length) of a rectangle given its perimeter and length (or width).
    return (1 / 2) * perimeter - length_or_width