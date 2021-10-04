  
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from colorama import init, Fore
init()

def main():
    rect = Rectangle(8, 8, "синий")
    circle = Circle(8, "зеленый")
    square= Square(8, "красный")
    print(Fore.BLUE)
    print(rect) 
    print(Fore.GREEN)
    print(circle)
    print(Fore.RED)
    print(square)

if __name__ == "__main__":
    main()