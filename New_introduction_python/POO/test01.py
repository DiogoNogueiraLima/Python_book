x = 1
def func():
    global x
    print(x)
    x = 2
    print(x)


def func2():
    print('WHAT A CRAZY THING BOY')
    
func()
func2()
print(x)

# A: 1
# B: 2
# C: Erro