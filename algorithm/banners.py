# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

from time import sleep
from algorithm.colors import *
from pyfiglet import figlet_format
from typing import Optional


def banner1() -> None:
  """Display the first banner style"""
  print()
  sleep(0.125)
  print(
    "\t%s[%sXXXXX%s|     %s//\\      %s|%sXXXXXXXXXXXXXXXXXXXXXXXXX%s]" % (white_bold, red_bold, white_bold, blue_bold,
                                                                           white_bold, red_bold, white_bold))
  sleep(0.125)
  print(
    "\t%s[%sXXXXX%s|    %s//  \\     %s|%sXXXXXX%s _%s|\\%s_________ %sXXXXX%s]" % (white_bold, red_bold, white_bold,
                                                                                    blue_bold, white_bold, red_bold,
                                                                                    white_bold, blue_bold, white_bold,
                                                                                    red_bold, white_bold))
  sleep(0.125)
  print(
    "\t%s[%sXXXXX%s|   %s//    \\    %s|%sXXXXXX%s| %s| \\   __   %s|%sXXXXX%s]" % (white_bold, red_bold, white_bold,
                                                                                    blue_bold, white_bold, red_bold,
                                                                                    white_bold, blue_bold, white_bold,
                                                                                    red_bold, white_bold))
  sleep(0.125)
  print(
    "\t%s[%sXXXXX%s|  %s//      \\   %s|%sXXXXXX%s| %s|  \\ /  |  %s|%sXXXXX%s]" % (white_bold, red_bold, white_bold,
                                                                                    blue_bold, white_bold, red_bold,
                                                                                    white_bold, blue_bold, white_bold,
                                                                                    red_bold, white_bold))
  sleep(0.125)
  print(
    "\t%s[%sXXXXX%s| %s/=========\\  %s|%sXXXXXX%s| %s| |\\V/| |  %s|%sXXXXX%s]" % (white_bold, red_bold, white_bold,
                                                                                    blue_bold, white_bold, red_bold,
                                                                                    white_bold, blue_bold, white_bold,
                                                                                    red_bold, white_bold))
  sleep(0.125)
  print("\t%s[%sXXXXX%s|%s//          \\ %s|%sXXXXXX%s| %s| | V | |  %s|%sXXXXX%s]" % (white_bold, red_bold, white_bold,
                                                                                       blue_bold, white_bold, red_bold,
                                                                                       white_bold, blue_bold,
                                                                                       white_bold, red_bold,
                                                                                       white_bold))
  sleep(0.125)
  print("\t%s[%sXXXXX%s|_____________%s\\%s|%sXXXXXX%s| %s V    | |  %s|%sXXXXX%s]" % (white_bold, red_bold, white_bold,
                                                                                       blue_bold, white_bold, red_bold,
                                                                                       white_bold, blue_bold,
                                                                                       white_bold, red_bold,
                                                                                       white_bold))
  sleep(0.125)
  print("\t%s[%sXXXXX               %s\\%sXXXXXX%s|       %s| |  %s|%sXXXXX%s]" % (white_bold, red_bold, blue_bold,
                                                                                   red_bold, white_bold, blue_bold,
                                                                                   white_bold, red_bold, white_bold))
  sleep(0.125)
  print(
    "\t%s[%sXXXXXXXXXXXXXXXXXXXXXXXXXXX%s|        %sV   %s|%sXXXXX%s]" % (white_bold, red_bold, white_bold, blue_bold,
                                                                          white_bold, red_bold, white_bold))
  sleep(0.125)
  print("\t%s[%sXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX%s]" % (white_bold, red_bold, white_bold))
  sleep(0.125)
  print()


