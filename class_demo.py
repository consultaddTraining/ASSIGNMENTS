class country:
    def req(self):
        print("Visa is required")
    def loc(self):
        print("I am in United States")

class state(country):
    def loc(self):
        print("I am in Texas")
    def ticket(self):
        print("You need a proper ticket")

class city(country):
    def loc(self):
        print("I am in Dallas")




country_obj = country()
state_obj = state()
city_obj = city()


country_obj.loc()
state_obj.loc()
city_obj.loc()

#country_obj.req()
state_obj.req()

city_obj.req()










'''x=10 # Global variable

class multiple_func:
    x=20 # Local Variable   # Class Variable
     str="I am inside class"
     def one(self):
             z=50   # Instance variable
             print("I amin one")
             avg=(x+y+z)/3

     def two(self):
             print("I amin two")
             print(x+y)
     def three(self):
             print("I amin three")
     def __init__(self,r):
             #self.r=name  # Instantiation stmt
             #print("I am executed, Name=",self.name)




obj = multiple_func("Rishabh")
obj1 = multiple_func("Vishal")
obj.three()
#obj.one() # it will internally call with self i,e obj.one(self)
#obj.two()


#multiple_func.one()  #  from multiple_func import one'''
