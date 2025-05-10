# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import platform
import os
import subprocess
import shutil
import socket
from typing import Optional, List, Union


class OS:
  """Class for operating system related operations"""

  OS_NAME = platform.system()
  RELEASE = platform.release()

  @staticmethod
  def get_home_dir() -> str:
    """Get user's home directory"""
    return os.path.expanduser("~")

  @staticmethod
  def is_dir(path: str) -> bool:
    """Check if path is a directory"""
    return os.path.isdir(path)

  @staticmethod
  def is_file(path: str) -> bool:
    """Check if path is a file"""
    return os.path.isfile(path)

  @staticmethod
  def path_exists(path: str) -> bool:
    """Check if path exists"""
    return os.path.exists(path)

  @staticmethod
  def get_size(path: str) -> int:
    """
        Get size of file/directory in bytes

        Args:
            path: Path to check

        Returns:
            Size in bytes or -1 if path doesn't exist
        """
    if OS.path_exists(path=path):
      return os.stat(path=path).st_size
    return -1

  @staticmethod
  def get_user() -> str:
    """Get current username"""
    return os.getlogin()

  @staticmethod
  def get_current_user() -> str:
    """Get current username (alternative method)"""
    return OS.run('whoami').strip()

  @staticmethod
  def get_host_name() -> str:
    """Get system hostname"""
    return socket.gethostname()

  @staticmethod
  def get_path() -> str:
    """Get current working directory"""
    return os.getcwd()

  @staticmethod
  def change_path(path: str) -> bool:
    """
        Change current working directory

        Args:
            path: Path to change to

        Returns:
            True if successful, False otherwise
        """
    if OS.is_dir(path=path):
      os.chdir(path=path)
      return True
    return False

  @staticmethod
  def get_user_permission() -> int:
    """Get current user's effective UID"""
    return os.geteuid()

  @staticmethod
  def get_list(path: str) -> Optional[List[str]]:
    """
        Get directory listing

        Args:
            path: Directory path

        Returns:
            List of directory contents or None if path is not a directory
        """
    if not OS.is_dir(path):
      return None
    return os.listdir(path)

  @staticmethod
  def get_file_from_path(path: str) -> Optional[str]:
    """
        Extract filename from path

        Args:
            path: Full file path

        Returns:
            Filename or None if path is not a file
        """
    if not OS.is_file(path):
      return None
    spl = '\\' if OS.OS_NAME.lower() == 'windows' else '/'
    return path.split(spl)[-1]

  @staticmethod
  def get_file_name(file: str) -> Optional[str]:
    """
        Get filename without extension

        Args:
            file: Filename or path

        Returns:
            Basename without extension or None if invalid
        """
    x = OS.get_file_from_path(file)
    if not x:
      return x
    return x.split('.')[0]

  @staticmethod
  def get_path_from_file(file: str) -> Optional[str]:
    """
        Get directory path from full file path

        Args:
            file: Full file path

        Returns:
            Directory path or None if invalid
        """
    x = OS.get_file_from_path(file)
    if not x:
      return x
    return file.replace(x, '')

  @staticmethod
  def copy_file(file: str, path: str) -> bool:
    """
        Copy file to destination

        Args:
            file: Source file path
            path: Destination directory

        Returns:
            True if successful, False otherwise
        """
    if not OS.is_file(file) or not OS.is_dir(path):
      return False
    shutil.copyfile(file, path)
    return True

  @staticmethod
  def run(command: str) -> str:
    """
        Execute shell command

        Args:
            command: Command to execute

        Returns:
            Command output as string
        """
    if OS.OS_NAME.lower() == 'windows':
      output = subprocess.run(
        ['powershell.exe', command],
        shell=True,
        capture_output=True
      )
    else:
      output = subprocess.run(
        command,
        shell=True,
        capture_output=True
      )
    return output.stderr.decode() if output.stderr else output.stdout.decode()

  @staticmethod
  def system(command: str) -> None:
    """Execute shell command (no output capture)"""
    os.system(command)

  @staticmethod
  def delete_file(path: str) -> bool:
    """
        Delete a file

        Args:
            path: File path to delete

        Returns:
            True if successful, False otherwise
        """
    if OS.is_file(path=path):
      os.remove(path=path)
      return True
    return False

  @staticmethod
  def delete_dir(path: str) -> bool:
    """
        Delete a directory

        Args:
            path: Directory path to delete

        Returns:
            True if successful, False otherwise
        """
    if OS.is_dir(path=path):
      os.rmdir(path=path)
      return True
    return False


# Legacy functions for backward compatibility
def get_home_dir(*args, **kwargs):
  return OS.get_home_dir(*args, **kwargs)


def is_dir(*args, **kwargs):
  return OS.is_dir(*args, **kwargs)


def is_file(*args, **kwargs):
  return OS.is_file(*args, **kwargs)


def path_exists(*args, **kwargs):
  return OS.path_exists(*args, **kwargs)


def get_size(*args, **kwargs):
  return OS.get_size(*args, **kwargs)


def get_user(*args, **kwargs):
  return OS.get_user(*args, **kwargs)


def get_current_user(*args, **kwargs):
  return OS.get_current_user(*args, **kwargs)


def get_host_name(*args, **kwargs):
  return OS.get_host_name(*args, **kwargs)


def get_path(*args, **kwargs):
  return OS.get_path(*args, **kwargs)


def change_path(*args, **kwargs):
  return OS.change_path(*args, **kwargs)


def get_user_permission(*args, **kwargs):
  return OS.get_user_permission(*args, **kwargs)


def get_list(*args, **kwargs):
  return OS.get_list(*args, **kwargs)


def get_file_from_path(*args, **kwargs):
  return OS.get_file_from_path(*args, **kwargs)


def get_file_name(*args, **kwargs):
  return OS.get_file_name(*args, **kwargs)


def get_path_from_file(*args, **kwargs):
  return OS.get_path_from_file(*args, **kwargs)


def copy_file(*args, **kwargs):
  return OS.copy_file(*args, **kwargs)


def run(*args, **kwargs):
  return OS.run(*args, **kwargs)


def system(*args, **kwargs):
  return OS.system(*args, **kwargs)


def delete_file(*args, **kwargs):
  return OS.delete_file(*args, **kwargs)


def delete_dir(*args, **kwargs):
  return OS.delete_dir(*args, **kwargs)


# Global variables for backward compatibility
OS_NAME = OS.OS_NAME
RELEASE = OS.RELEASE