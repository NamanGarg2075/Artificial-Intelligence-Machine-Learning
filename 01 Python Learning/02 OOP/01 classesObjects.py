#  Creating a class
class Myclass(object):
    def __init__(self, name): # initializing variales
        self.model = name
    
    def show_model(self): # creatig methods
        print("Model:", self.model)
    
#  defining methods
iphone7 = Myclass("iPhone 7")
iphone12 = Myclass("iPhone 12")

# calling methods
iphone7.show_model()
iphone12.show_model()