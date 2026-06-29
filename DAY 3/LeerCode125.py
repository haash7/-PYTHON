text = input("Enter the text")
text = text.replace(" ","")
text = text.lower()
reverse = text[::-1]
print(text)
if reverse==text:
    print("True")
else:
    print("False")    



text=input("Enter the text")
cleaned=""
for ch in text:
    if ch.isalnum():
        cleaned+=ch.lower()
if cleaned==cleaned[::-1]:
    print(True)
else:
    print(False)    
        