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

#combine if statements with lists
pizzaToppings.append("Mushrooms")
#Sidenote; if you use "if *list*, it will return true if the list is not empty
if pizzaToppings:
    for topping in pizzaToppings:
        if topping == "Mushrooms":
            print("Sorry! We are out of mushrooms")
        else:
            print("Adding " + str(topping) + " to your order.")
else:
    print("No toppings requested!")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
