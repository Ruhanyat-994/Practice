k=1
i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end=" ") #this loop is for spaces
        b+=1
    j=1
    while j<=k:
        print("*",end=" ")#this loop is for stars
        j+=1
    k+=2
    print()
    i+=1