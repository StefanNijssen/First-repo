
def AgeCheck():
    Name =input("Are you 18 years or older?\n")
    if Name == ("yes" or "Yes"):
        print("you're older than 18.")
    elif Name == ("No" or "no"):
        print("you're not older than 18.")
    else:
        print("You can only choose between yes or no.\nTry again")
        AgeCheck()    
AgeCheck()