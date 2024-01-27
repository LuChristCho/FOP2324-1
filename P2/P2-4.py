def su_path(length, width, movements):
    ora = [['.' for _ in range(length)] for _ in range(width)]
    x, y = 0, 0
    ora[y][x] = '*'
    for move in movements:
        if move == 'R' and x < length-1:
            x+=1
        elif move == 'L' and x > 0:
            x-=1
        elif move == 'B' and y < width-1:
            y+=1
        ora[y][x] = '*'
    for lin in ora:
        print(' '.join(lin))
    if x == length-1 and y == width-1:
        t = 2
    else:
        print("There's no way out!")
        
ran = int(input())
lst = [ ]
lst2 = [ ]

while True:
    x = input()
    if x != "END":
        lst.append(x)
        if x == "B":
            lst2.append(x)
    else:
        break
    
lltt = ''.join(lst)
xi = ran
yi = int(len(lst2)+1)

su_path(xi, yi, lltt)