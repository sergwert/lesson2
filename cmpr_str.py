# Сравнение строк
# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.

def cmpr_str(str1, str2):
    if str1==str2:
        r=1
    elif len(str1)>len(str2) and str1!=str2:
        r=2
    elif str2=='learn' and str1!=str2:
        r=3
    print(r)
    return r


def main():
    str1=input ('Введите строку 1: ')
    str2=input ('Введите строку 2: ')
    cmpr_str(str1,str2)

main ()