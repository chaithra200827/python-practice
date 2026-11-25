'''a=5j
print(a)'''
'''a ="happy father's day"
print(a)'''
'''a = [10,2.3,True,'hello']
a.append(10)
print(a)
a.remove(True)
print(a)
a.pop(0)
print(a)'''
'''a=10,20,30
print(a,type(a))
a={10,2,3,(1,2),'hi'}
print(a)'''
'''a={'a':[10,20,30],'b':40}
print(a['a'][-2])'''
'''a="HELLO"
print(a[1:3+1:2])'''
'''a="hello"
print(a[::-1])'''
'''a="good morning"
print(a[1:5+1:2])'''
'''a='good morning' 
print(len(a[10:4-1:-3]))'''
'''a=eval(input("enter:"))
print(a,type(a))'''
'''a=int(input("enter:"))
if (a%2==0):
    print("even")
else:
    print("odd")
'''
'''l=eval(input("enter:"))
if len(l)==5:
    print("yes")
else:
    print("no")
'''
'''ch=input("enter:")
if "A"<=ch<="Z":
    print("upper")
elif "a"<=ch<="z":
    print("lower")
else:
    print("not an alphabet")

'''
'''un=input("enter:")
if un=="chaitragowda":
    print("correct")
    pw=input("enter:")
    if pw=="ilovemath":
        print("sucessfully logged in")
    else:
        print("incorrect password")
else:
    print("incorrect username")
'''
'''i=1
while i<=100:
    print(i)
    i+=1
'''
'''i=2
while i<=50:
        if(i%2==0):
         print(i)
        i+=2
    '''

'''n=int(input("enter num:"))
rev=0'''

'''while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)
    
    '''
'''for i in range(1,100):
    print(i)'''

'''l=[10,20,30]
for i in l:
    print(i)'''



'''s=input("enter:")
out=''
for i in s:
    if 'A'<=i<='Z':

        out+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''


'''
s=input("enter:")
rev=''

for i in s:
    rev=i+rev
print(rev)'''


'''for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print()'''

for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print('&',end=' ')
        else:
            print('%',end=' ')
    print()   


 
              
    