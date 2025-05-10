# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

from algorithm.strings import random_string
from fake_email import Email
from typing import Dict, Optional


class FakeMail:
  """Class for handling fake email operations"""

  def __init__(self):
    self.mail: Optional[Dict] = None

  def get_mail(self) -> str:
    """
        Get a fake email address from omeie.com domain

        Returns:
            Email address string
        """
    while True:
      self.mail = Email().Mail()
      if self.mail['mail'].split("@")[-1] == "omeie.com":
        return self.mail['mail']

  def get_pwd(self, length: int = 16) -> str:
    """
        Generate a random password

        Args:
            length: Length of password to generate

        Returns:
            Random password string
        """
    return random_string(length=length)

  def start_listen(self) -> Dict:
    """
        Start listening for incoming emails

        Returns:
            Dictionary containing email details:
            - name: Sender name
            - from: Sender email
            - subject: Email subject
            - message: Email content

        Raises:
            Exception: If email session is not initialized
        """
    if not self.mail:
      raise Exception('Error in email session initialization *_*')

    while True:
      inbox = Email(self.mail['session']).inbox()
      if inbox:
        return {
          'name': inbox['name'],
          'from': inbox['from'],
          'subject': inbox['topic'],
          'message': inbox['message']
        }


# Global instance for backward compatibility
_fake_mail = FakeMail()


def get_mail() -> str:
  """Get a fake email address (legacy function)"""
  return _fake_mail.get_mail()


def get_pwd(length: int = 16) -> str:
  """Generate a random password (legacy function)"""
  return _fake_mail.get_pwd(length)


def start_listen() -> Dict:
  """Start listening for emails (legacy function)"""
  return _fake_mail.start_listen()