#!/usr/bin/env python3
from playsound import playsound
# from os import system, if playsound doesn't work use os.system bash script. EX. afplay
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
    pa = "/path/to/file/.m4a" #make sure to change this
    playsound(pa)
    print(f'Hi, {time}')


if __name__ == '__main__':
    timer_set()

#aaron-silicon-valley