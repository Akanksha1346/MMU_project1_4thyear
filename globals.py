# global variables and constants.
from termcolor import colored
from steganography.steganography import Steganography
import colorama
colorama.init()
#Red Color=> Error, Green Color=>Success Message
# current status message is initialized to None.
current_status_message = None

# list to store status messages.
STATUS_MESSAGES = ["Spy is Online", "Busy, Call If Urgent"]

friends=[]
#Spy Class
class Spy:
    def __init__(self,salutation,name,age,rating,is_Online):
        #Assigning Values
        self.Name=salutation+"."+name
        self.Age=age
        self.Rating=rating
        self.is_Online=is_Online
        self.chat=[]
    def displayDetails(self):
        print self.Name," ",self.Age
    def calcAverageWords(self):
        #Average Words Spoken
        avg=0
        if len(self.chat)!=0:
            for i in self.chat:
                avg=avg+len(Steganography.decode(i.Message))
            avg=avg/(len(self.chat))
        print "Average Words Spoken: ",avg
#Chat class
class Chat:
    def __init__(self,msgImage,timestamp):
        #Assigning Values
        self.Message=msgImage
        self.Timestamp=timestamp
    def displayMessage(self):
        print colored(self.Timestamp,'blue'),"\nMessage: ",self.Message,"\n"
