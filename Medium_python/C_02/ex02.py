x = 'ABC'
codes = [ord(x) for x in x]

print(x)

print(codes)

codes = [last := ord(c) for c in x] # dando aviso de run time pq c nao foi definido???????????
print(codes)

print(last)

#print(c)
