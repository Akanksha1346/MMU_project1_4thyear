#import statements
from spy_details import spy
from start_chat import start_chat
from add_status import add_status
print("let's get started")
question="Do you want to continue as" +spy['salutation']+ " " +spy['name']+ "(Y/N)?:"
existing=raw_input(question)

#validating users input
if (existing.upper()=="Y"):
    start_chat(spy['Name'],spy['age'],spy['rating'],spy['is_online'])
elif(existing.upper()=="N"):
    spy_name = raw_input("provide your name here:")

    # to check the length of spy name whether it has any input or not
    if len(spy_name) > 0:

        spy['salutation'] = raw_input("what should we call you?:")
        # concatenation of salutation and name
    spy['age']=raw_input("enter spy's age:")
# age limit on the spy_name
    if spy['age'] > 12 and spy['age'] < 50:
        print "Rigth now! you are not eligible to be spy"
    spy['rating'] = float(raw_input("spy rating is:"))
    if spy['rating'] > 4.5:
        print "you are great"
    elif spy['rating'] >= 3.5 and spy['rating'] <= 4.5:
        print "you are good"
    elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
        print "you are average"
    else :
         print "you are below average"



         print "welcome %s %s Glad to have you with us" % (spy_name, spy['salutation'])
         print 'alright ' + spy_name + " " "I'd like to know little bit more about u before we proceed further"
    spy_is_online=True
else:
    print"A spy needs to have a valid name,Please try again"




