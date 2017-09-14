#start_chat function definition
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
from globals import current_status_message
from read_chat import read_chat
def start_chat(name,age,rating,status):
    #from globals import current_status_message
    show_menu=True
    while (show_menu):
         menu_choices="what do you want to do??\n 1.Add Status \n 2.Exit Application"
         result=int(raw_input(menu_choices))
    if(menu_choices==1):
        print"you choose to update status"
    else:
        show_menu=False
    #validating users input
    error_message='Invalid age....'
    print error_message
    if result==1:
        current_status_message=None

    elif result==2:

        show_menu=False
    else:
        print "wrong input"
    current_status_message=add_status(current_status_message)