# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import sys
import time
import threading
import itertools
import progressbar
from typing import List, Iterator, Optional
from alive_progress import alive_bar
from progress.bar import Bar
from algorithm.colors import *
from algorithm.thread import Thread


class Loading:
  """Class for displaying loading indicators and progress bars"""

  def __init__(self, color: str = blue):
    self.color = color

  @staticmethod
  def loading_print(items: List, message: str = 'Loading: ',
                    color: str = blue) -> Iterator:
    """
        Display an animated progress bar for iterating through a list

        Args:
            items: List of items to iterate through
            message: Message to display
            color: Color to use

        Returns:
            Iterator yielding items from the list
        """
    with alive_bar(len(items), title=color + message,
                   force_tty=False, calibrate=None) as bar:
      for item in items:
        yield item
        bar()

  @staticmethod
  def loading_message(message: str = 'Loading...', color: str = blue) -> None:
    """
        Display a simple loading message with animated marker

        Args:
            message: Message to display
            color: Color to use
        """
    progressbar.ProgressBar(
      widgets=[color + message]
    ).start()

  @staticmethod
  def loading_animation(items: List, message: str = 'Loading...',
                        color: str = blue) -> Iterator:
    """
        Display an animation while iterating through items

        Args:
            items: List of items to iterate through
            message: Message to display
            color: Color to use

        Returns:
            Iterator yielding items from the list
        """
    bar = progressbar.ProgressBar(
      widgets=[color + message, progressbar.AnimatedMarker()]
    ).start()

    for item in items:
      yield item
      bar.update()

  @staticmethod
  def loading_bar(items: List, message: str = 'Loading: ',
                  icon: str = '█', color: str = blue) -> Iterator:
    """
        Display a progress bar while iterating through items

        Args:
            items: List of items to iterate through
            message: Message to display
            icon: Character to use for progress bar
            color: Color to use

        Returns:
            Iterator yielding items from the list
        """
    with Bar(message, suffix='%(percent)d%%', fill=icon) as bar:
      for item in items:
        yield item
        bar.next()

  @staticmethod
  def loading_list(items: List, message: str = "Loading: ",
                   style: bool = True, size: int = 50,
                   color: str = blue) -> Iterator:
    """
        Display a custom loading bar for list iteration

        Args:
            items: List of items to iterate through
            message: Message to display
            style: Whether to use block style (True) or hash style (False)
            size: Width of the progress bar
            color: Color to use

        Returns:
            Iterator yielding items from the list
        """
    count = len(items)

    def show(j: int) -> None:
      """Update progress display"""
      x = int(size * j / count)
      sys.stdout.flush()
      if style:
        sys.stdout.write(color + "%s[%s%s] %i/%i\r" % (
          message, '█' * x, " " * (size - x), j, count))
      else:
        sys.stdout.write(color + "%s[%s%s] %i/%i\r" % (
          message, '#' * x, "." * (size - x), j, count))
      sys.stdout.flush()

    show(0)
    for i, item in enumerate(items):
      yield item
      show(i + 1)

    sys.stdout.write("\n")
    sys.stdout.flush()


class LoadingThread(threading.Thread):
  """Thread-based loading animation"""

  def __init__(self, message: str = 'Loading...', color: str = blue):
    """
        Initialize loading thread

        Args:
            message: Message to display
            color: Color to use
        """
    super().__init__()
    self.message = message
    self.color = color
    self.l = len(message) + 1
    self.thread = Thread(target=self.animate)
    self.thread.start()

  def stop(self, message: Optional[str] = None) -> None:
    """
        Stop the loading animation

        Args:
            message: Optional final message to display
        """
    self.thread.kill()
    sys.stdout.write('\r' + (' ' * self.l))
    if message:
      sys.stdout.write('\r' + message + '\n')
    else:
      sys.stdout.write('\r')

  def animate(self) -> None:
    """Run the loading animation"""
    for c in itertools.cycle(['|', '/', '-', '\\']):
      sys.stdout.write('\r' + self.color + self.message + c)
      sys.stdout.flush()
      time.sleep(0.05)


# Legacy functions for backward compatibility
def loading_print(*args, **kwargs):
  return Loading.loading_print(*args, **kwargs)


def loading_message(*args, **kwargs):
  return Loading.loading_message(*args, **kwargs)


def loading_animation(*args, **kwargs):
  return Loading.loading_animation(*args, **kwargs)


def loading_bar(*args, **kwargs):
  return Loading.loading_bar(*args, **kwargs)


def loading_list(*args, **kwargs):
  return Loading.loading_list(*args, **kwargs)


class loading_thread(LoadingThread):
  """Legacy class for backward compatibility"""
  pass