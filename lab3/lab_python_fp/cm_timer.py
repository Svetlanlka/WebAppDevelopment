from time import sleep, time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.__time_start = time()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        time_end = time()
        print('time: ', round(time_end - self.__time_start, 2))

@contextmanager
def cm_timer_2():
    time_start = time()
    yield
    time_end = time()
    print('time: ', round(time_end - time_start, 2))

def main():
    print('cm_timer.py')
    with cm_timer_1():
        sleep(2.5)
    with cm_timer_2():
        sleep(2.5)

if __name__ == "__main__":
    main()