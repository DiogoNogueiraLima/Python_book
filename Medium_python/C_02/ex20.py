from array import array
octets = array('B', range(6)) 
m1 = memoryview(octets) 
m1.tolist()
[0, 1, 2, 3, 4, 5]
m2 = m1.cast('B', [2, 3]) 
m2.tolist()
[[0, 1, 2], [3, 4, 5]]
m3 = m1.cast('B', [3, 2]) 
m3.tolist()
[[0, 1], [2, 3], [4, 5]]
m2[1,1] = 22 
m3[1,1] = 33 
octets