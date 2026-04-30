import math

def Calculate_Cone_volume(radius, height):
    #The volume of a cone can be calculated using the following formula: V = 1/3πr²h, where V is the volume, r is the radius of the base, and h is the height of the cone.
    return (1 / 3) * math.pi * radius**2 * height

def Calculate_Cone_base_area(radius):
    #The base area of a cone is calculated using the formula: Base Area = πr².
    return math.pi * radius**2

def Calculate_Cone_lateral_surface_area(radius, slant):
    #The lateral surface area of a cone refers to the surface area of the conical surface formed by extending around the circumference of the base of the cone. The formula for calculating it is: Lateral Area = πrl, where Lateral Area is the lateral surface area, r is the radius of the base, and l is the slant height.
    return math.pi * radius * slant

def Calculate_Cone_surface_area(radius, slant):
    #The surface area of a cone consists of two parts: the area of its base and its lateral (side) surface area.
    return math.pi * radius**2 + math.pi * radius * slant