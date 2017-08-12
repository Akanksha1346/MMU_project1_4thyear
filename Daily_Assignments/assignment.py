1.
list=[]

for x in range(2000,3201):
    if x%7==0 and x%5!=0 :
         list.append(str(x))
print (','.join(list))

2.
num=int(raw_input("enter a no."))
n=1
while num>0:
    n=n*num
    num=num-1
print "factorial of a given", n

3.
num=int(raw_input("enter a no."))
d=dict()
for i in range(1,num+1):
    d[i]=i*i
print d

4.
l=[4,5,6]
print l
x=tuple(l)
print x

5.
a=raw_input("enter the string")
words=a.split(',')
words.sort()
print ",".join(words)

6.
a= raw_input("enter the string")
s=a.upper()
print s

7.



8.
a=raw_input("enter the input:")
b={"Digits":0 , "Letters":0}
for c in a:
    if c.isdigit():
        b["Digits"]+=1
    elif c.isalpha():
        b["Letters"]+=1
    else:
        pass
print "Digits",b["Digits"]
print "Letters",b["Letters"]

9.
a=raw_input("enter the input")
b={"Upper":0,"Lower":0}
for c in a:
    if c.islower():
        b["Lower"]+=1
    elif c.isupper():
        b["Upper"]+=1
    else:
        pass
print ("lowercase",b["Lower"])
print ("uppercase",b["Upper"])

10.
a=raw_input("enter the no")
num=x
for x in a.split(","):
    if(x%2!=0):
        print x
