def print_result(func):
    def decorator(*args):
        print(func.__name__)
        result = func(*args)
        if (type(result) == list):
            print(*result, sep='\n')
        elif (type(result) == dict):
            for key in result.keys():
                print(key, '=', result.get(key))
        else:
            print(result)
        return result

    return decorator

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

def main():
    print('print_result.py')
    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == "__main__":
    main()