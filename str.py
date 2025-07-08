def stng(s):
    lst=list(s)
    for i in range(len(s)):
        if i%2==0:
            lst[i]=lst[i].upper()
    print(lst)

s=input("enter a string")
print(stng(s))