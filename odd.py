def odd(s):
    lst=list(s)
    for i in range(len(s)):
        if i%2!=0:
            lst[i]=lst[i].upper()
    return lst
s=input("enter a str")
print(odd(s))