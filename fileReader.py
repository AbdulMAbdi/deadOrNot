import re
import urllib3
import threading
from termcolor import colored
import colorama

colorama.init()
http = urllib3.PoolManager()

#Class to manage and store url information
class Link: 
    def __init__(self,url):
        self.linkUrl = url
        self.linkStatus = None
        self.linkValid = None
    def checkStatus(self,option): 
        try: 
            self.linkStatus = http.request('HEAD', self.linkUrl).status
        except urllib3.exceptions.HTTPError or urllib3.exceptions.ConnectionError or urllib3.exceptions.TimeoutError as e: 
            self.linkValid = "Unknown"
        
        if self.linkStatus == 200: 
            self.linkValid = "Good"
            if option == 0 or option == 1:
                print(colored(self.linkUrl + " is a " + self.linkValid + " link", 'green'))
        elif self.linkStatus == 400 or self.linkStatus == 404: 
            self.linkValid = "Bad"
            if option == 0 or option == 2:
                print(colored(self.linkUrl + " is a " + self.linkValid + " link", 'red'))
        else: 
            self.linkValid = "Unknown"
            if option == 0 or option == 2:
                print(colored(self.linkUrl + " is an " + self.linkValid + " link", 'yellow'))

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
        
            
    










