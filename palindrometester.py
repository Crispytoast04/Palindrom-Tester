#palindrometester
#Chrstian Naclerio

keepGoing='y'

while keepGoing=='y':
    phrase=input("Enter your phrase: ")
    newPhrase=phrase.strip().lower().replace(" ","")
    reverse = newPhrase[::-1]
    if( newPhrase == reverse ):
      print(f" {newPhrase} is a Palindrome")
    else:
        print(f" {newPhrase} is a not a Palindrome")
    keepGoing=input("Would you like to enter another phrase: (y,n) ")
    if len(keepGoing) > 0 and keepGoing[0].lower()=="y":
        keepGoing="y"
print("Ok, Goodbye!!!")





