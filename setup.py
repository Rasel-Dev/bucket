from os.path import exists, isdir, join as path_join, isfile
from os import getcwd, mkdir, system
from shutil import copytree, copy2
from pathlib import Path


red = "\033[31;1m"
blue = "\033[34;1m"
pink = "\033[35;1m"
cyan = "\033[36;1m"
green = "\033[32;1m"
white = "\033[37;1m"
reset = "\033[00;1m"
yellow = "\033[33;1m"
root_core = path_join(Path.home(), ".BucketCore")
root_path = [path_join(getcwd(), root) for root in ["bin", "bucket.py"]]


def install():
    if not exists(root_core):
        try:
            mkdir(root)
        except Exception as e:
            print(e)
    if exists(root_path[0]) and isdir(root_path[0]):
        copytree(root_path[0], path_join(root_core, "bin"), dirs_exist_ok=True)
    if exists(root_path[1]) and isfile(root_path[1]):
        copy2(root_path[1], root_core)
        system(f"sudo ln -r -s {path_join(root_core,'bucket.py')} /bin/bucket")
        system(f"sudo chmod +x /bin/bucket")


def setup() -> None:
    if exists("/bin/bucket"):
        print(f"{yellow}[!]{white} already {red}exists{white} Do you want to reinstall {green}bucket{white} ? [{green}Y{white}/{red}N{white}] ", end="")
        answer = input()
        if answer == "Y" or answer == "y":
            print(f"{green}[+] {white}Checking Pip Requirements.......{green}",end="")
            system("python3 -m pip install -r requirements.txt >/dev/null 2>&1")
            print(f"OK{white}")
            try:
                system("sudo rm -rf /bin/bucket")
                install()
                print(f"{green}[+]{white} Successfully installed Type \033[32;5m'bucket -h'{reset}")
            except Exception as e:
                print(e.__context__)
        return
    else:
        print(f"{green}[+] {white}Checking Pip Requirements.......{green}",end="")
        system("python3 -m pip install -r requirements.txt >/dev/null 2>&1")
        print(f"OK{white}")
        try:
            install()
            print(f"{green}[+]{white} Successfully installed Type \033[32;5m'bucket -h'{reset}")
        except Exception as e:
            print(e.__context__)


setup()
