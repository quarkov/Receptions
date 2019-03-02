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


def shot(wall1, wall2, shot_point, later_point):
    shoot = Vector(later_point) - Vector(shot_point)
    w1 = Vector(wall1) - Vector(shot_point)
    w2 = Vector(wall2) - Vector(shot_point)

    w1_w2, w1_shoot, w2_shoot = w1.angle(w2), w1.angle(shoot), w2.angle(shoot)
    if not -10e-6 < w1_w2 - w1_shoot - w2_shoot < 10e-6: return -1

    alpha, beta, w = min([(w1_shoot, w1.angle(w1-w2), w1), (w2_shoot, w2.angle(w2-w1), w2)])
    h = w.length() * sin(alpha) / sin(pi - alpha - beta)
    return round(2 * h * 100 / (w1-w2).length())
