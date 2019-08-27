# Describes using decorators/annotation to create getters and setters

# Difference between a property and attribute
# https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute

# Attribute is variable
# Property is variable with getter and "setter method"
# Method is class function

# Internet says attributes and properties are interchangable 
# and methods are seperate class functions

# Declaring class A
class A(object):
    # Defining a _x attr
    _x = 0
    '''A._x is an attribute'''

    # Adding a getter for property x that returns _x
    @property
    def x(self):
        '''
        A.x is a property
        This is the getter method
        '''
        return self._x

    # Adding a setter that assigns values for _x
    @x.setter
    def x(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value < 0:
            raise ValueError("Must be >= 0")
        self._x = value

# Instantiating Class A
a = A()

# Checking functionality for a.x (should be working on or manipulating a._x)
a._x = -1
a.x = -1
# Correct one
# a.x = 1
print(a.x)