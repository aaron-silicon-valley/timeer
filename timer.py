
#!/usr/bin/env python3
from playsound import playsound
from os import system
from time import sleep


def get_timer():
    period_of_time = int(input("enter amount in minutes : "))
    min_time = period_of_time
    print(min_time)
    if type(period_of_time) != int:
        print("please use intergers(numbers): ")
        get_timer()
    return min_time


def timer_set():
    time = get_timer()
    set_period = sleep(time)
    pa = "/Users/aaron/Desktop/funk-loud.m4a"
    # system(pa)
    playsound(pa)
    print(f'Hi, {time}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    timer_set()

