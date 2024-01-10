import random
import math
lower=int(input("enter the lower number"))
upper=int(input("enter the higher number"))
c=random.randint(lower,upper)
print("you have only",round(math.log(upper-lower+1,2)),"chances to guess")
count=0
while count<math.log(upper-lower+1,2):
    count+=1
    z = int(input("enter your guess"))
    if c==z:
        print("you have done it",count)
        break
    elif c>z:
        print("ohh its too small")
    elif c<z:
        print("ohh its too high")
    if count>=math.log(upper-lower+1,2):
        print("better try next time")
