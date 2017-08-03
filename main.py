print("let's get started")
spy_name=raw_input("provide your name here:")
spy_salutation=raw_input("what should we call you?:")

#to check the length of spy name
if len(spy_name)>0:
    new_message="yay!name is not empty"
    print new_message

#concatenation of salutation and name
spy_name=spy_salutation + " " + spy_name


print 'welcome ' +spy_name+ ' Glad to have u back with us'