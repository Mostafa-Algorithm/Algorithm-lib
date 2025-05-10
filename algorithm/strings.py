# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import string
import secrets
import re
from typing import Optional, Union, List


class StringUtils:
  """Class for string manipulation and generation"""

  @staticmethod
  def random_string(
      start_with: Optional[str] = None,
      end_with: Optional[str] = None,
      length: int = 16,
      content: Optional[str] = None,
      lowercase: bool = True,
      uppercase: bool = True,
      digits: bool = True,
      symbols: bool = True,
      spaces: bool = True
  ) -> str:
    """
        Generate a random string with customizable options

        Args:
            start_with: String to prepend
            end_with: String to append
            length: Desired length of random part
            content: Custom character set to use
            lowercase: Include lowercase letters
            uppercase: Include uppercase letters
            digits: Include digits
            symbols: Include symbols
            spaces: Include spaces

        Returns:
            Generated random string
        """
    con = ''
    text = ''

    if content is None:
      if lowercase:
        con += string.ascii_lowercase
      if uppercase:
        con += string.ascii_uppercase
      if digits:
        con += string.digits
      if symbols:
        con += string.punctuation
      if spaces:
        con += ' '
    else:
      for c in content:
        con += StringUtils.get_like_string(c) or ''

    if start_with:
      text += start_with
      length -= len(start_with)
    if end_with:
      length -= len(end_with)

    if not con:
      raise ValueError("No character set available for generation")

    for _ in range(length):
      text += con[secrets.randbelow(len(con))]

    if end_with:
      text += end_with

    return text

  @staticmethod
  def type_of_string(s: str) -> str:
    """
        Determine the type of characters in a string

        Args:
            s: String to analyze

        Returns:
            String describing character type:
            'lower', 'upper', 'digit', 'space', 'title',
            'numeric', 'decimal', 'printable', 'symbol', 'unknown'
        """
    if s.islower():
      return 'lower'
    if s.isupper():
      return 'upper'
    if s.isdigit():
      return 'digit'
    if s.isspace():
      return 'space'
    if s.istitle():
      return 'title'
    if s.isnumeric():
      return 'numeric'
    if s.isdecimal():
      return 'decimal'
    if s.isprintable():
      return 'printable'
    if s in string.punctuation:
      return 'symbol'
    return 'unknown'

  @staticmethod
  def get_like_string(text: str) -> Optional[str]:
    """
        Get character set matching the types in the input text

        Args:
            text: Input text to analyze

        Returns:
            String containing all character types present in input,
            or None if no recognizable types found
        """
    r = ''
    for c in text:
      if c.islower() and string.ascii_lowercase not in r:
        r += string.ascii_lowercase
      if c.isupper() and string.ascii_uppercase not in r:
        r += string.ascii_uppercase
      if c.isdigit() and string.digits not in r:
        r += string.digits
      if c.isspace() and ' ' not in r:
        r += ' '
      if c in string.punctuation and string.punctuation not in r:
        r += string.punctuation
    return r if r else None

  @staticmethod
  def check_format(text: str, format: str) -> bool:
    """
        Check if text matches a regex format

        Args:
            text: Text to check
            format: Regex pattern to match

        Returns:
            True if pattern matches, False otherwise
        """
    return bool(re.fullmatch(format, text))


# Legacy functions for backward compatibility
def random_string(*args, **kwargs):
  return StringUtils.random_string(*args, **kwargs)


def type_of_string(*args, **kwargs):
  return StringUtils.type_of_string(*args, **kwargs)


def get_like_string(*args, **kwargs):
  return StringUtils.get_like_string(*args, **kwargs)


def check_format(*args, **kwargs):
  return StringUtils.check_format(*args, **kwargs)