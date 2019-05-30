def first(func):

    def inner(): # Wrapper class
        print("I need decoration")
        func()
        print("Hurray, I am decorated")
    return inner()


#@first
def helper():
    print("I have flowers")


h   =  first(helper)
#helper()
