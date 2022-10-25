from os import mkdir,listdir,getcwd
from os.path import (
    exists,
    isdir,
    isfile,
    join as path_join,
    basename,
)
from optparse import OptionParser
from pathlib import Path
from pyperclip import paste,copy
import shutil
from tabulate import tabulate
from colorama import init

## ------------- Variable -------------- ##
red, green, yellow, white, reset  = ("\033[31;1m", "\033[32;1m", "\033[33;1m", "\033[37;1m", "\033[00;1m")
parse = OptionParser()
HUB_DIR = ("templates","snippers")
__BASE__ = path_join(Path.home(),".bucket")
if not (exists(f"{__BASE__}") and isdir(f"{__BASE__}")) : mkdir(__BASE__)   # check .bucket or Create
HUB = [path_join(__BASE__,i) for i in HUB_DIR]

## -------------- functions -------------- ##

def divide_chunks(l, n):
    """Divide Array Into EQual Parts"""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def check():
    for i in HUB:
        if not (exists(i) and isdir(i)):
            mkdir(i)


def List(arg): ## listing help
    arg = path_join(__BASE__,arg)
    if not listdir(arg):
        print(f"\n{yellow}[!] {red}'{basename(arg)}'{white} was Empty \n")
        return 
    print("\n"+tabulate(list(divide_chunks(listdir(arg),4)),tablefmt="rounded_grid"),"\n")
        

def clone():  #TODO -> Create ->Template Clone
    print(__BASE__)

def push(arg,title):  #TODO -> FEATURE -> upcoming binary backup
    if arg == 'clip': #TODO -> Need To Fix -> Override existed files
        if not title:
            print(f"{yellow}[!]{white} you must specify a {red}title\n{green}[+] {white}use {green}--title {white}to set the {green}title")
            return
        clip_write_filename = path_join(HUB[-1],title)
        if len(clip_data:=paste()) > 0:
            with open(clip_write_filename,'w') as files:
                files.write(clip_data)
            print(f"{green}[+]{white} Clip written to {green}'{basename(clip_write_filename)}'{white} successfully created")

def grab(arg,others):
    if arg == 'clip':
        if not len(others) == 1: 
            print(f"\n{yellow}[!] {red}You can grab once clip at a time!\n")
            return
        title=others[0]
        if not title in listdir(HUB[-1]):
            print(f"{yellow}[!] {red}'{title}'{white} not Found !")
            return 
        with open(path_join(HUB[-1],title),'r') as file:
            copy(file.read())
            print(f"\n{green}[+] '{title}'{white} added in clip\n")
    elif arg == 'template':
        dirs = listdir(HUB[0])
        if not len(others) > 0:
            print("[!] You should choose any template's")
            return
        for title in others:
            if not title in dirs:
                print(f"[!] '{title}' not found !")
            else:
                if isdir(path_join(HUB[0],dirs[(dir_index:=dirs.index(title))])):
                    shutil.copytree(path_join(HUB[0],dirs[dir_index]),path_join(getcwd(),title))
                elif isfile(path_join(HUB[0],dirs[dir_index])):
                    shutil.copy(path_join(HUB[0],dirs[dir_index]),path_join(getcwd(),title))
            print(title)
        return



if __name__ == "bin":
    init()
    check()