'''
==========================================================================================

python sandbox

==========================================================================================
2024-05-01


a = int(input('a 입력: '))
b = int(input('b 입력: '))

if  a < b:
    print('b가 a보다 큽니다.')
if a > b:
    print('b가 a보다 큽니다.')
if a == b:
    print('둘이 같습니다.')
if a != b:
    print('a와 b가 서로 다릅니다.')
if a >= b:
    print('b보다 a가 더 크거나, 둘이 같습니다.')
if a <= b:
    print('a보다 b가 더 크거나, 둘이 같습니다.')

if (a == 1 and b == 1):
    print('a에 1이 들어있고, b에도 1이 들어있습니다.')
if a != 1 or b != 1:
    print('a에 1이 들어있지 않거나, 혹은 b에 1이 들어있지 않습니다.')
if not a == 1:
    print('a에 1이 들어있지 않다!')
===

person_1 = input('사람1: ')
person_2 = input('사람2: ')
person_3 = input('사람3: ')
dis = int(input('집간 거리: '))
answer =  dis * 3

question = input('{}과 {}와 {}이 있다.\n 셋의 집은 각각 {}km마다 떨어져 있는 거리에 존재한다.\n 세 명의 집을 차례대로 방문하려면 몇 km를 걸어가야 하는가? 정답:'.format(person_1, person_2, person_3, dis))

if question == int(answer):
    print('정답입니다.')
else: print('오답입니다.\n답은{}km입니다.'.format(answer))

===


num1 = int(input('Hello, Type some number: '))
num2 = int(input('and Type some number: '))

answer1 = int(input('{} + {} = '.format(num1, num2)))
exact_answer1 = int(num1 + num2)

if answer1 == exact_answer1:
    answer2 = int(input('정답입니다.\n 다음문제입니다. \n 둘 중 어떤 숫자가 더 큽니까?\n 1.{}\n 2.{}\n '.format(num1, num2)))
    exact_answer2 = 1 if num1 > num2 else 2
    if answer2 == 1:
        if num1 > num2:
            print('정답입니다.')
        else: print('오답입니다.정답은 {}번입니다.'.format(exact_answer2))
    if answer2 == 2:
        if num1 < num2:
            print('정답입니다.')
        else: print('오답입니다.정답은 {}번입니다.'.format(exact_answer2))
else: print('오답입니다.정답은 {}입니다.'.format(exact_answer1))
==========================================================================================
'''
num1 = int(input('Hello, Type some number: '))
num2 = int(input('and Type some number: '))

answer1 = int(input('{} + {} = '.format(num1, num2)))
exact_answer1 = int(num1 + num2)

if answer1 == exact_answer1:
    answer2 = int(input('정답입니다.\n 다음문제입니다. \n 둘 중 어떤 숫자가 더 큽니까?\n 1.{}\n 2.{}\n '.format(num1, num2)))
exact_answer2 = 1 if num1 < num2 else 2
if answer2 == 1:
    if num1 > num2:
        print('정답입니다.')
    else: print('오답입니다.정답은 {}번입니다.'.format(exact_answer2))
if answer2 == 2:
    if num1 < num2:
        print('정답입니다.')
    else: print('오답입니다.정답은 {}번입니다.'.format(exact_answer2))
else: print('오답입니다.정답은 {}입니다.'.format(exact_answer1)) 