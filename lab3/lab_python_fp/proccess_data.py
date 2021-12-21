import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique
from field import field

path = r"C:\Users\Pocht\OneDrive\Study\семестр5\РИП\webappdevelopment\lab3\lab_python_fp/data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)

def unique_sort(arr):
    tmp = []
    for i in Unique(arr, ignore_case=True):
        tmp.append(i)
    return sorted(tmp)

def f1(arg):
    return unique_sort([elem['job-name'] for elem in arg])

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    salary = list(gen_random(len(arg), 100000, 200000))
    work = list(zip(arg, salary))
    return list(map(lambda x: x[0] + ', зарплата ' + str(x[1]) + ' руб.', work))

def main():
    print('proccess_data.py')
    # print(f1(data))
    # print(f2(f1(data)))
    # print(f3(f2(f1(data))))
    with cm_timer_1():
        print(f4(f3(f2(f1(data)))))

if __name__ == "__main__":
    main()