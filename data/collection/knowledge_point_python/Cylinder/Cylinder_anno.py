import math

def Calculate_Cylinder_volume(radius, height):
    # The volume of a cylinder can be calculated using the following formula: V = πr²h, where V is the volume, π is the constant pi (approximately 3.14), r is the radius of the circular base, and h is the height of the cylinder.
    return math.pi * radius**2 * height

def Calculate_Cylinder_base_area(radius):
    # The base area of a circular is calculated using the formula: Base Area = πr².
    return math.pi * radius**2

def Calculate_Cylinder_lateral_area(radius, height):
    # To calculate the lateral area of a cylinder, the formula is: Lateral Area = 2πrh, where Lateral Area is the area of the side surface, r is the radius of the base, and h is the height.
    return 2 * math.pi * radius * height

def Calculate_Cylinder_surface_area(radius, height):
    # The surface area of a cylinder includes two bases and a lateral surface. The formula for calculating the surface area is: Surface Area = 2πrh + 2πr², where A is the surface area, r is the radius of the circular base, and h is the height of the cylinder.
    return 2 * math.pi * radius**2 + 2 * math.pi * radius * height