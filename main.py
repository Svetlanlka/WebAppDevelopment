import sys
import math

def get_coef(index, message):
    try:
        coef = float(sys.argv[index])
    except:
        print(message)
        while 1:
            try:
                coef = float(input())
                break
            except:
                print(message)

    return coef


def calculate(a, b, c):
    roots = []
    D = b*b - 4*a*c
    if D == 0:
        roots.append(-b / (2.0*a))
    elif D > 0:
        roots.append(+(-b + math.sqrt(D)) / (2.0*a))
        roots.append((-b - math.sqrt(D)) / (2.0*a))
    return roots


def main():
    a = get_coef(1, 'Input coef А:')
    b = get_coef(2, 'Input coef B:')
    c = get_coef(3, 'Input coef C:')
    roots = calculate(a, b, c)
    
    number_of_roots = len(roots)
    if number_of_roots == 0:
        print('No roots')
    elif number_of_roots == 1:
        print('One root: ', roots[0])
    elif number_of_roots == 2:
        print('Two roots:', roots[0], ",", roots[1])
    else:
        print("Error! Too many roots")
    

if __name__ == "__main__":
    main()