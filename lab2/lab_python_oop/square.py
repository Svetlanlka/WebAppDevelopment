from lab_python_oop.geomfigure import GeomFigure
from lab_python_oop.color import FigureColor

class Square(GeomFigure):
    NAME = "Квадрат"

    def __init__(self, _side, _color):
        self.side = _side
        self.color = FigureColor()
        self.color.color = _color

    def square(self):
        return self.side * self.side

    @classmethod
    def get_name(obj):
        return obj.NAME

    def __repr__(self):
        return 'Фигура: {}\nПараметры:\n\tширина стороны: {}\n\
        цвет: {}\n\tплощадь: {}\n'.format(
            Square.get_name(),
            self.side,
            self.color.color,
            self.square()
        )