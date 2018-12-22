class employee():
    def __init__(self,first_name,last_name,annual_salary,company):
        self.f=first_name
        self.l=last_name
        self.a=annual_salary
        self.c=company
        self.list=[]
    def give_raise(self):
        self.a+=5000
p1=employee("deepak singh","rumal",24000000,"facebook")
i=0
while i<1:
    input("tell mem your name:")
    i+=1
print("okay! cool your data was found.")       
print(p1.f)
print(p1.l)
print(p1.a)
print(p1.c)
print(p1.give_raise())
