class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.diameter * Circle.__pi
        return circumference

    def calculate_area(self):
        area = pow(self.diameter / 2, 2) * Circle.__pi
        return area

    def calculate_area_of_sector(self, angle):
        self.angle = angle
        sector_area = (self.angle / 360) * Circle.__pi * pow(self.diameter // 2, 2)
        return sector_area


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
