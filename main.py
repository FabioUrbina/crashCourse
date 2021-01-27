# This is a scratch code area to play with Crash Course and some simple hints.

# Lists: create with var_name = []
var = ["one", "two", "fewg"]
var_name = range(1, 15)

# Slice using [:] syntax. var_name[:3] goes from first to 3rd, var_name[3:] goes third to last
# create a list in one line; ** is exponential
squares = [x ** 2 for x in range(1, 19)]
print(squares[-7:])

# important! Setting x=y is NOT creating a new list, but adding two names to the same list
squareNot = squares
squareNot.append(5)
print("This one is exactly the same data: ", squareNot)

# to create a duplicate list, must assign the whole slice from beginning to end:
squareNot = squares[:]
squareNot.append(5)
print("This one is a copy: ", squareNot)

# Tuples are immutable, but otherwise the same as list, just () instead of []
dimensions = (250, 50)
print(dimensions[0])
# dimensions[0] = 200 # throws error
# We can overwrite a tuple, however:
dimensions = (500, 30)
print(dimensions)

# If comparison statements. If we don't care about case, can make everything lower
exampleCar = 'Audi'
print(exampleCar == 'audi')
print(exampleCar.lower() == 'audi')

# for multiple conditions, can use and
pizzaTopping = 'anchovies'
if exampleCar.lower() == 'audi' and pizzaTopping == 'anchovies':
    print('fuck anchovies')
# can use parentheses to improve readability, but not necessary:
age_1 = 4
age_2 = 17
if (age_1 > 2) and (age_2 < 20):
    print('yezzir')

# or is used similarly:
if (age_2 < 1) or (age_2 < 20):
    print('okay')

# to check if a value is in a list, use the keyword "in":
pizzaToppings = ['anchovies', 'pepporoni', 'cheese']
print("anchovies" in pizzaToppings)
# use 'not' to do the opposite:
print("anchovies" not in pizzaToppings)

# some if elif else syntaxin example: free admission under 4, $5 for 4-18yo, 7$ for adult
childAge = 8
if childAge < 4:
    ticketPrice = 0
elif childAge > 4 or childAge < 18:
    ticketPrice = 5
else:
    ticketPrice = 7
print("your admission price is $" + str(ticketPrice) + ".")
# Else isn't needed, but it acts as a catch-all. Use if you need a catch-all,omit if you have specific conditions you
# are trying to meet. Press the green button in the gutter to run the script. if __name__ == '__main__':

# combine if statements with lists
pizzaToppings.append("Mushrooms")
# Sidenote; if you use "if *list*, it will return true if the list is not empty
if pizzaToppings:
    for topping in pizzaToppings:
        if topping == "Mushrooms":
            print("Sorry! We are out of mushrooms")
        else:
            print("Adding " + str(topping) + " to your order.")
else:
    print("No toppings requested!")

# Time for some dictionary love!
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])
new_points = alien_0["points"]
print("alien is worth " + str(new_points) + " points")

# can add new key:value pairs to the dictions like this:
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# can start an empty dictionary like this:
alien_1 = {}
alien_1['color'] = 'green'
print(alien_1)

# changing key:value pair is easy:
print('alien 1 is ' + str(alien_1['color']))
alien_1['color'] = 'yellow'
print('alien 1 is ' + str(alien_1['color']))

# to remove key:value pair:
del alien_0['points']
print(alien_0)

# for creating longer dictionaries, easier to read if input like:
favorite_language = {
    'jen': 'C',
    'bob': 'python',
    'elise': 'LISP'
}
print(favorite_language['elise'])
# to access everything in a dictionary, can loop through:
for key, value in favorite_language.items():
    print("\nKey: " + key)
    print("Value: " + value)
for k, v in favorite_language.items():
    print("\n" + str(v))

# to loop through specifically keys
for name in favorite_language.keys():
    print(name)
# its default behavior, so same as:
for name in favorite_language:
    print(name)
# for values, use .value
for val in favorite_language.values():
    print(val)

# to sort before looping, used sorted (different than sort)
for name in sorted(favorite_language.keys()):
    print(name)

# We can store a list of dictionaries:
alien_3 = {'color': 'yellow', 'points': 5}
all_aliens = [alien_0, alien_1, alien_3]
for aliens in all_aliens:
    print(aliens)

aliens = []
# lets make a whole fleet of aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens:
for alien in aliens:
    print(alien)

print(str(len(aliens)))

# lets use pizza to store a list inside a dictionary:
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese', 'anchovies']
}
print(pizza['toppings'])

# can nest dictionaries;
user_base = {
    'kenny': {
        'temp': 'yes'
    }
}

message = input('tell me something: ')
print(message)


# Now, we'll create a class dog.
class Dog:
    """a simple attempt to model a dog."""

    def __init__(self, name, dog):
        """initialize name and age attributes."""
        self.name = name
        self.dog = dog

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(Self.name.title() + " is sitting now.")

    def rollOver(self):
        """Simulate a dog rolling over in response to a command."""
        print(Self.name.title() + " rolled over!")

myDog = Dog('willie',6)
print('My dogs name ' + myDog.name.title() + '.')

class Car:
    """This class creates a car representation."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('the car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mielage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('feck off')

    def increment_odometer(self, miles):
        self.odometer_reading += miles



"""if our attributed get too big, create a new class. For batteries:"""
class Battery:
    """a simple battery class"""

    def __init__(self,battery_size=70):
        """initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        print('this batter has a size of ' + self.battery_size)


class ElectricCar(Car):
    """represents aspects of electric cars specifically"""

    def __init__(self, make, model, year):
        """initialize attributes of the parent classs."""
        super().__init___(make, model, year)  # so these two init just link child/parent, and should be the same.
        #self.battery_size = 70
        self.battery = Battery()

        # to override a function, just create a new one in the child with the same name, thats it- no problem.

    def update_odometer(self, mileage):
        print('lol')


my_tesla = ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())

#can create classes inheriting classes + calling instances of other classes! Like above:
"""
car class
battery class
electric class (child of car)
    inside electric, create battery class assign with self.x

And can call functions, working out way down:
mytesla.battery.describe_batter()

Also, good practive; have classes in their own file, import module, much like functions
If classes are split up but nest, then inherit in the file for the one module
Car is one module
electric-car/batter in another module
import car in the electric-car/battery module, then only import EC/B into the main script
"""