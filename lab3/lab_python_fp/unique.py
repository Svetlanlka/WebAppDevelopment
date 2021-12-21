from gen_random import gen_random

# Итератор для удаления дубликатов
class Unique(object):
    ignore_case = False

    def __init__(self, items, **kwargs):
        self.__it = iter(items)
        self.__values = set()
        if kwargs.get('ignore_case') == True:
            Unique.ignore_case = True

    def __next__(self):
        while True:
             next_item = next(self.__it)
             if ((Unique.ignore_case == False and next_item not in self.__values) or
                (Unique.ignore_case == True and str(next_item).lower() not in self.__values 
                and str(next_item).lower() not in [j.lower() for j in self.__values])):
                    self.__values.add(next_item)
                    return next_item 

    def __iter__(self):
        return self

def main():
    print('unique.py')
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data1_unique =  Unique(data1)
    print(*data1_unique, sep=', ')

    data2 = gen_random(10, 1, 3)
    data2_unique =  Unique(data2)
    print(*data2_unique, sep=', ')

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    data3_unique =  Unique(data3)
    print(*data3_unique, sep=', ')

    data4_unique =  Unique(data3, ignore_case=True)
    print(*data4_unique, sep=', ')

    data5 = ['Sveta', 'TANYA', 'SVETA', 'Sveta', 'Svetta']
    data5_unique =  Unique(data5, ignore_case=True)
    print(*data5_unique, sep=', ')


if __name__ == "__main__":
    main()