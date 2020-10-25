n = int(input('Мне>'));


def age_to_str(n):
    return 'лет' \
        if n // 10 % 10 == 1 or n % 10 in [0, 5, 6, 7, 8, 9] \
        else 'год' \
        if n % 10 == 1 \
        else 'года'


print(f' {n} {age_to_str(n)} ')
