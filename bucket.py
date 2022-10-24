from bin import (
    HUB,
    List,
    parse,
    os,
    clone,
    __BASE__,
    HUB_DIR,
    push,grab
)

from sys import argv

## ---- options ----- #
parse.add_option('-l','--list',dest="dirlist",help=f"Example: -l [{' | '.join(i for i in HUB_DIR)}]",metavar="dirname")
parse.add_option('-L',dest="hubs",help=f"list of hubs",metavar="hub",action="store_true")
parse.add_option('-c','--clone',dest="Tempclone",help="Clone: only for templates",metavar="template")
## ------ Push Section ----- #
parse.add_option('--push',dest="push",help="Example: --push [ clip | template ]",metavar="\b ")
parse.add_option('--title',dest="title",help="Title for clip content",metavar="<name>")
## ------- Grab Section ------- #
parse.add_option('-g',dest="grab",help="Example: -g [ clip | template ]",metavar="\b ")
# parse.add_option('--title',dest="title",help="Title for clip content",metavar="<name>")

(option,arg) = parse.parse_args()

if option.dirlist in HUB_DIR:
    List(option.dirlist)
elif option.Tempclone in os.listdir(f"{__BASE__}/templates/"):
    clone()
elif option.hubs == True:
    print(", ".join(os.listdir(__BASE__)))
elif option.push in ["clip","template"]:
    push(option.push,option.title)
elif option.grab in ["clip","template"]:
    grab(option.grab, arg)