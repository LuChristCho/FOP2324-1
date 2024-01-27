def func1(input):
    output = input.strip()
    output = ' '.join(output.split())
    return output
def func2(input):
    atsign = input.find('@')
    while atsign != -1:
        temp = input.find('#', atsign)
        if temp != -1:
            input = input[:temp] + input[temp+1:]
        atsign = input.find('@', atsign + 1)
    return input
def func3(input):
    input = input.replace('\\n', '\n')
    return input
print("Formatted Text: " + func3(func2(func1(input()))))