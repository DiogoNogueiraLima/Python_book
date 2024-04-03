# oop/simplest.class.py
class Simplest(): # when empty, the braces are optional
    num : int = 2
    pass
print(type(Simplest)) # what type is this object?
simp = Simplest() # we create an instance of Simplest: si
print(type(simp)) # what type is simp?
# is simp an instance of Simplest?
print(type(simp) is Simplest) # There's a better way to
print(isinstance(simp, Simplest))