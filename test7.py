#Let us make the above game a little more interesting by converting it into a gambling  problem. 
#Suppose that a player starts with Rs. 1,000. 
#If a player can guess the number in his  first chance, then he will be given a prize of Rs. 5,000, if he requires 2 attempts 
#then he will  get a prize of Rs.1,000. If he loses then he will lose Rs. 500. For example the game should go  like this: 
#You have a cash of Rs. 1,000 with you...  
#Guess the number: 8 
#Too high 
#Guess the number: 3 
#You have just won Rs. 1,000
#Your balance: Rs. 2000 
#see this properly
import random
money=1000
i=1
while(i<4):
    rn=random.randint(1,10)
    n=int(input("enter n:"))
    if n<rn and (i==1 or i==2):
        print("too low")
    elif n>rn and (i==1 and i==2):
        print("too high")
    elif n==rn and i==1:
        print("you got the prize money of 5000")
        print("current balance=",money+5000)
        break
    elif n==rn and i==2:
        print("you win the prize money of 1000")
        print("current balance=",money+2000)
        break
    else:
        if i==3:
         print("sorry you lost")
         print("balance is=",money-500)
    i=i+1
    



