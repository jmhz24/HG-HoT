import math

def Sector_area_degrees(radius, degrees):
    # This function uses the property that the area of a sector can be calculated using the following formulas: Area = (π × radius squared × central angle in degrees) ÷ 360.
    area = (math.pi * radius ** 2 * degrees) / 360
    return area

def Sector_area_radians(radius, radians):
    # This function uses the property that the area of a sector can be calculated using the following formulas: Area = (radius squared × central angle in radians) ÷ 2.
    area = (radius ** 2 * radians) / 2
    return area

def Sector_area_arc_length(radius, arc_length):
    # This function uses the property that the area of a sector can be calculated using the following formulas: Area = (radius × arc length) ÷ 2.
    area = (radians * arc_length) / 2
    return area