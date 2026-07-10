class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius    
    def circumference(self):
        return 2 * 3.14 * self.radius
    def diameter(self):
        return 2 * self.radius
    
radius = int(input("enter the radius"))
circ = Circle(radius)
print("circumference is:",circ.circumference())
print("Area of the circle:",circ.area())
print("Diameter is:",circ.diameter())