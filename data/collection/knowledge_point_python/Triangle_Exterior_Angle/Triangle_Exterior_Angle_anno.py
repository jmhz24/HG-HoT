def Triangle_Exterior_Angle_add(angle_1, angle_2):
    #This function uses the property that an exterior angle of any triangle is equal to the sum of the two interior angles that are not adjacent to it.
    return angle_1 + angle_2

def Triangle_Exterior_Angle_minus(external_angle, interior_angle):
    #This function uses the property that an exterior angle of any triangle is equal to the sum of the two interior angles that are not adjacent to it.
    return external_angle - interior_angle

def Triangle_Exterior_Angle_isosceles_triangle(angle):
    #This function uses the property that in an isosceles triangle, the base angle (the angle between a leg and the base) is half of the exterior angle of the vertex angle (the angle between the two legs).
    return (1 / 2) * angle