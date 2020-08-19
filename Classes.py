import turtle

class Polygon:
    """docstring for Polygon."""
    def __init__(self, sides, name, size = 100, color = "black", line_thickness = 2):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angle = (self.sides - 2)*180
        self.angle = self.interior_angle / self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180 - self.angle)
        turtle.hideturtle()
        turtle.done()
        

# Concept of Subclassing.
class Square(Polygon):
    """docstring for Square."""
    def __init__(self, size=100, color='black', line_thickness = 2):
        # super uses the initilise method of the parent class.
        super().__init__(4, "square", size, color, line_thickness)

squ = Square(color = "#213acb", line_thickness = 5)

# Square = Polygon(4,'Square')
# Pentagon = Polygon(5,'Pentagon')
#
# print(Square.sides, Square.name, Square.interior_angle, Square.angle)
#
# print(Pentagon.sides, Pentagon.name, Pentagon.interior_angle, Pentagon.angle)

# Square.draw()
# Pentagon.draw()
# Hexagon = Polygon(6, 'Hexagaon', 100,"red")
# Hexagon.draw()

squ.draw()
