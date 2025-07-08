def even(s):
    lst=[]
    for i in range(len(s)):
        lst.append(s[i])

        if i%2==0:
            lst[i].upper()
    print(lst)
s=input("enter a string")
even(s)