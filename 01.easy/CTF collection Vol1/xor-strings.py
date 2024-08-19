# Prompt the user to enter the first string
s1_input = input("Enter the first string: ")

# Prompt the user to enter the second string
s2_input = input("Enter the second string: ")

# Convert the input strings to bytes
s1 = bytes.fromhex(s1_input)
s2 = bytes.fromhex(s2_input)

# Perform the XOR operation on the corresponding bytes
xor_result = bytes(a ^ b for a, b in zip(s1, s2))

# Convert the XOR result to ASCII and print
ascii_result = xor_result.decode('ascii')
print("XOR result (ASCII):", ascii_result)