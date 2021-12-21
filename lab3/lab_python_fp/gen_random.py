from random import randint

def gen_random(count, min, max):
    return [randint(min, max) for i in range(count)]

def main():
    print('gen_random.py')
    print(*gen_random(5, 1, 3), sep=', ')

if __name__ == "__main__":
    main()