#import statements
from spy_details import spy
from start_chat import start_chat
from add_status import add_status
from termcolor import colored
import re



print("let's get started")
all=True
#check variable to iterate if value is not Y/N
while all:
    question="Do you want to continue as" +spy['salutation']+ " " +spy['name']+ "(Y/N)?:"
    existing=raw_input(question)

#validating users input
if (existing.upper()=="Y"):
    # default user
    all= False
    start_chat(spy.Name,spy.Age,spy.Rating,spy.is_online)
elif(existing.upper()=="N"):
    all = False
    check_all = True  # temporary variable
    while (check_all):
        temp_check = True  # temporary variable
        # Validation Using Regex
        patternsalutation = '^Mr|Ms$'
        patternname = '^[A-Za-z][A-Za-z\s]+$'
        patternage = '^[0-9]+$'
        patternrating = '^[0-9]+\.[0-9]$'
        # Validating Each Values Using Regular Expression
        while temp_check:
            salutation = raw_input("Mr. or Ms.? : ")
            if (re.match(patternsalutation, salutation) != None):
                tempcheck = False
            else:
                print colored("Enter Again!!!!", 'red')
        temp_check = True
        while temp_check:
             spy_name = raw_input("provide your name here:")
        if (re.match(patternname, spy.Name) != None):
            tempcheck = False
        else:
            print colored("Enter Again!!!!", 'red')
            # concatenation.
        spy.Name = spy.Salutation + "." + spy.Name
    temp_check = True
    while temp_check:
        spy.Age= raw_input("Your Age?")
        if (re.match(patternage, spy.Age) != None):
            temp_check = False
            spy.Age= int(spy.Age)
        else:
            print colored("Enter Again!!!!", 'red')

    tempcheck = True
    while temp_check:
        spy.Rating = raw_input("Spy rating?")
        if (re.match(patternrating, spy.Rating) != None):
            tempcheck = False
            spy.Rating = float(spy.Rating)
        else:
            print colored("Enter Again!!!!", 'red')

            # Checking If Spy is eligible
            if spy.Rating <= 5.0 and spy.Age > 12 and spy.Age < 50:
                start_chat(spy.Name, spy.Age, spy.Rating, spy.is_Online)
                wholecheck = False
            else:
                print colored("Invalid Entry!!!!Start From Scratch.", 'red')
    else:
        print colored("Wrong choice. Try again", 'red')

