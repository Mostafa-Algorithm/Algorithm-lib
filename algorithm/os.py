import platform, os, subprocess, shutil, socket

OS_NAME = platform.system()
RELEASE = platform.release()

def get_home_dir() -> str: return os.path.expanduser("~")

def is_dir(path: str) -> bool: return os.path.isdir(path)

def is_file(path: str) -> bool: return os.path.isfile(path)

def path_exists(path: str) -> bool: return os.path.exists(path)

def get_size(path: str) -> int:
    if path_exists(path=path): return os.stat(path=path).st_size
    else: return -1

def get_user() -> str: return os.getlogin()

def get_current_user() -> str: return run('whoami').strip()

def get_host_name() -> str: return socket.gethostname()

def get_path() -> str: return os.getcwd()

def change_path(path: str) -> bool:
    if is_dir(path=path): os.chdir(path=path); return True
    else: return False

def get_user_permission() -> int: return os.geteuid()

def get_list(path: str) -> list | None:
    if not is_dir(path): return None
    return os.listdir(path)

def get_file_from_path(path: str) -> str | None:
    if not is_file(path): return None
    if OS_NAME.lower() == 'windows': spl = '\\'
    else: spl = '/'
    return path.split(spl)[-1]

def get_file_name(file: str) -> str | None:
    x = get_file_from_path(file)
    if not x: return x
    return x.split('.')[0]

def get_path_from_file(file: str) -> str:
    x = get_file_from_path(file)
    if not x: return x
    return file.replace(x, '')

def copy_file(file: str, path: str) -> bool:
    if not is_file(file) or not is_dir(path): return False
    shutil.copyfile(file, path)

def run(command: str) -> str:
    if OS_NAME.lower() == 'windows': output = subprocess.run(['powershell.exe', command], shell=True, capture_output=True)
    else: output = subprocess.run(command, shell=True, capture_output=True)
    if output.stderr: return output.stderr.decode()
    else: return output.stdout.decode()

def system(command: str) -> None: os.system(command)

def delete_file(path: str) -> bool:
    if is_file(path=path): os.remove(path=path); return True
    else: return False

def delete_dir(path: str) -> bool:
    if is_dir(path=path): os.rmdir(path=path); return True
    else: return False
