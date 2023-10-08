'''
#Program 1
a,b=5,10
a,b=b,a
print(a,b)

#Program 2
length=int(input())
breadth=int(input())
area=length*breadth
print(area)

#Program 3
ctemp= int(input())
ftemp= (ctemp*(9/5))+32
print(ftemp)

## String based questions ##

#Program 1
x=input()
count=0
for i in x:
    count+=1
print(count)

#Program 2
x=input()
count=0
for i in x:
    if i in ("a","e","i","o","u","A","E","I","O","U"):
        count+=1
print(count)

#Program 3
x=input()
rev=x[::-1]
print(rev)

#Program 4
x=input()
rev=x[::-1]
if rev==x:
    print("panlindrome")
else:
    print("not palindrome")
'''
#Program 5
x=input()
new_word=x.replace(" ","")
print(new_word)
