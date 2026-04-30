import math

def Sector_area_degrees(radius, degrees):
    area = (math.pi * radius ** 2 * degrees) / 360
    return area

def Sector_area_radians(radius, radians):
    area = (radius ** 2 * radians) / 2
    return area

def Sector_area_arc_length(radius, arc_length):
    area = (radians * arc_length) / 2
    return area