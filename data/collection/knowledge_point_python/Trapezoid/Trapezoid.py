def Trapezoid_midline_area_relationship(high, midline=None, area=None):
    if midline:
        return midline * high
    else:
        return area / high
