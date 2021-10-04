from lab_python_oop.geomfigure import GeomFigure
from lab_python_oop.color import FigureColor
import math

class Circle(GeomFigure):
    NAME = "Круг"

    def __init__(self, _radius, _color):
        self.radius = _radius
        self.color = FigureColor()
        self.color.color = _color

    def square(self):
        return self.radius * self.radius * math.pi

    @classmethod
    def get_name(obj):
        return obj.NAME

    def __repr__(self):
        return 'Фигура: {}\nПараметры:\n\tрадиус: {}\n\
        цвет: {}\n\tплощадь: {}\n'.format(
            Circle.get_name(),
            self.radius,
            self.color.color,
            self.square()
        )