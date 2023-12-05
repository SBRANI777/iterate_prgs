import random
i=0
while(True):
        n=eval(input("enter value n::"))
        ran=random.randint(1,10)
        if ran==n:
            print("congrats!!you got it")
            break
        else:
            print("sorry try again",{ran})
            print("--------------------------------------------")
            i=i+1
                   
