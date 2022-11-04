#!/bin/python3

from bin import (
    argv,
    listdir,
    tabulate,
    Main_Class as main,
    basename,
# -------- Color ----------#
    red,
    green,
    yellow,
    blue,
    pink,
    cyan,
    white,
    reset
)

# ------Variable------#
parse = main.parse
root = main()

## -------- function -------- ##
def help_msg():
    print(f"""
██████████████████████████████████████
█▄─▄─▀█▄─██─▄█─▄▄▄─█▄─█─▄█▄─▄▄─█─▄─▄─█
██─▄─▀██─██─██─███▀██─▄▀███─▄█▀███─███
▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀

Usage: {basename(argv[0])} [options]

Options:
  -d                    Delete the unnecessary Data
  -g                    Grab The data from your bucket
  -L                    list of Bucket Directory
  --title               Set The Title for clip content
  --push                push Data into your bucket
  -c, --clone           set the Template for Push
  -l, --list            show list of files in your bucket
  -h, --help            show this help message and exit
  --version             show version and exit

Examples:
  bucket --push clip --title <name> # Save Clip in bucket
  bucket -g clip --title <name>     # grab Clip from bucket
  bucket -l [templates | snippers]  # Show list of templates or snippers
  bucket --push template -c <name>  # push Template in bucket
  bucket -g template <name>         # grab Template from bucket
  bucket -d clip <name>             # delete Clip from bucket
  bucket -d templates <name>        # delete Template from bucket

""")


## ------- Options ------- #
parse.add_option('-g',dest="grab")
parse.add_option('-d','--delete',dest="delete")
parse.add_option('-l','--list',dest="dirlist")
parse.add_option('-L',dest="hubs",action="store_true")
parse.add_option('-c','--clone',dest="Tempclone")
parse.add_option('--push',dest="push")
parse.add_option('--title',dest="title")
parse.add_option('-h','--help',dest="help",action="store_true")

(option,arg) = parse.parse_args()

if option.help:
    help_msg()

elif option.dirlist:
    if option.dirlist in main.HUB_DIR:
        root.ListDir(option.dirlist)
    else:
        print(f"\n{yellow}[!] {red}'{option.dirlist}'{white} is not a valid directory\n\n{green}hint{white}: check {cyan}-L{white} and try again\n")


elif option.hubs == True:
    print("\n"+tabulate([listdir(main.__BASE__)],tablefmt="rounded_grid")+"\n")

elif option.push:
    if option.push == "clip":
        root.push(option.push, option.title)
    elif option.push == "template":
        root.push(option.push, option.Tempclone)
        
    else:
        print(f"\n{yellow}[!]{red} Invalid argument\n{green}[+]{white} Do you mean {yellow}--push {cyan}'clip' {white}|{cyan} 'template'{white} ?")

elif option.grab:
    if option.grab == "clip":
        root.grab(option.grab, option.title)

    elif option.grab == "template":
        root.grab(option.grab, arg)
    else:
        print(f"{red}[-]{white} Invalid argument\n{green}[+]{white} Do you mean {yellow}-g {cyan}'clip' {white}|{cyan} 'template'{white}?")
elif option.delete:
    if option.delete in ["clip","template"]:
        root.Delete(option.delete,arg)
    else:
        print(f"{red}[-]{white} Invalid argument\n{green}hint{white}: use {yellow}--delete {cyan}'clip'{white} or {cyan}'template'{green} <name>{white} to delete")

else:
    print(f"\n{yellow}[!]{red} You must specify arguments\n{green}hint{white}: Check {yellow}--help{white} and try again !")