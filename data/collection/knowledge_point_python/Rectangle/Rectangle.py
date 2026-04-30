def Rectangle_equal_line(line):
    return line

def Rectangle_perpendicular():
    return 90

def Rectangle_bisect(whole_line=None, half_line=None):
    if whole_line:
        return (1 / 2) * whole_line
    else:
        return 2 * half_line

def Rectangle_calculate_area(length, width):
    return length * width

def Rectangle_calculate_length_or_width_based_area(area, length_or_width):
    return area / length_or_width

def Rectangle_calculate_perimeter(length, width):
    return 2 * (length + width)

def Rectangle_calculate_length_or_width_based_perimeter(perimeter, length_or_width):
    return (1 / 2) * perimeter - length_or_width