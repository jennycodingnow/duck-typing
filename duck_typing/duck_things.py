# This function doesn't really care what the actual type is
# that d refers to, just as long as the thing has the
# attributes species, fly, walk, and talk. fly, walk, and
# talk must all be "callable" (such as a function).
def do_duck_things(d):
    print(d.species)
    print(d.fly())
    print(d.walk())
    print(d.talk())
