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