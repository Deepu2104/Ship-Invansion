class singers():
    """Making the instance of the function"""
    def __init__(self,name,rating):
        self.n=name
        self.r=rating
    def bio(self):
        print(self.n.title(),"is the name of the singers")
        print(self.r.title(),"is the rating of the singer")
    def fun(self):
        print("\nBut! friends ",self.n.title(),"is my favorite singer")
        #Creating the object/instance of the class to feed into the __init__ method..
p1=singers("\nhoney singh","5 stars out of 5 stars.")
p2=singers("\nbaadshah","3.9 stars out of 5 stars")
p3=singers("\nbohemia","4.5 stars out of 5 stars")
p1.bio()
p2.bio()
p3.bio()
p1.fun()
