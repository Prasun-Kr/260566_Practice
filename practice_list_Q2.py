l=list(map(int,input().split(" ")))
n=int(input("enter pos: "))
if n<len(l)-1:
    l[n+1]=l[n]
print(l)