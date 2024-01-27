a, b = map(int, input().split())

if b >= a:
	t_base = "main order - amount: "
else:
	t_base = "reverse order - amount: "
	a, b = b, a
	
def function_PD(a, b):
    count = 0
    for num in range(a, b + 1):
        if num == 0 or num == 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1
    return count
    
final = str(function_PD(a, b))

print(t_base + final)