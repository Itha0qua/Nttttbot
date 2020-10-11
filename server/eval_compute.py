from math import *
from random import *
from scipy import *
from scipy import integrate
from numpy import *
import signal

def signal_handler(signum , frame):
    print('Time Out')
    raise RuntimeError

def eval_com(stri):
    signal.signal(signal.SIGALRM, signal_handler)
    try:
        signal.alarm(5)   # Ten seconds
        result = eval(stri)
        print(result)
        signal.alarm(0)
    except:
        signal.alarm(0)
        return '太烧脑了'
    return result

if __name__ == '__main__':
    while(True):
        a = input()
        print(eval_com(a))