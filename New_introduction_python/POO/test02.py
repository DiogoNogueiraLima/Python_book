x = 1
def outer():
    x = 2

    def inner():
        x = 3

        def double_inner():
            nonlocal x
            x = 4
            print(f'double inner sees x equal to {x}')

        double_inner()
        print(f'inner sees x equal to {x}')
    
    inner()
    print(f'outer sees x equal to {x}')

outer()
print(f'global sees x equal to {x}')

'''
double inner sees x equal to 4
inner sees x equal to 4
outer sees x equal to 2
global sees x equal to 1
'''