def banner2() -> None:
  """Display the second banner style"""
  print()
  sleep(0.125)
  print(red_bold + "     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     ")
  sleep(0.125)
  print(
    "     %sXXXXXXX %s* %sXXXXXXXXXXXXXXXXXXXXXXXXXXXXX %s* %sXXXXXXX     " % (red_bold, blue_bold, red_bold, blue_bold,
                                                                               red_bold))
  sleep(0.125)
  print(
    "     %sXXXXXXXX %sMM %sXXXXXXXXXXXXXXXXXXXXXXXXX %sMM %sXXXXXXXX     " % (red_bold, blue_bold, red_bold, blue_bold,
                                                                               red_bold))
  sleep(0.125)
  print(
    "     %sXXXXXXXXX %sMMM %sXXXXXXXXXXXXXXXXXXXXX %sMMM %sXXXXXXXXX     " % (red_bold, blue_bold, red_bold, blue_bold,
                                                                               red_bold))
  sleep(0.125)
  print(
    "     %sXXXXXXXXXX %sMMM %sXXXXXXXXXXXXXXXXXXX %sMMM %sXXXXXXXXXX     " % (red_bold, blue_bold, red_bold, blue_bold,
                                                                               red_bold))
  sleep(0.125)
  print("     %sXXXXXXXXX %sMMM %sXXXXXXXXX %s* %sXXXXXXXXX %sMMM %sXXXXXXXXX     " % (red_bold, blue_bold, red_bold,
                                                                                       blue_bold, red_bold, blue_bold,
                                                                                       red_bold))
  sleep(0.125)
  print("     %sXXXXXXXX %sMMM %sXXXXXXXXX %sMMM %sXXXXXXXXX %sMMM %sXXXXXXXX     " % (red_bold, blue_bold, red_bold,
                                                                                       blue_bold, red_bold, blue_bold,
                                                                                       red_bold))
  sleep(0.125)
  print("     %sXXXXXXX %sMMMMMM %sXXXXXX %sMMMMM %sXXXXXX %sMMMMMM %sXXXXXXX     " % (red_bold, blue_bold, red_bold,
                                                                                       blue_bold, red_bold, blue_bold,
                                                                                       red_bold))
  sleep(0.125)
  print("     %sXXXXXX %sMMMM MMMM %sXXX %sMMMMMMM %sXXX %sMMMM MMMM %sXXXXXX     " % (red_bold, blue_bold, red_bold,
                                                                                       blue_bold, red_bold, blue_bold,
                                                                                       red_bold))
  sleep(0.125)
  print(" %s*   %sXXXXX %sMMMM %sX %sMMMM %sX %sMMM   MMM %sX %sMMMM %sX %sMMMM %sXXXXX   %s* " % (blue_bold, red_bold,
                                                                                                   blue_bold, red_bold,
                                                                                                   blue_bold, red_bold,
                                                                                                   blue_bold, red_bold,
                                                                                                   blue_bold, red_bold,
                                                                                                   blue_bold, red_bold,
                                                                                                   blue_bold))
  sleep(0.125)
  print(
    "  %sMM %sXXXX %sMMMM %sXXXX %sMMMMMM       MMMMMM %sXXXX %sMMMM %sXXXX %sMM  " % (blue_bold, red_bold, blue_bold,
                                                                                       red_bold, blue_bold, red_bold,
                                                                                       blue_bold, red_bold, blue_bold))
  sleep(0.125)
  print(
    "   %sMMM %sX %sMMMM %sXXXXXX %sMMMM         MMMM %sXXXXXX %sMMMM %sX %sMMM   " % (blue_bold, red_bold, blue_bold,
                                                                                       red_bold, blue_bold, red_bold,
                                                                                       blue_bold, red_bold, blue_bold))
  sleep(0.125)
  print(
    "    %sMMMMMMMM %sXXXXXX %sMMMM           MMMM %sXXXXXX %sMMMMMMMM    " % (blue_bold, red_bold, blue_bold, red_bold,
                                                                               blue_bold))
  sleep(0.125)
  print(
    "     %sMMM %sXXXXXXXXX %sMMMM  MMMMMMMMMMMMMMM %sXXXXXXXXX %sMMM     " % (blue_bold, red_bold, blue_bold, red_bold,
                                                                               blue_bold))
  sleep(0.125)
  print(
    "      %sMMM %sXXXXXXX %sMMMM               MMMM %sXXXXXXX %sMMM      " % (blue_bold, red_bold, blue_bold, red_bold,
                                                                               blue_bold))
  sleep(0.125)
  print("     %sX %sMMM %sXXXXX %sMMMM                 MMMM %sXXXXX %sMMM %sX     " % (red_bold, blue_bold, red_bold,
                                                                                       blue_bold, red_bold, blue_bold,
                                                                                       red_bold))
  sleep(0.125)
  print("     %sXXXXXXXXXXXX %sMMMM               MMMM %sXXXXXXXXXXXX     " % (red_bold, blue_bold, red_bold))
  sleep(0.125)
  print("     %sXXXXXXXXXXXXXX %sMMM             MMM %sXXXXXXXXXXXXXX     " % (red_bold, blue_bold, red_bold))
  sleep(0.125)
  print("     %sXXXXXXXXXXXXXXXX %sMM           MM %sXXXXXXXXXXXXXXXX     " % (red_bold, blue_bold, red_bold))
  sleep(0.125)
  print("     %sXXXXXXXXXXXXXXXXXX %s*         * %sXXXXXXXXXXXXXXXXXX     " % (red_bold, blue_bold, red_bold))
  sleep(0.125)
  print("     %sXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXX     " % (red_bold))
  sleep(0.125)
  print("     %sXXXXXXXXXXXXXXXXXXXXXX%s+...+%sXXXXXXXXXXXXXXXXXXXXXX     " % (red_bold, blue_bold, red_bold))
  sleep(0.125)
  print()


