# creating custom constructor and desctructor for the class
class C :
    def __init_(self):
        print("Constructor")
    def __del__(self):
        print("Destructor")

o = C()  # constructor called
print("Hello,World!")
# destructor will be called at the end of the program
