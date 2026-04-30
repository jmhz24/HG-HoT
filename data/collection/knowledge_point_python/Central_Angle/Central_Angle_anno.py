def Central_Angle_relationship_with_arc(angle):
    #This function uses the property that the degree measure of an arc is equal to the degree measure of its corresponding central angle.
    return angle

def Central_Angle_relationship_with_inscribed_angle(central_angle=None, inscribed_angle=None):
    #This function uses the property that the degree measure of a central angle is twice the degree measure of any inscribed angle subtending the same arc.
    if central_angle:
        return (1 / 2) * central_angle
    else:
        return 2 * inscribed_angle

def Central_Angle_equal_chord(chord):
    #This function uses the property that the if two central angles are equal, then chords they subtend are also equal, and vice versa.
    return chord

def Central_Angle_equal_arc(arc):
    #This function uses the property that the if two central angles are equal, then arcs they subtend are also equal, and vice versa.
    return arc