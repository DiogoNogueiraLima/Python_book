# Example of unpacking with assignment to two variables
data = (1, 2, 3)

# Parallel assignment using unpacking for two variables
a, b, _ = data  # Add an extra variable to handle the remaining value in the tuple

# Result
print(a)  # Output: 1
print(b)  # Output: 2
