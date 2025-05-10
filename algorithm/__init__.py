# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

__version__ = "2.0.0"
__author__ = "Mostafa Algorithm"
__license__ = "MIT"

# Import all modules
from algorithm.arguments import Arguments
from algorithm.banners import *
from algorithm.colors import *
from algorithm.fakemail import FakeMail
from algorithm.loading import Loading, LoadingThread
from algorithm.network import Network
from algorithm.os import OS
from algorithm.strings import StringUtils
from algorithm.thread import Thread
from algorithm.webdriver import WebDriver, WebDriverExceptions, BrowserConfig, BrowserType

# Legacy imports for backward compatibility
from algorithm.arguments import Arguments as arguments
from algorithm.banners import (
    banner1, banner2, banner3, banner4,
    banner_small, team_banner_large,
    team_banner_small, make_banner
)
from algorithm.colors import *
from algorithm.fakemail import FakeMail as fakemail
from algorithm.loading import (
    loading_print, loading_message,
    loading_animation, loading_bar,
    loading_list, loading_thread
)
from algorithm.network import Network as network
from algorithm.os import OS as os
from algorithm.strings import StringUtils as strings
from algorithm.thread import Thread as thread

__all__ = [
    'Arguments', 'arguments',
    'banner1', 'banner2', 'banner3', 'banner4',
    'banner_small', 'team_banner_large', 'team_banner_small', 'make_banner',
    'FakeMail', 'fakemail',
    'Loading', 'loading_print', 'loading_message',
    'loading_animation', 'loading_bar', 'loading_list', 'LoadingThread', 'loading_thread',
    'Network', 'network',
    'OS', 'os',
    'StringUtils', 'strings',
    'Thread', 'thread'
]