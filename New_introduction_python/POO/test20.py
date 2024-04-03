# oop/private.attrs.py
class A:
    def __init__(self, factor):
        self._factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))

class B(A):
    def op2(self, factor):
        self._factor = factor
        print('Op2 with factor {}...'.format(self._factor))

obj = B(100)
obj.op1() # Op1 with factor 100...

obj.op2(42) # Op2 with factor 42...
obj.op1() # Op1 with factor 42... <- This is BAD

'''# oop/private.attrs.fixed.py'''
class A:
    def __init__(self, factor):
        self.__factor = factor # same thing that: _A__factor
        self.none = 'NONE'

    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))

class B(A):
    def op2(self, factor):
        self.__factor = factor # same thing that: _B__factor
        print('Op2 with factor {}...'.format(self.__factor))

obj = B(100)
obj.op1() # Op1 with factor 100...

obj.op2(42) # Op2 with factor 42...
obj.op1() # Op1 with factor 100... <- Wohoo! Now it's G

print(obj.__dict__.keys())

### Avoid to subscribe the atribute on heritance
