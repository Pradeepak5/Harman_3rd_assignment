list1=[]
count=int(input("Enter the count : "))
for i in range(0,count):
    a=int(input("enter number : "))
    list1.append(a)

print(list1)
sqr=list(map(lambda x:x*x,list1))
print(sqr)
cube=list(map(lambda x:x**3,list1))
print(cube)