def banner3() -> None:
  """Display the third banner style"""
  print(red_bold)
  print('\t╭━━━┳╮╱╱╱╱╱╱╱╱╱╭╮╭╮')
  sleep(0.125)
  print('\t┃╭━╮┃┃╱╱╱╱╱╱╱╱╭╯╰┫┃')
  sleep(0.125)
  print('\t┃┃╱┃┃┃╭━━┳━━┳━╋╮╭┫╰━┳╮╭╮')
  sleep(0.125)
  print('\t┃╰━╯┃┃┃╭╮┃╭╮┃╭╋┫┃┃╭╮┃╰╯┃')
  sleep(0.125)
  print('\t┃╭━╮┃╰┫╰╯┃╰╯┃┃┃┃╰┫┃┃┃┃┃┃')
  sleep(0.125)
  print('\t╰╯╱╰┻━┻━╮┣━━┻╯╰┻━┻╯╰┻┻┻╯')
  sleep(0.125)
  print('\t╱╱╱╱╱╱╭━╯┃')
  sleep(0.125)
  print('\t╱╱╱╱╱╱╰━━╯')
  sleep(0.125)
  print()


def banner4() -> None:
  """Display the fourth banner style"""
  print(red_bold)
  print('\t░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗██╗░░██╗███╗░░░███╗')
  sleep(0.125)
  print('\t██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝██║░░██║████╗░████║')
  sleep(0.125)
  print('\t███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░███████║██╔████╔██║')
  sleep(0.125)
  print('\t██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██╔══██║██║╚██╔╝██║')
  sleep(0.125)
  print('\t██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░░██║██║░╚═╝░██║')
  sleep(0.125)
  print('\t╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝')
  sleep(0.125)
  print()


def banner_small() -> None:
  """Display a small banner"""
  print(red_bold + """
    ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
    █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█
    """)


def team_banner_large() -> None:
  """Display a large team banner"""
  print(red_bold)
  print(
    '\t░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░██╗████████╗██╗░░██╗███╗░░░███╗  ████████╗███████╗░█████╗░███╗░░░███╗')
  sleep(0.125)
  print(
    '\t██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗██║╚══██╔══╝██║░░██║████╗░████║  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║')
  sleep(0.125)
  print(
    '\t███████║██║░░░░░██║░░██╗░██║░░██║██████╔╝██║░░░██║░░░███████║██╔████╔██║  ░░░██║░░░█████╗░░███████║██╔████╔██║')
  sleep(0.125)
  print(
    '\t██╔══██║██║░░░░░██║░░╚██╗██║░░██║██╔══██╗██║░░░██║░░░██╔══██║██║╚██╔╝██║  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║')
  sleep(0.125)
  print(
    '\t██║░░██║███████╗╚██████╔╝╚█████╔╝██║░░██║██║░░░██║░░░██║░░██║██║░╚═╝░██║  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║')
  sleep(0.125)
  print(
    '\t╚═╝░░╚═╝╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝')
  sleep(0.125)
  print()


def team_banner_small() -> None:
  """Display a small team banner"""
  print(red_bold + """
    ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█  ▀█▀ █▀▀ ▄▀█ █▀▄▀█
    █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█  ░█░ ██▄ █▀█ █░▀░█
    """)


def make_banner(text: str, color: str = red_bold, font: str = 'standard') -> None:
  """
    Create a custom banner with the given text

    Args:
        text: Text to display in the banner
        color: Color to use for the banner
        font: Font style for the banner
    """
  print(color + figlet_format(text, font=font))
  print('Development by Algorithm\n')