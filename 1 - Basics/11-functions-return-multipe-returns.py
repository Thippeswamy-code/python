# Describes returning values from functions

# Single return value from function
# return value, when a single return value, keeps the type in return statement
# Can return multiple values from a function
# return values, when multiple return values, gets coverted to the type of tuple

# Return values can be captured in a variable during invocation (Single or Multiple return values)
# Values can be destructured and assigned to multiple variables (Multiple return values)
#     The return values are of specific types as returned and not a tuple in this case


def hello(name):
    print('Howdy! ' + name)
    return name


sing = hello('Testing Single Return')
print(sing)

# Multiple return from function
def helloMultiple(name):
    print('Howdy! ' + name)
    return 'name', name


# Capture multiple returns as a tuple
mul = helloMultiple('Testing Multiple returns')
print(mul)

# Capture multiple returns in different variables using destructuring
var1, var2 = helloMultiple(
    'Testing Multiple returns captured in multiple values')
print(var1, var2)
