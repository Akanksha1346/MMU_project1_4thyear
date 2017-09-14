from globals import friends
def select_friend():

    item_number=0
    for friend in friends:
        print  '%d. %s' % (item_number + 1), friend['name']
        item_number=item_number+1
    friend_choice=raw_input("choose from your friends")
    friend_choice_position=int(friend_choice)-1
    return friend_choice_position