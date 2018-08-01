class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)


class Triangle:

    def init_from_points(self, A, B, C):
        """Create triangle from Points"""
        self.A = A
        self.B = B
        self.C = C

    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        """Create triangle by coordinates of edges"""
        self.A = Point(Ax, Ay)
        self.B = Point(Bx, By)
        self.C = Point(Cx, Cy)

    def __str__(self):
        description = 'Triangle with edges {p1}, {p2}, {p3}'
        return description.format(p1=self.A, p2=self.B, p3=self.C)

    def __repr__(self):
        repr = '{classname}({p1x}, {p1y}, {p2x}, {p2y}, {p3x}, {p3y})'
        return repr.format(classname=self.__class__.__name__,
                           p1x=self.A.x, p1y=self.A.y, p2x=self.B.x, p2y=self.B.y, p3x=self.C.x, p3y=self.C.y)

    def __contains__(self, item):
        """Check if point is in Triangle"""
        b1 = self._sign(item, self.A, self.B) < 0
        b2 = self._sign(item, self.B, self.C) < 0
        b3 = self._sign(item, self.C, self.A) < 0
        return (b1 == b2) and (b2 == b3)

    @staticmethod
    def _sign(p1, p2, p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)


if __name__ == '__main__':

    origin = Point(0, 0)

    triangles = []
    with open("/home/darius/git/project-euler/102-triangle-containment/triangles.txt") as f:
        for line in f:
            coordinates = line.rstrip('\n').split(',')
            coordinates = [int(val) for val in coordinates]
            triangles.append(Triangle(*coordinates))

    # problem states that the first triangle from file contains origin, second doesnt
    assert (origin in triangles[0]) == True
    assert (origin in triangles[1]) == False

    contains_origin = [origin in triangle for triangle in triangles]
    print(contains_origin.count(True))