"""
Problem definition:
There is an arbitrary line segment, which start point (wall1) and end point (wall2)
are defined by a pair of tuples: (x1, y1) and (x2, y2).
There is also an arbitrary vector which start and end point are defined in the same way.

The need is to evaluate whether the vector (which could be extended) hits the line segment.
If it does, it's also needed to evaluate how close their intersection point lies to the segment's center point.
If the vector crosses the segment in its center point, the result is 100%.
If the vector crosses one of the segments edge points, the result is 0%.
"""


from math import acos, sin, pi


class Vector:
    def __init__(self, end_point):
        self.x = end_point[0]
        self.y = end_point[1]

    def __sub__(self, other):
        return Vector((self.x - other.x, self.y - other.y))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y

    def length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def angle(self, other):
        return acos((self * other) / (self.length() * other.length()))


def shot(wall1, wall2, start_point, end_point):
    vector = Vector(end_point) - Vector(start_point)
    w1 = Vector(wall1) - Vector(start_point)
    w2 = Vector(wall2) - Vector(start_point)

    w1_w2, w1_shoot, w2_shoot = w1.angle(w2), w1.angle(vector), w2.angle(vector)
    if not -10e-6 < w1_w2 - w1_shoot - w2_shoot < 10e-6: return -1

    alpha, beta, w = min([(w1_shoot, w1.angle(w1-w2), w1), (w2_shoot, w2.angle(w2-w1), w2)])
    h = w.length() * sin(alpha) / sin(pi - alpha - beta)
    return round(2 * h * 100 / (w1-w2).length())
