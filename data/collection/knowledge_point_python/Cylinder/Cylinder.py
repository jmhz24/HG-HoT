import math

def Calculate_Cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def Calculate_Cylinder_base_area(radius):
    return math.pi * radius**2

def Calculate_Cylinder_lateral_area(radius, height):
    return 2 * math.pi * radius * height

def Calculate_Cylinder_surface_area(radius, height):
    return 2 * math.pi * radius**2 + 2 * math.pi * radius * height