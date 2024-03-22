*range(4), 4 # (0, 1, 2, 3) + (4)
(0, 1, 2, 3, 4)
[*range(4), 4]
[0, 1, 2, 3, 4] # [0, 1, 2, 3] + [4]
{*range(4), 4, *(5, 6, 7)} # descompacte range(4) + 4 + descompactaçao da tupla (5, 6, 7)
{0, 1, 2, 3, 4, 5, 6, 7}
b = [0, 1, 2, 3]
c = b + [4]
print(c)