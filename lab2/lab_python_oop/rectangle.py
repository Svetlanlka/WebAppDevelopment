from lab_python_oop.geomfigure import GeomFigure
from lab_python_oop.color import FigureColor


class Rectangle(GeomFigure):
    NAME = "Прямоугольник"

    def __init__(self, _width, _height, _color):
        self.width = _width
        self.height = _height
        self.color = FigureColor()
        self.color.color = _color

    def square(self):
        return self.width * self.height

    @classmethod
    def get_name(obj):
        return obj.NAME

    def __repr__(self):
        return 'Фигура: {}\nПараметры:\n\tширина: {}\n\tвысота: {}\n\
        цвет: {}\n\tплощадь: {}\n'.format(
            Rectangle.get_name(),
            self.width,
            self.height,
            self.color.color,
            self.square()
        )