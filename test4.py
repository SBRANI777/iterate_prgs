import random
i=1
while(i<4):
    rnm=random.randint(1,9)
    n=int(input("guess the number:"))
    if n<rnm and (i==1 or i==2):
        print("too low",{rnm})
        print("----------------------------------")
    elif n>rnm and (i==1 and i==2):
        print("too high",{rnm})
        print("-------------------------------")
    elif n==rnm:
        print("right ans",{rnm})
        break
    else:
        if i==3:
            print("game over")
    i=i+1
    