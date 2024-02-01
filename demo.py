class Point:
    default_user = "Guest"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f" Point of x,y ({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)


point = Point.zero()
print(point)