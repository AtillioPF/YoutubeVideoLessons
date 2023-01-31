# Class attributes

class Person:
    number_of_people = 0 # class attribute, specific to the class, not the isntance
        
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod  # class method to be called at the class itself not on the instance
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
p1 = Person("Robert")
p2 = Person("Maurice")
print(Person.number_of_people_())
print(Person.number_of_people)