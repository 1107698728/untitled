#1
a=int(input("请输入a的值："))
b=int(input("请输入b的值："))
c=int(input("请输入c的值："))
d=int(input("请输入d的值："))
print(a+b-c*d)
#2
s=0
for i in range(1,100):
    if i%3==0:
        s+=i
print(s)
#3
for i in range(1,10):
    if i%2==1:
        print(i)
#4
S1=0
S2=0
for i in range(1,101):
    if i%2==0:
        S1+=i
    else:
        S2+=i
print(S1-S2)
#5
S=0
for i in range(1,101):
    S+=i
print(S)
#6
n=int(input("请输入要判断的数："))
if n%3==0 and n%5==0:
    print("这个数能够同时被3和5整除")
#7
n=int(input("请输入要判断的数："))
if n in range(1,101):
    print(n)
#8
x=int(input("请输入x的值："))
y=int(input("请输入y的值："))
z=int(input("请输入z的值："))
if x>y:
    a=x
    x=y
    y=a
if x>z:
    a=x
    x=z
    z=a
if y>z:
    a=y
    y=z
    z=a
print(x,y,z)
#9
y=int(input("请输入学生成绩："))
x="A" if y>90 else "B" if y>60 else ""
print(x)
#10
a=[1,2]
b=[3,4]
a+=b
print(a)
#11
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print(i,"*",j,"=",i*j,end=" ")
    print("\n")
#12
str=input("请输入字符串：")
s=0
k=0
n=0
o=0
for i in list(str):
    if (ord(i)>65 and ord(i)<=89) or (ord(i)>90 and ord(i)<=121):
        s+=1
    elif ord(i)>48 and ord(i)<=57:
        n+=1
    elif ord(i)==32:
        k+=1
    else:
        o+=1
print("字母的数量是：",s,"空格的数量是：",k,"数字的数量是：",n,"其他字符的数量是：",o)
#13
a=int(input("请输入数字："))
n=int(input("请输入最大数位数："))
x=0
s=0
for i in range(n):
    x+=a*10**(i)
    print(x)
    s+=x
print(s)
#14
j=0
for i in range(7):
    if i<4:
        j+=1
    else:
        j-=1
    print(" " * (4 - j) + "*" * (j*2-1))