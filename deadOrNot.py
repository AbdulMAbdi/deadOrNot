import argparse
import fileReader
import threading
import sys
from termcolor import colored
import colorama


parser = argparse.ArgumentParser(description="Determine status of link in file",
                                 epilog="""The CLI takes a file path (relative or absolute)
                                        and reads and parses it for urls to check their http status""")

#take file names as an argument on command line
parser.add_argument("files", nargs="+")
#create command line option to output live links only
parser.add_argument('-g', '--good', action='store_true', 
                    help="Outputs only live links")
#create command line option to output dead and unknown status links only
parser.add_argument('-b', '--bad', action='store_true', 
                    help="Outputs only dead links")
#create command line option to output all links
parser.add_argument('-a', '--all', action='store_true', 
                    help="Outputs all links")
#create command line option for general information
parser.add_argument('-in', '--info', action='store_true',
                    help="Outputs overall information about links in file, i.e how many live or dead links there are")
#create command line option to output in JSON format
parser.add_argument('-j', '--json', action='store_true',
                    help="Outputs links in json format")
#create command line option to ignore specified link patterns
parser.add_argument('-i', '--ignore', nargs=1,
                    help="Outputs the links that do not match the provided pattern")


def processFile(file,option):
    colorama.init()
    argFile = fileReader.TextFile(file)
    processLinks(file,argFile,option)


def processFileWithIgnore(file,pattern,option):
    colorama.init()
    argFile = fileReader.TextFile(file)
    for link in argFile.fileLinks:
        argFile.compareLinks(link.linkUrl,pattern)
        if argFile.match:
            argFile.fileLinks.remove(link)
    processLinks(file,argFile,option)


def processLinks(file,argFile,option):
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
def processArguments(argsNormal,option):
    for arg in argsNormal:
        threading.Thread(target=processFile(arg,option)).start()


#take command line files and create thread for each file, while ignoring specified links
def processArgumentsWithIgnore(argsWithIgnore,pattern,option):
    for arg in argsWithIgnore:
        threading.Thread(target=processFileWithIgnore(arg,pattern,option)).start()


#run argparse -help option if no arguments entered on command line
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)


def ignoreOptionFilter(args):
    if args.good:
        processArgumentsWithIgnore(args.files, ignoreLink.fileLink[0].linkUrl, 1)
    elif args.bad:
        processArgumentsWithIgnore(args.files, ignoreLink.fileLink[0].linkUrl, 2)
    elif args.info:
        processArgumentsWithIgnore(args.files, ignoreLink.fileLink[0].linkUrl, 3)
    elif args.json:
        processArgumentsWithIgnore(args.files, ignoreLink.fileLink[0].linkUrl, 4)
    else:
        processArgumentsWithIgnore(args.files, ignoreLink.fileLink[0].linkUrl, 0)


#parse arguments
args = parser.parse_args()
if args.good:
    processArguments(args.files,1)
elif args.bad:
    processArguments(args.files,2)
elif args.info:
    processArguments(args.files,3)
elif args.json:
    processArguments(args.files,4)
else: 
    processArguments(args.files,0)











