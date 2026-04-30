def Polygon_sum_interior_angle(number_line, other_angle):
    # This function uses the property that the sum of the interior angles of a polygon depends on the number of its sides. For a polygon with n sides, the sum of its interior angles is (n-2) × 180°.
    sum_interior_angle = (number_line - 2) * 180
    return sum_interior_angle - other_angle