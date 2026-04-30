import math
import sympy as sp

def Coordinates_calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (y2 - y1) / (x2 - x1)

def Coordinates_calculate_Midpoint(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def Coordinates_distance_line(point, line_coefficients):
    x0, y0 = point
    A, B, C = line_coefficients
    distance = sp.Abs(A*x0 + B*y0 + C) / sp.sqrt(A**2 + B**2)
    return distance.evalf()