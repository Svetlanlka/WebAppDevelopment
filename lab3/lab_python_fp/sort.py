def abs_value(value):
    return abs(value)

def sort_simply(arr):
    return sorted(arr, reverse=True, key = abs_value)

def sort_with_lambda(arr):
    return sorted(arr, reverse=True, key=lambda el: abs(el))

def main():
    print('sort.py')
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    result = sort_simply(data)
    print(result)

    result_with_lambda = sort_with_lambda(data)
    print(result_with_lambda)


if __name__ == "__main__":
    main()