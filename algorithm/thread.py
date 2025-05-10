# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import sys, threading
from _thread import *

class Thread(threading.Thread):
    def __init__(self, *args, **keywords) -> None:
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self) -> None:
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self) -> None:
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg) -> any:
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg) -> any:
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self) -> None:
        self.killed = True