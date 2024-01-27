import math
import functools
legal_inputs = ['sum', 'average', 'gcd', 'lcd', 'min', 'max']
input_list = [ ]
f = False
flag = True
user_inputs = input()

if user_inputs in legal_inputs:

    while True:
        data = input()
        if data == "end":
            f = True
            break
        input_list.append(int(data))
else:
    print("Invalid command")
    flag = False
if user_inputs == "sum":
    print(sum(input_list))
elif user_inputs == "average":
    final = sum(input_list)/len(input_list)
    final = round(final, 2)
    print(final)
elif user_inputs == "gcd":
    result= input_list[0]
    for member in input_list[1:]:
        result = math.gcd(result, member)
    print(result)
elif user_inputs == "lcd":
    def lcm_0(liste):
        def lcm(x, y):
            return x*y // math.gcd(x, y)
        return functools.reduce(lcm, liste)
    print(lcm_0(input_list))
elif user_inputs == "min":
    print(min(input_list))
elif user_inputs == "max":
    print(max(input_list))