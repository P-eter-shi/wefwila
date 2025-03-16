#this is based on the concept of inheritance
"""
class school:
    def __init__(self,studying):
        self.studying=studying
    def library(self):
        print(f"Students need to borrow books they want to {self.studying}")
class libo(school):
    def __init__(self,studying,reading):
        super().__init__(studying)
        self.reading=reading
    def read(self):
        print(f"Students are reading {self.reading}")
        
class college(school):
    def __init__(self,studying,test):
        super().__init__(studying)
        self.test=test
    def read(self):
        print(f"Students are reading for {self.test}")

for x in [libo("books","novels"),college("books","exams")]:
    print(x.read())
    
print("")
"""

#assignment plp
class campus:
    def __init__(self,library,hostel):
        self.__fees=100000
        self._books=library
        self.hostel=hostel
    def fees(self,amount,course,balance,filename):
        self.__balance=balance
        self.filename=filename
        self.course=course
        self.amount=amount
        self.course=input(f"Enter your course program:")
        self.amount=int(input(f"Enter your payments"))
        if self.amount>=self.__fees:
            print(f"You are elligible to seat for exam in {self.course}")
        else:
            self.__balance=self.__fees-self.amount
            filename=input("Enter your name:")
            with open("feestatement.txt","w") as file:
                file.write(f"Dear {filename} ,you have a balance of {self.__balance} to clear")
                print("Your fee statement is ready")
    def library(self,want):
        self.booksavail=["novels","medical","engineering","law","bussiness"]
        self.want=want
        self.spebooks=["novels","medical","engineering"]
        try:
            print(f"Books available are {self.booksavail}")
            want=input("Enter the book you want to borrow:")
            if want in self.spebooks:
                print(f"This require special permission")
            else:
                print("Go ahead and borrow the book")
        except NameError:
            print("Not available for borrowing")
    def hostels(self,stay):
        self.stay=stay
        self.hotels=["A","B","C","D","E"]
        print(f"Hostels available are {self.hotels}")
        try:
            stay=input("Enter the hostel you want to stay:")
            if stay in self.hotels:
                print(f"Enjoy Stay in hostel{stay}")
            else:
                print("Not available")
        except NameError:
            print("Choose a valid hostel")
class studii(campus):
    def __init__(self, library, hostel):
        super().__init__(library, hostel)
        pass
mwanafunzi=studii("books","hostels")
mwanafunzi.library("novels")
mwanafunzi.hostels("stay")
mwanafunzi.fees("amount","course","balance","filename")



            
        
        
        
        
        
        