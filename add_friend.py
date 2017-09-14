from globals import friends, new_name
from spy_details import spy
def add_friend():
    new_friend={
        'name':'','salutation':'',   'age':0,'rating':0.0  }


    new_friend['name']=raw_input("add your friends name")
    new_friend['salutation']=raw_input("are they ms.or mr??")
    new_friend['name']=new_friend['salutation']+" "+ new_friend['name']
    new_friend['age']=int(raw_input("age??"))
    new_friend['rating']= float(raw_input("spy rating??"))

    if  len(new_friend['name)']>0  and new_friend['age']>12 and new_friend['rating']>=spy['rating']):
         friends.append(new_friend)
    else:
         print "invalid"

    return len(friends)