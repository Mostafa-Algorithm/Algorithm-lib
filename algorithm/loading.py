# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import sys
import time
import threading
import itertools
from enum import auto, Enum
from typing import List, Iterator, Optional, Callable, Any, Generator
from algorithm.colors import *
from algorithm.thread import Thread


class LoadingStyle(Enum):
  """Enumeration of available loading animation styles.

  Attributes:
      SPINNER: Classic spinner (|, /, -, \)
      DOTS: Expanding dots animation
      ARROWS: Rotating arrow animation
      BOUNCING: Bouncing bar animation
      SEARCHING: Radar-like searching animation
      RADAR: Sweeping radar animation
      PULSE: Pulsing circle animation
      BAR: Progress bar style (used for bar() method)
  """
  SPINNER = auto()
  DOTS = auto()
  ARROWS = auto()
  BOUNCING = auto()
  SEARCHING = auto()
  RADAR = auto()
  PULSE = auto()
  BAR = auto()


class Loading:
  """Advanced loading indicator with multiple styles and print handling.

  Features:
  - 8 built-in animation styles
  - Threaded and non-threaded operation
  - Progress bars for iterables
  - Context manager support
  - External print handling
  - Color customization

  Example Usage:
      >>> with Loading("Processing", style=LoadingStyle.PULSE):
      ...     # Your code here
      ...     time.sleep(2)
  """

  _ANIMATIONS = {
    LoadingStyle.SPINNER: ["|", "/", "-", "\\"],
    LoadingStyle.DOTS: [".", "..", "...", "...."],
    LoadingStyle.ARROWS: ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
    LoadingStyle.BOUNCING: ["[    ]", "[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]", "[   =]", "[    ]"],
    LoadingStyle.SEARCHING: [
      "[◜    ]", "[ ◜   ]", "[  ◜  ]", "[   ◜ ]", "[    ◜]",
      "[    ◝]", "[   ◝ ]", "[  ◝  ]", "[ ◝   ]", "[◝    ]",
      "[◞    ]", "[ ◞   ]", "[  ◞  ]", "[   ◞ ]", "[    ◞]",
      "[    ◟]", "[   ◟ ]", "[  ◟  ]", "[ ◟   ]", "[◟    ]"
    ],
    LoadingStyle.RADAR: [
      "🞅∙∙∙∙∙", "∙🞅∙∙∙∙", "∙∙🞅∙∙∙", "∙∙∙🞅∙∙", "∙∙∙∙🞅∙",
      "∙∙∙∙∙🞅", "∙∙∙∙🞆∙", "∙∙∙🞆∙∙", "∙∙🞆∙∙∙", "∙🞆∙∙∙∙"
    ],
    LoadingStyle.PULSE: ["○", "◎", "◉", "●", "◉", "◎"]
  }

  _COLORS = {
    "blue": blue,
    "green": green,
    "yellow": yellow,
    "red": red,
    "cyan": cyan,
    "white": white,
    "reset": reset
  }

  def __init__(
      self,
      message: str = "Loading...",
      color: str = "blue",
      style: LoadingStyle = LoadingStyle.SPINNER,
      use_thread: bool = False
  ):
    """Initialize loading indicator.

    Args:
        message: Text to display before animation
        color: Color name from available colors
        style: Animation style from LoadingStyle enum
        use_thread: Run animation in background thread
    """
    self.message = message
    self.color = self._COLORS.get(color, "\033[94m")
    self.style = style
    self.use_thread = use_thread
    self._stop_event = threading.Event()
    self._thread = None
    self._lock = threading.Lock()
    self._last_line_length = 0
    self._running = False

  def _get_frames(self):
    """Get animation frames for current style."""
    return self._ANIMATIONS.get(self.style, ["*"])

  def _animate(self):
      """Main animation loop with proper cleanup."""
      frames = itertools.cycle(self._get_frames())
      self._running = True

      try:
          while not self._stop_event.is_set():
              with self._lock:
                  self._clear_line()
                  frame = next(frames)
                  line = f"{self.color}{self.message} {frame}{self._COLORS['reset']}"
                  sys.stdout.write(line)
                  sys.stdout.flush()
                  self._last_line_length = len(line)
              time.sleep(0.1)
      except KeyboardInterrupt:
          pass  # Let the main thread handle the interrupt
      except Exception as e:
          print(f"\nLoading error: {e}", file=sys.stderr)
      finally:
          with self._lock:
              self._clear_line()
          self._running = False

  def _clear_line(self):
      """Clear the current line safely."""
      sys.stdout.write("\r" + " " * self._last_line_length + "\r")
      sys.stdout.flush()

  def start(self):
    """Start the loading animation.

    Starts either threaded or non-threaded animation based on initialization.
    """
    if self.use_thread:
      self._thread = Thread(target=self._animate)
      self._thread.daemon = True
      self._thread.start()
    else:
      self._animate()

  def stop(self, final_message: Optional[str] = None):
    """Stop the loading animation.

    Args:
        final_message: Optional message to display after stopping
    """
    self._stop_event.set()

    try:
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=0.1)  # Short timeout for KeyboardInterrupt
    except KeyboardInterrupt:
        pass  # Already stopping

    with self._lock:
        self._clear_line()
        if final_message:
            print(final_message)

  def __enter__(self):
    """Context manager entry point.

    Returns:
        self: Loading instance
    """
    self.start()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    """Context manager exit point.

    Args:
        exc_type: Exception type if any
        exc_val: Exception value if any
        exc_tb: Exception traceback if any
    """
    self.stop()

  @classmethod
  def bar(cls, iterable: List, message: str = "Loading: ", color: str = "blue",
          size: int = 50, fill_char: str = "█") -> Generator[Any, None, None]:
    """Create a progress bar for iterables.

    Args:
        iterable: Items to iterate over
        message: Prefix message
        color: Progress bar color
        size: Bar width in characters
        fill_char: Character to fill progress

    Yields:
        Items from the iterable one by one

    Example:
        >>> for item in Loading.bar(items):
        ...     process(item)
    """
    color_code = cls._COLORS.get(color, blue)
    total = len(iterable)

    def _update(progress: int):
      filled = int(size * progress / total)
      sys.stdout.write(
        f"\r{color_code}{message}[{fill_char * filled}{' ' * (size - filled)}] "
        f"{progress}/{total}{reset}"
      )
      sys.stdout.flush()

    _update(0)
    for i, item in enumerate(iterable, 1):
      yield item
      _update(i)
    print()

  @classmethod
  def spinner(cls, message: str = "Processing...", color: str = "blue",
              style: LoadingStyle = LoadingStyle.SPINNER) -> 'Loading':
    """Create a spinner context manager.

    Args:
        message: Text to display
        color: Spinner color
        style: Animation style

    Returns:
        Configured Loading instance

    Example:
        >>> with Loading.spinner("Thinking"):
        ...     complex_calculation()
    """
    return cls(message=message, color=color, style=style)


# Legacy API functions
def loading_print(*args, **kwargs) -> Iterator:
  """Legacy function for progress bar iteration.

  See Loading.bar() for implementation.
  """
  return Loading.bar(*args, **kwargs)


def loading_message(*args, **kwargs) -> Callable:
  """Legacy function for spinner context manager.

  See Loading.spinner() for implementation.
  """
  return Loading.spinner(*args, **kwargs)


def loading_animation(*args, **kwargs) -> Iterator:
  """Legacy function for animated iteration.

  See Loading.bar() for implementation.
  """
  return Loading.bar(*args, **kwargs)


def loading_bar(*args, **kwargs) -> Iterator:
  """Legacy function for progress bar.

  See Loading.bar() for implementation.
  """
  return Loading.bar(*args, **kwargs)


def loading_list(*args, **kwargs) -> Iterator:
  """Legacy function for list progress.

  See Loading.bar() for implementation.
  """
  return Loading.bar(*args, **kwargs)