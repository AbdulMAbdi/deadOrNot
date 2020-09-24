import argparse
import fileReader
import threading
import sys
from termcolor import colored
import colorama

colorama.init()

parser = argparse.ArgumentParser(description="Determine status of link in file", epilog="""The CLI takes a file path (relative or absolute)
                                                                                            and reads and parses it for urls to check their http status""")

#take file names as an argument on command line
parser.add_argument("files", nargs="+")
#create command line option to output live links only
parser.add_argument('-g', '--good', action='store_true', 
    help="Outputs only live links")
#create command line option to output dead and unknown status links only
parser.add_argument('-d', '--dead', action='store_true', 
    help="Outputs only dead links")
#create command line option for general information
parser.add_argument('-i', '--info', action='store_true', 
    help="Outputs overall information about links in file, i.e how many live or dead links there are")


def processFile(file,option):
    argFile = fileReader.TextFile(file)
    if argFile.fileText is not None: 
        argFile.checkLinkStatuses(option)
    #info option, get counts for link status types 
    if option == 3: 
        deadLinks = 0 
        liveLinks = 0 
        unknownLinks = 0
        for url in argFile.fileLinks: 
            if url.linkValid == "good": 
                liveLinks += 1
            if url.linkValid == "unknown":
                unknownLinks += 1
            if url.linkValid == "bad":
                deadLinks += 1 
        print("The file " + file + " has " + colored(str(deadLinks) + " dead links ", 'red') + " and " + colored(str(liveLinks) + " live links", "green"))
        print("There are also " + colored(str(unknownLinks) + " unknown links", "yellow"))


#take command line files and create thread for each file
def processArguments(args,option):
    for arg in args:
        threading.Thread(target=processFile(arg,option)).start()

#run argparse -help option if no arguments entered on command line
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

#parse arguments
args = parser.parse_args()
if args.good:
    processArguments(args.files,1)
elif args.dead:
    processArguments(args.files,2)
elif args.info:
    processArguments(args.files,3)
else: 
    processArguments(args.files,0)











