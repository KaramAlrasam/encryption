import string
userList=[]
myString=string.ascii_letters
def mysteres(sentence,num):
    userList.append(sentence)
    userList.append(num)
    mLetter=""
    for letter in sentence:
        if letter==" ":
            mLetter+=" "
        for index in range(len(myString)):
            if myString[index]==letter and index+num in range(len(myString)) :
                mLetter+=myString[index+num] 
            elif myString[index]==letter and index+num not in range(len(myString)) :
                mLetter+="Z"
    userList.append(mLetter)            
    print(mLetter) 
user=input("Enter the sentence: ")
user1=int(input("Enter the number: "))
mysteres(sentence=user,num=user1)
def sillossion():    
    user2=input("Enter the sentence: ")
    user3=int(input("Enter the number: "))
    if user2 == userList[2] and user3==userList[1]:
       print(userList[0])
    else:
       print("Invaled input!!!")

sillossion()    
