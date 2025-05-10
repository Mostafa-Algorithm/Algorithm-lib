# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import requests
import validators
import subprocess
import netifaces
import speedtest
from getmac import get_mac_address
from psutil import process_iter
from signal import SIGTERM
from typing import Optional, Dict, List
from algorithm.loading import Loading
from algorithm.colors import *
from algorithm.os import OS_NAME

class Network:
  """Class for network-related operations"""

  @staticmethod
  def get_url_text(url: str) -> str:
    """
        Get text content from a URL

        Args:
            url: URL to fetch

        Returns:
            Text content of the URL

        Raises:
            requests.RequestException: If request fails
        """
    return requests.get(url=url).text

  @staticmethod
  def public_ip() -> str:
    """
        Get public IP address

        Returns:
            Public IP address as string

        Raises:
            requests.RequestException: If request fails
        """
    return requests.get("https://api.ipify.org").text

  @staticmethod
  def local_ip() -> str:
    """
        Get local IP address

        Returns:
            Local IP address as string
        """
    return Network.ifaces_info()[Network.iface()]['ip']

  @staticmethod
  def gateway() -> List:
    """
        Get default gateway information

        Returns:
            List of gateway information
        """
    return netifaces.gateways()['default'][2]

  @staticmethod
  def getmac(iface: Optional[str] = None,
             ipv4: Optional[str] = None,
             ipv6: Optional[str] = None,
             hostname: Optional[str] = None) -> str:
    """
        Get MAC address for a network interface

        Args:
            iface: Interface name
            ipv4: IPv4 address
            ipv6: IPv6 address
            hostname: Hostname

        Returns:
            MAC address as string
        """
    return get_mac_address(
      interface=iface,
      ip=ipv4,
      ip6=ipv6,
      hostname=hostname
    )

  @staticmethod
  def check_ipv4_format(ip: str) -> bool:
    """
        Check if string is a valid IPv4 address

        Args:
            ip: IP address to validate

        Returns:
            True if valid IPv4, False otherwise
        """
    return validators.ipv4(ip) == True

  @staticmethod
  def check_ipv6_format(ip: str) -> bool:
    """
        Check if string is a valid IPv6 address

        Args:
            ip: IP address to validate

        Returns:
            True if valid IPv6, False otherwise
        """
    return validators.ipv6(ip) == True

  @staticmethod
  def check_domain_format(domain: str) -> bool:
    """
        Check if string is a valid domain name

        Args:
            domain: Domain to validate

        Returns:
            True if valid domain, False otherwise
        """
    return validators.domain(domain) == True

  @staticmethod
  def check_url_format(url: str) -> bool:
    """
        Check if string is a valid URL

        Args:
            url: URL to validate

        Returns:
            True if valid URL, False otherwise
        """
    return validators.url(url) == True

  @staticmethod
  def download_speed() -> int:
    """
        Measure download speed in Mbps

        Returns:
            Download speed in Mbps (rounded)
        """
    return round(speedtest.Speedtest().download() / (1024 * 1024))

  @staticmethod
  def upload_speed() -> int:
    """
        Measure upload speed in Mbps

        Returns:
            Upload speed in Mbps (rounded)
        """
    return round(speedtest.Speedtest().upload() / (1024 * 1024))

  @staticmethod
  def speed_test() -> List[int]:
    """
        Perform speed test (download and upload)

        Returns:
            List containing [download_speed, upload_speed] in Mbps
        """
    return [Network.download_speed(), Network.upload_speed()]

  @staticmethod
  def ifaces() -> List[str]:
    """
        Get list of network interfaces

        Returns:
            List of interface names
        """
    return netifaces.interfaces()

  @staticmethod
  def iface() -> str:
    """
        Get default network interface

        Returns:
            Interface name
        """
    return Network.gateway()[1]

  @staticmethod
  def check_connection(target: str = 'google.com',
                       message: Optional[str] = None) -> bool:
    """
        Check network connection to a target

        Args:
            target: Hostname or IP to check
            message: Optional message to display

        Returns:
            True if connection successful, False otherwise
        """
    param = '-n1' if OS_NAME.lower() == 'windows' else '-c1'
    try:
      if message:
        Loading.loading_message('[-] Connecting to ' + message)
        output = str(subprocess.Popen(
          ["ping", param, "-w100", target],
          stdout=subprocess.PIPE
        ).stdout.read())

        if 'ttl=' in output:
          print(green + '[+] %s connection found. ^_^' % message)
          return True
        else:
          print(red + '[*] %s connection failed. *_*' % message)
          return False
      else:
        output = str(subprocess.Popen(
          ["ping", param, "-w100", target],
          stdout=subprocess.PIPE
        ).stdout.read())
        return 'ttl=' in output
    except (requests.ConnectionError, requests.ConnectTimeout):
      return False

  @staticmethod
  def ifaces_info() -> Dict[str, Dict]:
    """
        Get information about all network interfaces

        Returns:
            Dictionary with interface information
        """
    my_data = {}
    for iface in Network.ifaces():
      data = netifaces.ifaddresses(iface)
      my_data[iface] = {}
      my_data[iface]['addr'] = data[list(data.keys())[1]][0]['addr']
      try:
        if data.get(2):
          my_data[iface]['ip'] = data[2][0]['addr']
          my_data[iface]['netmask'] = data[2][0]['netmask']
      except (IndexError, KeyError):
        pass
    return my_data

  @staticmethod
  def kill_port(port: int) -> Optional[bool]:
    """
        Kill process using a specific port

        Args:
            port: Port number to free

        Returns:
            True if successful, False if no process found,
            None if permission denied
        """
    for proc in process_iter():
      for conns in proc.connections(kind='inet'):
        if conns.laddr.port == port:
          from psutil._common import AccessDenied
          try:
            proc.send_signal(SIGTERM)
            return True
          except AccessDenied:
            return None
    return False


# Legacy functions for backward compatibility
def get_url_text(*args, **kwargs):
  return Network.get_url_text(*args, **kwargs)


def public_ip(*args, **kwargs):
  return Network.public_ip(*args, **kwargs)


def local_ip(*args, **kwargs):
  return Network.local_ip(*args, **kwargs)


def gateway(*args, **kwargs):
  return Network.gateway(*args, **kwargs)


def getmac(*args, **kwargs):
  return Network.getmac(*args, **kwargs)


def check_ipv4_format(*args, **kwargs):
  return Network.check_ipv4_format(*args, **kwargs)


def check_ipv6_format(*args, **kwargs):
  return Network.check_ipv6_format(*args, **kwargs)


def check_domain_format(*args, **kwargs):
  return Network.check_domain_format(*args, **kwargs)


def check_url_format(*args, **kwargs):
  return Network.check_url_format(*args, **kwargs)


def download_speed(*args, **kwargs):
  return Network.download_speed(*args, **kwargs)


def upload_speed(*args, **kwargs):
  return Network.upload_speed(*args, **kwargs)


def speed_test(*args, **kwargs):
  return Network.speed_test(*args, **kwargs)


def ifaces(*args, **kwargs):
  return Network.ifaces(*args, **kwargs)


def iface(*args, **kwargs):
  return Network.iface(*args, **kwargs)


def check_connection(*args, **kwargs):
  return Network.check_connection(*args, **kwargs)


def ifaces_info(*args, **kwargs):
  return Network.ifaces_info(*args, **kwargs)


def kill_port(*args, **kwargs):
  return Network.kill_port(*args, **kwargs)