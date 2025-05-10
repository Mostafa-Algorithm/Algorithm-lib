# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import requests, validators, subprocess, netifaces, socket, select
from algorithm.loading import loading_message
from algorithm.colors import *
from algorithm.os import OS_NAME
from speedtest import Speedtest # speedtest-cli
from getmac import get_mac_address
from psutil import process_iter
from signal import SIGTERM

def get_url_text(url: str) -> str: return requests.get(url=url).text

def public_ip() -> str: return requests.get("https://api.ipify.org").text

def local_ip() -> str: return ifaces_info()[iface()]['ip']

def gateway() -> list: return netifaces.gateways()['default'][2]

def getmac(iface=None, ipv4=None, ipv6=None, hostname=None) -> str: return get_mac_address(interface=iface, ip=ipv4, ip6=ipv6, hostname=hostname)

def check_ipv4_format(ip: str) -> bool: return validators.ipv4(ip) == True

def check_ipv6_format(ip: str) -> bool: return validators.ipv6(ip) == True

def check_domain_format(domain: str) -> bool: return validators.domain(domain) == True

def check_url_format(url: str) -> bool: return validators.url(url) == True

def download_speed() -> int: return round(Speedtest().download()/(1024 * 1024))

def upload_speed() -> int: return round(Speedtest().upload()/(1024 * 1024))

def speed_test() -> list[int, int]: return [download_speed(), upload_speed()]

def ifaces() -> list: return netifaces.interfaces()

def iface() -> str: return gateway()[1]

def check_connection(target: str = 'google.com', message: str = None) -> bool:
    param = '-n1' if OS_NAME.lower()=='windows' else '-c1'
    try:
        if message:
            loading_message('[-] Connecting to ' + message)
            if str(subprocess.Popen(["ping", param, "-w100", target], stdout=subprocess.PIPE).stdout.read()).__contains__('ttl='):
                print(green + '[+] %s connection found. ^_^' %message)
                return True
            else:
                print(red + '[*] %s connection failed. *_*' %message)
                return False
        else:
            return str(subprocess.Popen(["ping", param, "-w100", target], stdout=subprocess.PIPE).stdout.read()).__contains__('ttl=')
    except requests.ConnectionError or requests.ConnectTimeout: return False

def ifaces_info() -> dict:
    my_data = {}
    for iface in ifaces():
        data = netifaces.ifaddresses(iface)
        my_data[iface] = {}
        my_data[iface]['addr'] = data[list(data.keys())[1]][0]['addr']
        try:
            if data.get(2):
                my_data[iface]['ip'] = data[2][0]['addr']
                my_data[iface]['netmask'] = data[2][0]['netmask']
        except IndexError or KeyError:
            pass
    return my_data

def kill_port(port: int) -> bool | None:
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == port:
                from psutil._common import AccessDenied
                try: proc.send_signal(SIGTERM); return True
                except AccessDenied: return None
    return False