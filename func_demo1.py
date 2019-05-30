'''def demo():
    x="Inside" # Their is no scope after exitting fromfunc # Local Variable
    print("I am0",x,"of function")

x="Outside" # Global variable
print("I am0",x,"of function")'''



def func(*name):
    print("My name is",name)



func("Amit","Snmita","Noman")
