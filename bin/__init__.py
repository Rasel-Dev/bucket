from os.path import (
    exists,
    isdir,
    isfile,
    join as path_join,
    basename,
    split as path_split
)
from os import (
    mkdir,
    listdir,
    getcwd,
    remove as os_remove
)
from optparse import OptionParser
from pathlib import Path
from pyperclip import paste, copy
from shutil import (
    copy2,
    copytree,
    rmtree
)
from tabulate import tabulate
from colorama import init
from sys import argv

# -------------[Color]-----------------#

red = "\033[31;1m"
blue = "\033[34;1m"
pink = "\033[35;1m"
cyan = "\033[36;1m"
green = "\033[32;1m"
white = "\033[37;1m"
reset = "\033[00;1m"
yellow = "\033[33;1m"

# --------------[Main_Class]--------------#

class Main_Class:
    
    parse = OptionParser(add_help_option=False,version="%prog 1.0a")
    HUB_DIR = ("templates","snippers")
    __BASE__ = path_join(Path.home(),".bucket")

    def __init__(self):
        self.root_filename = lambda filename,i: path_join(self.__BASE__,self.HUB_DIR[i],filename)
        self.HUB = list(path_join(self.__BASE__,i) for i in self.HUB_DIR)
        self.answer = ""
        if not exists(self.__BASE__) and not isdir(self.__BASE__): mkdir(self.__BASE__)
        self.__check()

    def __divide_chunks(self,array: list=[], Step: int=4):
        for i in range(0,len(array),Step):
            yield array[i:i+Step]
    
    def __check(self):
        for _dir in self.HUB:
            if not isdir(_dir):
                mkdir(_dir)

    def ListDir(self,arg:str):
        arg = path_join(self.__BASE__,arg)
        if not exists(arg):
            print(f"\n{yellow}[!] {red} '{basename(arg)}' {white} was not found!\n")
            return self
        if not listdir(arg):
            print(f"\n{yellow}[!] {red}'{basename(arg)}' {white} was empty !\n")
            return self
        print("\n"+tabulate(list(self.__divide_chunks(listdir(arg),4)),tablefmt="rounded_grid"),"\n")
        return self
    
    def push(self,arg:str,title:list):       #TODO: Binary Cache
        if arg == "clip":
            if not title:
                print(f"{yellow}[!]{white} you must specify a {red}'title'{white} for the clip\n{green}[+] {white}use {green}--title {white}to set the {green}title")
                return self

            clip_dst = self.root_filename(title,1)
            
            if not len(clip_data:=paste()) > 0:
                print(f"{yellow}[!] {red}'Clip' {white} was empty!\n")
                return self

            if exists(clip_dst):
                print(f"{yellow}[!] {red} already exists {white}\nDo you want to overwrite Or Rename [O/R/N] ",end="")
                try: self.answer = input()
                except KeyboardInterrupt:
                    print(f"{yellow}[!] Ctrl+C {red}Abort{white} Operation !")
                    quit()
                if (self.answer == "n" or self.answer == "N"):
                    print(f"{yellow}[!] {red}Abort{white} Operation !")
                    return self
                elif self.answer == "r" or self.answer == "R":
                    try: rename = input("Enter a new name: ")
                    except KeyboardInterrupt:
                        print(f"{yellow}[!] Ctrl+C {red}Abort{white} Operation !")
                        quit()

                    if rename.strip():
                        clip_dst = self.root_filename(rename,1)
                        title = rename
                else:
                    self.answer = 'o'
                    
            with open(clip_dst,"w") as f:
                f.write(clip_data)
            print(f"{green}[+] '{title}' {white} successfully {'Stored' if not (self.answer.lower() == 'o') else 'Overwrite'}")
        
        if arg == "template":        #TODO: Archive Cache
            if not title:
                print(f"{yellow}[!]{white} you must specify a {red}'Clone'\n{green}[+] {white}use {green}--clone {white}to set the {green} 'Clone Name'")
                return self

            template_src = path_join(getcwd(),title)
            template_dst = self.root_filename(basename(title),0)

            if not exists(template_src):
                print(f"{yellow} [!] {red}'{title}' {white} was not found !")
                return self

            if isdir(template_src):

                if exists(template_dst):
                    print(f"{yellow}[!] {red} already exists {white}\nDo you want to overwrite Or Rename[O/R/N] ",end="")
                    try: self.answer = input()
                    except KeyboardInterrupt:
                        print(f"{yellow}[!] Ctrl+C {red}Abort{white} Operation!")
                        quit()
                    if (self.answer == "n" or self.answer == "N"):
                        print(f"{yellow}[!] {red}Abort{white} Operation !")
                        return self
                    elif self.answer == "r" or self.answer == "R":
                        try: rename = input("Enter a new name: ")
                        except KeyboardInterrupt:
                            print(f"{yellow}[!] Ctrl+C {red}Abort{white} Operation!")
                            quit()
                        if rename.strip():
                            template_dst = self.root_filename(rename,0)
                            title = rename
                    else:
                        self.answer = 'o'
                copytree(template_src,template_dst)
                print(f"{green}[+] '{title}' {white} successfully {'Copied' if not (self.answer.lower() == 'o') else 'Overwrite'}")
                return self

            elif isfile(template_src):
                if exists(template_dst):
                    print(f"{yellow}[!] {red} already exists {white}\nDo you want to overwrite Or Rename[O/R/N] ",end="")
                    try: self.answer = input()
                    except KeyboardInterrupt:
                        print(f"{yellow}[!] Ctrl+C {red}Abort{white} Operation!")
                        quit()

                    if (self.answer == "n" or self.answer == "N"):
                        print(f"{yellow}[!] {red}Abort{white} Operation !")
                        return self
                    elif self.answer == "r" or self.answer == "R":
                        try: rename = input("Enter a new name: ")
                        except KeyboardInterrupt:
                            print(f"{yellow}[!] Ctrl+C {red}Abort{white} Operation!")
                            quit()
                        if rename.strip():
                            template_dst = self.root_filename(rename,0)
                            rename = title
                    else:
                        self.answer = 'o'

                copy2(template_src,template_dst)
                print(f"{green}[+] '{title}' {white} successfully {'Copied' if not (self.answer.lower() == 'o') else 'Overwrite'}")
                return self

    def grab(self,arg:str,title:str):
        if arg == "clip":
            if not title:
                print(f"{yellow}[!]{white} you must specify a {red}title\n{green}[+] {white}use {green}--title {white}to set the {green}title")
                return self
            if not title in listdir(self.HUB[1]):
                print(f"{yellow}[!] {red}'{title}' {white} was not found!")
                return self
            with open(self.root_filename(title,1),"r") as f:
                copy(f.read())
            print(f"\n{green}[+] '{title}'{white} added in clip\n")
        
        if arg == "template":
            if not title:
                print(f"\n{yellow}[!]{white} you must give a {red}'Template Name'\n{green}hint: {white}use {yellow}-l {green}templates {white} then.\n{green}hint: {white}use {yellow}-g {green}template {cyan}<name>\n")
                return self
            if not (title:=title[0]) in listdir(self.HUB[0]):
                print(f"{yellow}[!] {red}'{title}' {white} was not found!")
                return self

            template_src = path_join(getcwd(),title)
            template_dst = self.root_filename(basename(title),0)
            
            if isdir(template_dst):
                copytree(template_dst,template_src)
                print(f"{green}[+] '{title}' {white} successfully Copied")
                return self
            else:
                copy2(template_dst,template_src)
                print(f"{green}[+] '{title}' {white} successfully Copied")
                return self
    

    def Delete(self,arg:str,name:str) -> None:
        if arg == "template":
            if not name:
                print(f"{yellow}[!]{white} you must specify a {red}'name'\n{green}hint{white}: use {yellow}--delete {green}template {cyan}<name>")
                return self
            delete_dst = self.root_filename(name[0],0)
            name = name[0]

            if exists(delete_dst) and isdir(delete_dst):
                rmtree(delete_dst)
                print(f"{green}[+] {cyan}'{name}'{white} deleted successfully")
                return self
            elif exists(delete_dst) and isfile(delete_dst):
                os_remove(delete_dst)
                print(f"{green}[+] {cyan}'{name}'{white} deleted successfully")
                return self
            else:
                print(f"{yellow}[!] {red}'{name}' {white} was not found !")
                return self

        elif arg == "clip":
            if not name:
                print(f"{yellow}[!]{white} you must specify a {red}'name'\n{green}hint{white}: use {yellow}--delete {green}clip {cyan}<name>")
                return self
            delete_dst = self.root_filename(name[0],1)
            name = name[0]
            if exists(delete_dst) and isfile(delete_dst):
                os_remove(delete_dst)
                print(f"{green}[+] {cyan}'{name}'{white} deleted successfully")
                return self
            else:
                print(f"{yellow}[!] {red}'{name}' {white} was not found !")
                return self
        