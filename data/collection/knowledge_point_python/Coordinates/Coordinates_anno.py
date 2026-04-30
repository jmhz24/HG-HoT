import math
import sympy as sp

def Coordinates_calculate_slope(point1, point2):
    # Calculate the slope.
    x1, y1 = point1
    x2, y2 = point2
    return (y2 - y1) / (x2 - x1)

def Coordinates_calculate_Midpoint(point1, point2):
    # Calculate the midpoint between two points.
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def Coordinates_distance_line(point, line_coefficients):
    # Calculate the shortest distance between a point and a line in 2D. The line is given in the general form Ax + By + C = 0.
    x0, y0 = point
    A, B, C = line_coefficients

    # Using the distance formula d = |Ax0 + By0 + C| / sqrt(A^2 + B^2)
    distance = sp.Abs(A*x0 + B*y0 + C) / sp.sqrt(A**2 + B**2)
    return distance.evalf()