d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d3 = d2 | d1 # é a união, onde os conflitos ficam na parte da esquerda (a principal, a qual está servindo de base)
{'a': 2, 'b': 4, 'c': 6}
ja = {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4, 'x': 5}}
{'a': 0, 'x': 1, 'y': 2, 'z': 3, 'x': 4, **{x: y for x,y in {'z': 3, 'x': 4}.items()}}
novo = dict(a= 2, b= 4, 'c'=6)