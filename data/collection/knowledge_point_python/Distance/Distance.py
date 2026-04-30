import math
import sympy as sp

def Distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def Distance_line(point, line_coefficients):
    x0, y0 = point
    A, B, C = line_coefficients
    distance = sp.Abs(A*x0 + B*y0 + C) / sp.sqrt(A**2 + B**2)
    return distance.evalf()