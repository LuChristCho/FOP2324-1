n = int(input())
m = int(input())
k = int(input())

while m != 0:
        temp = n & m
        n = n ^ m
        m = temp << 1
print(n)
    
if n == k:
	print("YES")
else:
	print("NO")