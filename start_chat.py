#start_chat function definition
def start_chat(name,age,rating):
    show_menu=True
    while (show_menu):
         menu_choices="what do you want to do??\n 1.Add Status \n 2.Exit Application"
         result=int(raw_input(menu_choices))

    #validating users input
    if result==1:
        print "simran"
    elif result==2:
        show_menu=False
    else:
        print "wrong input"