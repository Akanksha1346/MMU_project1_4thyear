a=input("enter your choice :1.addition\n 2.subtraction\n 3.multiplication\n 4.division \n")
b=input("enter 1st no.:")
c=input("enter 2nd no.:")
if a==1:

    result=b+c
    print result

elif a==2:
    result=b-c
    print result
elif a==3:
    result=b*c
    print result
elif a==4:
    result=b/c
    print result
else:
    print "wrong input"