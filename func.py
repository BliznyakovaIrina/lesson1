def test():
    return get_summ(2,3)

def get_summ(one, two, delimiter='&'):
    sum = str(one)+str(delimiter)+str(two)
    return sum.upper()

def get_summ2(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'

first = 'Learn'
second = 'python'
sum = get_summ(first, second)
sum2 = get_summ2(first,second)
print(sum)
print(sum2.upper())
print(test())

