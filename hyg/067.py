a = int(input())

def is_plus(num):
    if abs(num) == num:
        return True
    return False


def is_even(num):
    if num%2==0:
        return True
    return False

x = is_plus(a)
y = is_even(a)

if x and y:
    print('C')
elif x and not y:
    print('D')
elif not x and y:
    print('A')
else:
    print('B')