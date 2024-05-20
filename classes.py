# Classes in Python

# A class is a blueprint for creating objects. It allows you to bundle data and functionality together.


# Defining a class:
class MyClass:
    """This is a simple class."""

    pass


# Creating an instance of a class:
obj = MyClass()


# Constructor (__new__):
# The __new__ method is called to create a new instance of a class. It's rarely used directly.
class MyClass:
    def __new__(cls):
        instance = super(MyClass, cls).__new__(cls)
        return instance


# Initializer (__init__):
# The __init__ method initializes the instance. It is called immediately after the instance is created.
class MyClass:
    def __init__(self, value):
        self.value = value
        print(f"Initialized with value: {value}")


obj = MyClass(10)  # >>> "Initialized with value: 10"


# Destructor (__del__):
# The __del__ method is called when an object is about to be destroyed.
class MyClass:
    def __init__(self, value):
        self.value = value
        print(f"Initialized with value: {value}")

    def __del__(self):
        print(f"Instance with value {self.value} is being destroyed")


obj = MyClass(10)
del obj  # >>> "Instance with value 10 is being destroyed"


# Magic methods:
# Magic methods are special methods with double underscores at the beginning and end. They are used to override default behaviors.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # >>> "Vector(4, 6)"


# Inheritance:
# Inheritance allows you to define a class that inherits all the methods and properties from another class.
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()  # >>> "Animal speaks"
dog.bark()  # >>> "Dog barks"


# Public, protected, and private members:
# Public members can be accessed from anywhere. Protected members are indicated by a single underscore and should not be accessed outside the class or its subclasses. Private members are indicated by double underscores and are name-mangled.
class MyClass:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"


obj = MyClass()
print(obj.public)  # >>> "I am public"
print(obj._protected)  # >>> "I am protected"
# print(obj.__private)  # This will raise an AttributeError
print(obj._MyClass__private)  # >>> "I am private" (name-mangling)


# Class variables:
# Class variables are shared among all instances of the class.
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")
print(MyClass.class_variable)  # >>> "I am a class variable"
print(obj1.class_variable)  # >>> "I am a class variable"
print(obj2.class_variable)  # >>> "I am a class variable"
MyClass.class_variable = "Changed class variable"
print(obj1.class_variable)  # >>> "Changed class variable"
print(obj2.class_variable)  # >>> "Changed class variable"


# Static and class methods:
# Static methods are defined using the @staticmethod decorator and do not have access to the instance or class. Class methods are defined using the @classmethod decorator and have access to the class but not the instance.
class MyClass:
    @staticmethod
    def static_method():
        print("I am a static method")

    @classmethod
    def class_method(cls):
        print(f"I am a class method in {cls}")


MyClass.static_method()  # >>> "I am a static method"
MyClass.class_method()  # >>> "I am a class method in <class '__main__.MyClass'>"


# Properties:
# Properties allow you to customize access to instance attributes.
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """The value property."""
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value


obj = MyClass(10)
print(obj.value)  # >>> 10
obj.value = 20
print(obj.value)  # >>> 20
# obj.value = -10  # This will raise a ValueError
del obj.value
# print(obj.value)  # This will raise an AttributeError

# Summary:
# - Defining a class:
#   class ClassName:
#       # Class body
#
# - Constructor (__new__):
#   def __new__(cls, *args, **kwargs):
#       # Create and return a new instance
#
# - Initializer (__init__):
#   def __init__(self, *args):
#       # Initialize the instance
#
# - Destructor (__del__):
#   def __del__(self):
#       # Clean up before the instance is destroyed
#
# - Magic methods:
#   def __add__(self, other):
#       # Define addition behavior
#
# - Inheritance:
#   class SubClass(BaseClass):
#       # SubClass body
#
# - Public, protected, and private members:
#   public_member
#   _protected_member
#   __private_member
#
# - Class variables:
#   class_variable = value
#
# - Static and class methods:
#   @staticmethod
#   def static_method():
#       # Static method body
#
#   @classmethod
#   def class_method(cls):
#       # Class method body
#
# - Properties:
#   @property
#   def property_name(self):
#       # Getter method
#
#   @property_name.setter
#   def property_name(self, value):
#       # Setter method
#
#   @property_name.deleter
#   def property_name(self):
#       # Deleter method
