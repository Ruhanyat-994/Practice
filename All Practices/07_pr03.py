spamWords = ['click here','Got it','subscribe it']

email = input("Enter your email :").lower()
spam = False

if("click here" in email):
    spam= True

if("Got it " in email ):
    spam = True
if("subscribe it" in email):
    spam = True 

print("Spam is ",spam)