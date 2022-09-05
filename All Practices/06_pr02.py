m1 = int(input("Enter your marks no 1:"))
m2 = int(input("Enter your marks no 2:"))
m3 = int(input("Enter your marks no 3:"))

overall=(m1+m2+m3)/3

if(overall>= 40):
    if(m1>=33 and m2>=33 and m3>= 33):
        print("You have passed the exam")
    else:
        print("You have not passed the exam due to fail in each subject")
else:
    print("You have not passed the exam due to overall marks")