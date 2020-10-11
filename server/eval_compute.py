from math import *
from random import *
from scipy import *
from scipy import integrate
from numpy import *
import signal
global z
return_str = ['不会','太烧脑了','想干啥']

def signal_handler(signum , frame):
    z = 1
    print('Time Out')
    raise RuntimeError

def eval_com(stri):
    if '_' in stri:
        return return_str[2]
    z = 0
    signal.signal(signal.SIGALRM, signal_handler)
    try:
        signal.alarm(5)   # Ten seconds
        result = eval(stri, {'__builtins__':{},
                            'rand':rand,
                            'quad':integrate.quad,
                            'exp':exp,
                            'sin':sin,
                            'cos':cos,
                            'tan':tan,
                            'log':log,
                            'factorial':factorial})
        print(result)
        signal.alarm(0)
    except:
        signal.alarm(0)
        return return_str[z]
    return result

if __name__ == '__main__':
    while(True):
        a = input()
        print(eval_com(a))