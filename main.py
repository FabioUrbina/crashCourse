# This is a scratch code area to play with Crash Course and some simple hints.

# Lists: create with var_name = []
var = ["one","two","fewg"]
var_name = range(1,15)

# Slice using [:] syntax. var_name[:3] goes from first to 3rd, var_name[3:] goes third to last
# create a list in one line; ** is exponential
squares = [x**2 for x in range(1,19)]
print(squares[-7:])

# important! Setting x=y is NOT creating a new list, but adding two names to the same list
squareNot= squares
squareNot.append(5)
print("This one is exactly the same data: ", squareNot)

# to create a duplicate list, must assign the whole slice from beginning to end:
squareNot =squares[:]
squareNot.append(5)
print("This one is a copy: ", squareNot)

# Tuples are immutable, but otherwise the same as list, just () instead of []
dimensions = (250,50)
print(dimensions[0])
# dimensions[0] = 200 # throws error
# We can overwrite a tuple, however:
dimensions = (500,30)
print(dimensions)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
