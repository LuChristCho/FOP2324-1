def t1(number):
    div_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            div_sum += i
    return div_sum

def t2(number, base):
    if base < 2 or base > 9:
        return "0"
    result = ""
    while number > 0:
        result = str(number % base) + result
        number //= base
    return int(result) if result else 0

data = []
while True:
    user_input = input()
    if user_input == "-1 -1":
        break
    else:
        n, b = map(int, user_input.split())
        data.append((n, b))

total = 0
lcheck = False
for n, b in data:
    finalt1 = t1(n)
    finalb = t2(finalt1, b)

    if finalb != "0":
        total += int(finalb)
    else:
        print("invalid base!")
        lcheck = True
        break

if not lcheck:
    print(total)
