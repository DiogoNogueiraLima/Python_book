a = 2
print(id(a))
t = (1, a, [30, 40])
print(id(t[1]))
#t[2] += [50, 60]
a = 3
print(id(a))
print(id(t[1]))
print(t)
pass

def duplicate(obj):
    obj = [obj[0]] + [obj[0]] # [9] + [9]
    return obj

def duplicateinplace(obj):
    obj += [obj[0]] 

x = [9]
x = duplicate(x)
duplicateinplace(x)
pass