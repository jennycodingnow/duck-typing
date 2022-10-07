class Empty: pass

def SoNotADuck():
    # Make an "empty" object that we can stick new attributes on
    inst = Empty()

    # Fill in the attributes the object needs to pass for a duck
    inst.species = "SoNotADuck.species"
    inst.fly = lambda: "SoNotADuck.fly"
    inst.walk = lambda: "SoNotADuck.walk"
    inst.talk = lambda: "SoNotADuck.talk"

    # Return the initialized instance
    return inst

