# oop/class.attribute.shadowing.py
class Point:
    x = 10
    a = [1, 2, 3]
    y = 7
    #fazer inplace append no a
p = Point()
print(p.x) # 10 (from class attribute)
print(p.y) # 7 (from class attribute)
p.x = 12 # p gets its own `x` attribute
print(p.x) # 12 (now found on the instance)
print(Point.x) # 10 (class attribute still the same)
del p.x # we delete instance attribute
print(p.x) # 10 (now search has to go again to find class
p.z = 3 # let's make it a 3D point
print(p.z) # 3
print(Point.z)
# AttributeError: type object 'Point' has no attribute '
