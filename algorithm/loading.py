# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import sys, progressbar, threading, itertools
from time import sleep
from algorithm.colors import *
from alive_progress import alive_bar
from algorithm.thread import Thread
from progress.bar import Bar

color = blue

def loading_print(list, message: str = 'Loading: ', color: str = color) -> None:
    with alive_bar(len(list), title = color + message, force_tty = False, calibrate = None) as bar:
        for i in list: yield i; bar()

def loading_message(message: str = 'Loading...', color: str = color) -> None: progressbar.ProgressBar(widgets=[color + message]).start()

def loading_animation(list, message: str = 'Loading...', color: str = color) -> None:
    bar = progressbar.ProgressBar(widgets=[color + message, progressbar.AnimatedMarker()]).start()
    for i in list: yield i; bar.update()

def loading_bar(list, message: str = 'Loading: ', icon: str = '█', color: str = color) -> None:
    with Bar(message, suffix='%(percent)d%%', fill=icon) as bar:
        for i in list: yield i; bar.next()

class loading_thread(threading.Thread):

    color = blue

    def __init__(self, message: str = 'Loading...', color: str = color) -> None :
        self.l = len(message) + 1
        self.thread = Thread(target=self.animate, args=(message, color,))
        self.thread.start()

    def stop(self, message: str = None) -> None :
        self.thread.kill()
        sys.stdout.write('\r' + (' ' * self.l))
        if message: sys.stdout.write('\r' + message + '\n')
        else: sys.stdout.write('\r')

    def animate(self, message: str, color: str) -> None :
        for c in itertools.cycle(['|', '/', '-', '\\']):
            sys.stdout.write('\r' + color + message + c)
            sys.stdout.flush()
            sleep(0.05)

def loading_list(list, message: str = "Loading: ", style: bool = True, size: int = 50, color: str = color) -> None :
    count = len(list)
    def show(j) -> None :
        x = int(size*j/count)
        sys.stdout.flush()
        if style: sys.stdout.write(color + "%s[%s%s] %i/%i\r" %(message, u'█'*x, " "*(size-x), j, count))
        else: sys.stdout.write(color + "%s[%s%s] %i/%i\r" %(message, u'#'*x, "."*(size-x), j, count))
        sys.stdout.flush()
    show(0)
    for i, item in enumerate(list): yield item; show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()