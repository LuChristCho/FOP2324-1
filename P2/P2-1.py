def calculate_line(n):
    line = [1]
    for i in range(1, n + 1):
        line.append(line[i - 1] * (n - i + 1) // i)
    return line

def print_pascals_triangle(lines):
    pascal_triangle = []
    for i in range(lines):
        pascal_triangle.append(calculate_line(i))
        
    for line in pascal_triangle:
        for member in line:
            print(member, end=" ")
        print()

x = int(input())
print_pascals_triangle(x)


#test