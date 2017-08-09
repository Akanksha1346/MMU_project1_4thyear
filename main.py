print("let's get started")
spy_name=raw_input("provide your name here:")


#to check the length of spy name whether it has any input or not
if len(spy_name)>0:
    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    spy_salutation = raw_input("what should we call you?:")
    #concatenation of salutation and name

    print "welcome %s %s Glad to have you with us" %(spy_name,spy_salutation)
    print 'alright ' +spy_name+ " " "I'd like to know little bit more about u before we proceed further"

else:
    print"A spy needs to have a valid name,Please try again"

spy_age = raw_input("spy age is:")
print type(spy_age)
spy_age = int(spy_age)
print type(spy_age)
# age limit on the spy_name
if spy_age > 12 and spy_age < 50:
    spy_rating = raw_input("spy rating is:")
else:
    print "Rigth now! you are not eligible to be spy"
#to check how spy will be
if spy_rating>4.9 and spy_rating<4.5:
    print "you are great"
elif spy_rating>3.5  and spy_rating<4.5  :
    print "you are good"
elif spy_rating>2.5 and spy_rating<3.5:
    print "you are average"
else :
    print "you are below average"
