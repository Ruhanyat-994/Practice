'''A multiplication table of your desired number'''

number=int(input("Enter your number : \n"))
for item in range(10):
    print(f"{number}X{item+1}={number*(item+1)}")