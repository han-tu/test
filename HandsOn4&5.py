yourString = input("Insert a string : ")
yourString.lower()
myString = ""

for i in range(len(yourString)) :
    if yourString[i] != ' ' :
        myString += yourString[i]

half = (int) (len(myString) / 2)
flag = 0

for i in range(half) :
    if myString[i] != myString[len(myString) - i - 1] :
        flag = 1

if flag == 1 :
    print(f'"{yourString}" is Not a Palindrome')
else :
    print(f'"{yourString}" is a Palindrome')
