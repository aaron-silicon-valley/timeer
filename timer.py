<<<<<<< HEAD
#!/usr/bin/env python3
from playsound import playsound
# from os import system, if playsound doesn't work use os.system bash script. EX. afplay
=======

#!/usr/bin/env python3
from playsound import playsound
from os import system
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    pa = "/path/to/file/.m4a" #make sure to change this
    playsound(pa)
    print(f'Hi, {time}')
=======
    pa = "/Users/aaron/Desktop/funk-loud.m4a"
    # system(pa)
    playsound(pa)
    print(f'Hi, {time}')  # Press ⌘F8 to toggle the breakpoint.
>>>>>>> refs/remotes/origin/main


if __name__ == '__main__':
    timer_set()

<<<<<<< HEAD
#aaron-silicon-valley
=======
>>>>>>> refs/remotes/origin/main
