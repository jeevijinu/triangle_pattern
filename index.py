a=int(input("enter value : "))
b=a-1
for i in range(0,a):
    for j in range(0,b):
        print(end=" ")
    b=b-1
    for k in range(0,i+1):
        print("* ",end="")
    print()
