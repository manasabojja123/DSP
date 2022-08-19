t=("manasa","swaroop","praveen","ruchi","swag")
t1=("swarna")
T=tuple(("apple","hello","hi"))
print(t)
print(T)
print(len(t))
print(type(t))
print(type(t1))
print(t[0])
print(t[-2])
print(t[2:3])
print(t[:4])
print(t1[1:])
print(t[-1:-3])
#changing
y=list(t)
y[1]="satish"
x=tuple(y)
print(x)
#adding
y=list(t)
y.append("rasagulla")
t=tuple(y)
print(t)
#removing
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#unpacking
f=("swaroop","mani","sai")
(f1,f2,f3)=f
print(f1)
print(f2)
print(f3)
#hehe
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#looping using for
z=("apple", "banana", "cherry", "strawberry", "raspberry")
for i in z:
    print(i)
for i in range(len(z)):
    print(z[i])
print("*******")
#looping using while
i=0
while(i<len(z)):
        print(z[i])
        i=i+1
#joining
t1=("a","b","c")
t2=(1,2,3)
T=t1+t2
print(T)
print(t1*2)
#methods
x=(1,2,3,4,5,2)
print(x.count(2))
print(x.index(3))


   






