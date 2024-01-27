def func(nlist, n):
    temp = {}
    check_s = set()
    for index, num in enumerate(nlist):
        fin = n - int(num)
        if fin in temp:
            check_s.add((min(index, temp[fin]), max(index, temp[fin])))
        temp[int(num)] = index
    if not check_s:
        print('Not Found!')
        return
    sum_list = [sum(pair) for pair in check_s]
    sum_list.sort()
    for pair in sum_list:
        print(pair)
in1 = input().split()
in2 = int(input())
func(in1, in2)