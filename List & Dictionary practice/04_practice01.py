B_E_dic = {
    "lathi":"stick",
    "chula": "stove",
    "potaka": "flag"
}
key = input("Enter your key :\n")
if (B_E_dic.get(key)== None):
    print("Value not found")
else:
    print("The value corresponding to key is :",B_E_dic.get(key))
