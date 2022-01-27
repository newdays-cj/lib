#!/usr/bin/python3

from threading import Thread

class RetThread(Thread):
    def __init__(self, func, args):
        super(RetThread, self).__init__()
        self.func = func
        self.argsv = args
        self.ret = []

    def run(self):
        for args in self.argsv:
            self.ret.append(self.func(args))

    def get_ret(self):
        return self.ret

