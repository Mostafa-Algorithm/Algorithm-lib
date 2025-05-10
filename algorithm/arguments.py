# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

from argparse import ArgumentParser
from typing import Any, Dict, List, Optional, Union


class Arguments:
  def __init__(self, title: str, description: str = None) -> None:
    """Initialize argument parser with title and optional description"""
    self.add = False
    self.parser = ArgumentParser(prog=title, description=f'description: {description}')
    self.parser.format_help()
    self.options: List[str] = []
    self.groups: Dict[str, Any] = {}

  def __check__(self) -> None:
    """Check if any arguments have been added"""
    if not self.add:
      raise Exception('No arguments found...! *_*')

  def add_group(self, name: str, title: str, description: str) -> None:
    """Add an argument group"""
    self.groups[name] = self.parser.add_argument_group(title, description)

  def add_argument(self, shorter: str, longer: str, type: Any, description: str,
                   optional: bool = False, length: int = 1, group: str = None,
                   default: Any = None, choices: List[Any] = None) -> None:
    """
        Add an argument to the parser

        Args:
            shorter: Short flag (e.g., "h" for -h)
            longer: Long flag (e.g., "help" for --help)
            type: Argument type (e.g., str, int)
            description: Help description
            optional: Whether the argument is optional
            length: Number of arguments expected
            group: Group name to add argument to
            default: Default value
            choices: List of allowed values
        """
    if optional:
      description += ' (optional)'
      self.options.append(longer)
    if default is not None:
      description += f' (default={default})'
    if length <= 0:
      length = '+'

    opj = self.groups[group] if group else self.parser

    kwargs = {
      'nargs': length,
      'type': type,
      'help': description,
      'default': default
    }
    if choices:
      kwargs['choices'] = choices

    opj.add_argument(f'-{shorter}', f'--{longer}', **kwargs)

    if not self.add:
      self.add = True

  def get_argument(self, longer: str) -> Union[List[Any], Any]:
    """Get argument value by its long name"""
    arg = self.get_arguments()[longer]
    if arg is not None and len(arg) == 1:
      return arg[0]
    return arg

  def get_arguments(self) -> Dict[str, Any]:
    """Get all arguments as a dictionary"""
    self.__check__()
    return {arg[0]: arg[1] for arg in self.parser.parse_args()._get_kwargs()}

  def check_none(self) -> Optional[str]:
    """Check for missing required arguments"""
    dic = self.get_arguments()
    for key in dic:
      if not dic[key] and key not in self.options:
        return key
    return None

  def help_none(self, close: bool = True) -> None:
    """Print help if required arguments are missing"""
    if self.check_none():
      self.print_help()
      if close:
        exit()

  def print_help(self) -> None:
    """Print help message"""
    self.parser.print_help()
    print('\nDevelopment by Mostafa Algorithm\n')

  def get_parser(self) -> ArgumentParser:
    """Get the underlying ArgumentParser instance"""
    return self.parser