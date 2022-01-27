#!/usr/bin/python3

from threading import Thread
from RetThread import RetThread

# create @thread_count thread to call @func(@argsv[*])
# @ret is the list of value returned by @func.
# ret[*] = func(argsv[*])
def run(func, argsv, thread_count):
    if thread_count <= 0:
        thread_count = 1

    ts = []
    step = int((len(argsv) + thread_count)/ thread_count)
    for i in range(0, len(argsv), step):
        if i + step > len(argsv):
            step = len(argsv) - i
        t = RetThread(func=func, args=argsv[i:i + step])
        ts.append(t)

    for t in ts:
        t.start()

    ret = []
    for t in ts:
        t.join()
        ret += t.get_ret()
    return ret

def ThreadFunc(args):
    return args

def main():
    ret = run(func = ThreadFunc, argsv = range(0,10), thread_count = 0)
    print(ret)

if __name__ == '__main__':
    main()

