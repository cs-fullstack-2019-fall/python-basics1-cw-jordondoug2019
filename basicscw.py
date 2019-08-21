#Problem1
myNameis= "My name is: "
myName= "Jordon"
print(myNameis + myName)

#Problem2
userExtraCredit=int(input("Please Enter the Extra Credit Earned: "))
if(userExtraCredit<5):
    print("Thats not enough extra credit")
elif(userExtraCredit>20):
    print("Thats too much extra credit")

 #Problem3
userPassword= input("Enter a Password: ")
userpassword2= input("Enter a Password: ")
if(userPassword==userpassword2):
    print("you are correct")

 #Problem4
card=int(input("Card number1:"))
card1=int(input("enter card number 2: "))
sum= card+card1
if (sum== 21):
    print("Blackjack!")
elif(sum >21):
    print("Bust")
elif(sum<21):
    print("The total is :" + str(sum))
