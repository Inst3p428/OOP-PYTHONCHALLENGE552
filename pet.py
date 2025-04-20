class Pet:
    
    def __init__(self):
        self.name = ""
        self.hunger =  0
        self.energy = 0
        self.happiness = 0
        
    def get_input(self):
        self.name = str(input("Enter name of pet: "))
        self.hunger = int(input("Enter value of hunger between 0-10: " ))
        self.energy = int(input("Enter value of energy between 0-10: "))
        self.happiness = int(input("Enter value of happiness between 0-10: "))
    
    
    def eat(self):
        if self.hunger -3 <= 0:
            return self.hunger
        else:
            self.hunger -= 3
            self.happiness += 1
        
            
    def sleep(self):
        if self.energy + 5 >= 10:
            return self.energy
        else:
            self.energy += 5
            
       
            
    def play(self):
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1
       
    def train(self):
        self.list_trick = []
        int_inputs = 0
        self.numinputs=int(input("Enter number of tricks to learn: "))
        while int_inputs != self.numinputs:
            self.trick = str(input("Enter trick to learn: "))
            self.list_trick.append(self.trick)
            int_inputs += 1
        
        
        
    def show_tricks(self):
        print(f"Tricks learned: {self.list_trick}")
     
            
    def get_status(self):
        print(f"Name pet is {self.name}")
        print(f"Current energy level is {self.energy}")
        print(f"Current happiness level is {self.happiness}")
        print(f"Current hunger level is {self.hunger}")



