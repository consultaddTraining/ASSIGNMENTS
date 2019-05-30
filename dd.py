x=int(input("Please enter number:")) #0


if(x>0):  #1 stmt executed
    print("The number is greater than 0")
    if(x>10): # nested if statements
        print("x is gtreater than 10")
    else:
        print("Not greater than 10")

elif(x<0): #Plan B
    print("Less than 0")

else:
    print("Equal to zero")
    if True:
        print("I am inside else")




'''if(x<0):  # 2 stmt executed
    print("Less than 0")

if (x==0): # 3 stmt executed
    print("Equals to zero")'''
