class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return .5 * self.base * self.height


        def __str__(self):
            out = str(self.base) + ", " + str(self.height)
            return out

