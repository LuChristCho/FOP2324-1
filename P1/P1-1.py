a = int(input())
b = int(input())

Count = 0
while a != b:
    if a & 1 != b & 1:
    	Count += 1
    a >>= 1
    b >>= 1

print(Count)