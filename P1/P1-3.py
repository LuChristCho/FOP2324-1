Rs = int(input())
Ls = int(input())

def dtb(decimal_number):
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2
    padding = "0" * (32 - len(binary_number))
    binary_number = padding + binary_number
    return binary_number

B64 = str(dtb(Ls)) + str(dtb(Rs))

num_inputs = int(input())

inputs = []
for i in range(num_inputs):
    value = int(input())
    inputs.append(value)

BF = B64[::-1]

values = []

for input_val in inputs:
    if 0 <= input_val < len(BF):
        if BF[input_val] == '1':
            values.append("yes")
        else:
            values.append("no")

for value in values:
    print(value)
