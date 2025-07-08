def fun(n):
    if n<0:
        print("not possible")
    while n>0:
        t=n
        d=n%10
        print(d)
        n=n//10


n=int(input("enter a number:"))
fun(n)