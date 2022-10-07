from duck_typing.duck import Duck
from duck_typing.not_a_duck import NotADuck
from duck_typing.so_not_a_duck import SoNotADuck
from duck_typing.duck_things import do_duck_things

# we can do duck things with a duck
print()
print("#### do_duck_things with a Duck ####")
common_duck = Duck()
do_duck_things(common_duck)

# or even another class that isn't a duck, but has the
# attributes of compatible types that we expect a duck
# to have
print()
print("#### do_duck_things with a NotADuck ####")
not_a_duck = NotADuck()
do_duck_things(not_a_duck)

# even if we set up that object in a really strange way
print()
print("#### do_duck_things with a SoNotADuck ####")
so_not_a_duck = SoNotADuck()
do_duck_things(so_not_a_duck)

# but an object missing any of those attributes cannot
# be used, so a dict causes an error
print()
print("#### do_duck_things with a dict ####")
do_duck_things({})

# Our main take-away is that Python generally has no idea what
# type anything is before it tries to access the object's
# attributes. WHen we write code like

# some_instance.some_attribute

# Python essentially has to ask the instance at the moment the
# code runs whether it actually has an attribute called
# some_attribute. The instance will either return the value
# the attribute refers to (if it has that attribute), or
# it will raise an AttributeError.

# This is why we have to be soe careful about what value we
# are passing around, and how Python code is potentially
# able to work with a wide range of types, even without ever
# importing the "definition" of those types.
