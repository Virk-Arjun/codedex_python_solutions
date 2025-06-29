class Pokemon: 
    def __init__(self, entry, name, types, description, is_caught): 
        self.entry = entry 
        self.name = name 
        self.types = types 
        self.description = description 
        self.is_caught = is_caught

    def speak(self): 
        print(self.name)

    def display_details(self): 
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        print(f"Caught: {self.is_caught}")

pikachu = Pokemon(25, "Pikachu", "Electric", "A yellow mouse with electricity powers", True)

pikachu.speak()           
pikachu.display_details() 
