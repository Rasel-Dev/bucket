import os
from optparse import OptionParser
from pathlib import Path
from pyperclip import paste,copy
import shutil


parse = OptionParser()
HUB_DIR = ("templates","snippers")
__BASE__ = f"{Path.home()}/.bucket"
if not (os.path.exists(f"{__BASE__}") and os.path.isdir(f"{__BASE__}")) : os.mkdir(__BASE__)   # check .bucket or Create
HUB = [os.path.join(__BASE__,i) for i in HUB_DIR]

def check():
    for i in HUB:
        if not (os.path.exists(i) and os.path.isdir(i)):
            os.mkdir(i)


def List(arg): ## listing help
    arg = f"{__BASE__}/{arg}"
    if not os.listdir(arg):
        print(f"[!] '{os.path.basename(arg)}' was Empty ")
        return 
    for i in os.listdir(arg):
        print(f"{i}")
        

def clone():  ## only for templates
    print(__BASE__)

def push(arg,title):  #TODO -> FEATURE -> upcoming binary backup
    if arg == 'clip':
        if len(clip_data:=paste()) > 0:
            with open(f"{__BASE__}/snippers/{title}",'w') as files:
                files.write(clip_data)

def grab(arg,others):
    if arg == 'clip':
        if not len(others) == 1: 
            print("You can grap once clip at a time!")
            return
        title=others[0]
        if not title in os.listdir(f"{__BASE__}/snippers"):
            print(f"[!] '{title}' not Found !")
            return 
        with open(f"{__BASE__}/snippers/{title}",'r') as file:
            copy(file.read())
            print(f"[+] '{title}' in clip")
    elif arg == 'template':
        dirs = os.listdir(f"{__BASE__}/templates")
        if not len(others) > 0:
            print("You should choose any template's")
            return
        for title in others:
            if not title in dirs:
                print(f"[!] '{title}' not found !")
            else:
                if os.path.isdir(f"{__BASE__}/templates/{dirs[(dir_index:=dirs.index(title))]}"):
                    shutil.copytree(os.path.isdir(f"{__BASE__}/templates/{dirs[dir_index]}"),f"{os.getcwd()}/{title}")
                elif os.path.isfile(f"{__BASE__}/templates/{dirs[dir_index]}"):
                    shutil.copy(os.path.isfile(f"{__BASE__}/templates/{dirs[dir_index]}"),f"{os.getcwd()}/{title}")



            print(title)
        return