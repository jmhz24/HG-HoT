def Trapezoid_midline_area_relationship(high, midline=None, area=None):
    # This function uses the property that the relationship between the midline and the area of a trapezoid.
    if midline:
        return midline * high
    else:
        return area / high
