class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self._name = name  # Encapsulated
        self._secret_identity = secret_identity  # Encapsulated
        self.power_level = power_level

    def use_power(self):
        return f"{self._name} uses power level {self.power_level}!"

    def special_ability(self):  # For polymorphism
        return f"{self._name} fights with strength."

class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, power_level, flight_speed):
        super().__init__(name, secret_identity, power_level)
        self.flight_speed = flight_speed

    def special_ability(self):  # Polymorphic override
        return f"{self._name} flies at {self.flight_speed} mph!"

# Example usage
hero1 = Superhero("Thunderbolt", "Alex Smith", 85)
print(hero1.use_power())  
print(hero1.special_ability())  

hero2 = FlyingSuperhero("Sky Guardian", "Jane Doe", 90, 300)
print(hero2.use_power())  
print(hero2.special_ability())  