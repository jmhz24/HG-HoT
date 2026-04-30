import math

def Calculate_Cone_volume(radius, height):
    return (1 / 3) * math.pi * radius**2 * height

def Calculate_Cone_base_area(radius):
    return math.pi * radius**2

def Calculate_Cone_lateral_surface_area(radius, slant):
    return math.pi * radius * slant

def Calculate_Cone_surface_area(radius, slant):
    return math.pi * radius**2 + math.pi * radius * slant