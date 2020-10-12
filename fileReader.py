import re
import urllib3
import threading
from colorama import Fore, init

http = urllib3.PoolManager()

#Class to manage and store url information
class Link: 
    def __init__(self,url):
        self.linkUrl = url
        self.linkStatus = None
        self.linkValid = None
        self.linkInfo = ""
    def checkStatus(self,option):
        init()
        try: 
            self.linkStatus = http.request('HEAD', self.linkUrl).status
            if self.linkStatus == 200: 
                self.linkValid = 'good'
            elif self.linkStatus == 400 or self.linkStatus == 404: 
                self.linkValid = 'bad'
            else: 
                self.linkValid = "unknown"
        except urllib3.exceptions.HTTPError or urllib3.exceptions.ConnectionError as e: 
            self.linkValid = "unknown"
            self.linkStatus = "failed to establish a connection"
        if option == 4: 
            self.linkInfo = '{ \"url\": \'' + self.linkUrl + '\', \"status\":' + str(self.linkStatus) +' }'
        else: 
            self.linkInfo =  self.linkUrl + " is a " + self.linkValid + " link with a HTTP status of " + str(self.linkStatus)
            
        if self.linkStatus == 200: 
            if option != 2:
                print(Fore.GREEN + self.linkInfo)
        elif self.linkStatus == 400 or self.linkStatus == 404: 
            if option != 1:
                print(Fore.RED + self.linkInfo)
        else: 
            if option != 1:
                print(Fore.YELLOW + self.linkInfo)

#Class to manage and store file information
class TextFile: 
    def __init__(self,filePath):
        # try to read and store file information, catch fileNotFound and IO errors
        try:
            self.fileText = open(filePath, 'r').read()
            self.fileUrls = set(re.findall('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', self.fileText))
            self.fileLinks = [Link((url[0]+"://" + url[1] + url[2])) for url in self.fileUrls]
        except IOError as e:
            print("File was unable to be read") 
            self.fileText = None    
        except FileNotFoundError as e: 
            self.fileText = None
            print("File was not found")
        
    def checkLinkStatuses(self,option):
        # use multithreading for http requests
        self.fileThreads = [threading.Thread(target=url.checkStatus(option)) for url in self.fileLinks]
        for thread in self.fileThreads: 
            thread.start()
        for thread in self.fileThreads: 
            thread.join()
        
            
    










