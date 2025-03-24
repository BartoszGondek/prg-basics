class Phone():
    def __init__(self, model, colour, screen_size,battery):
        self.model = model 
        self.colour = colour
        self.screen_size = screen_size
        self.is_charge = True
        self.battery = battery
    def charge(self):
       self.is_charge = True
    def not_charge(self):
        self.is_charge = False
    def display_info(self):
        print(f"My phone model is: {self.model}")
        print(f"It has {self.colour} colour")
        print(f"Screen size is {self.screen_size}")
        if self.is_charge:
            print(f"Phone is being charged and it has {self.battery}% now")
        else:
            print(f"Phone is not being charged, it has {self.battery}% now")
        print(f"Opened apps for : {self.model}")
           count = 0 
        
def main():
    my_phone = Phone("Iphone SE 3rd generation", 'white', "5inch", 82)

    my_phone.charge()

