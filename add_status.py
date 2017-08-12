STATUS_MESSAGES=['a','b','c']
def add_status(current_status_message_):
    if current_status_message_!= None:
            print"current status is" + current_status_message_

    else:
        print"you don't have any status"

    default=raw_input("do you want to select from the older status(y/n)?")

    if default.upper()=="N":
     new_status_message= int(raw_input("what status message do u want to set?"))
    if len(new_status_message)>0:
        updated_status_message=new_status_message
        STATUS_MESSAGES.append(new_status_message)
    elif default.upper()=="Y":
        item_position=1
        for message in STATUS_MESSAGES:
         print str(item_position)+ "." + str(message)

        item_position=item_position+1
    message_selection=int (raw_input("\nchoose from the older messages"))
    if len(STATUS_MESSAGES)>= message_selection:
        updated_status_message=STATUS_MESSAGES[message_selection-1]

    return add_status