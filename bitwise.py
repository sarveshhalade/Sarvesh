# Define two integers
a = 10  # in binary: 1010
b = 4   # in binary: 0100

# Bitwise AND
result_and = a & b
print(f"{a} & {b} = {result_and} (binary: {bin(result_and)})")

# Bitwise OR
result_or = a | b
print(f"{a} | {b} = {result_or} (binary: {bin(result_or)})")

# Bitwise XOR
result_xor = a ^ b
print(f"{a} ^ {b} = {result_xor} (binary: {bin(result_xor)})")

# Bitwise NOT
result_not = ~a
print(f"~{a} = {result_not} (binary: {bin(result_not)})")

# Left Shift
shift_left = a << 2
print(f"{a} << 2 = {shift_left} (binary: {bin(shift_left)})")

# Right Shift
shift_right = a >> 2
print(f"{a} >> 2 = {shift_right} (binary: {bin(shift_right)})")
