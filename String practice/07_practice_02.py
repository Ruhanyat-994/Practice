


name=input("enter the name: ")
date = input("enter the date: ")

templete= '''
Dear <|name|>, 
you are selected
<|date|>
'''
print(templete.replace("<|name|>",name).replace("<|date|>",date))