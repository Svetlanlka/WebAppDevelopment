def field(items, *args):
    assert len(args) > 0
    objects = []

    if len(args) == 1:
         for item in items:
            if args[0] in item and item[args[0]] != None:
                yield item[args[0]]        

    for item in items:
        obj = {}

        for arg in args:
            if arg in item and item[arg] != None:
                obj[arg] = item[arg]
        if len(obj) > 0:
            yield obj

    

def main():
    print('field.py')
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    for item in field(goods, 'title'):
        print(item, end=', ')
    print('\n')

    for item in field(goods, 'title', 'price'):
        print(item, end=', ')
    print('\n')

if __name__ == "__main__":
    main()