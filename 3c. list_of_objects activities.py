class Pet:
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
 
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self.name +'\nCategory: ' + self.category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: ' + str(self.vaccinated)
        return my_status
    
p1 = Pet('Bonnie', 'Cat', 4)
p2 = Pet('Clyde', 'Dog',7)      

print(p1)


p1 = Pet('Bonnie', 'Cat', 4)
p2 = Pet('Clyde', 'Dog', 7)
p3 = Pet(category='Rabbit', name='Ruby', age=13)
p4 = Pet('George', 'Cat', 6)
p5 = Pet('Sally', 'Hampster', 2)

print(p1) 
#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list