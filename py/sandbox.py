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

==========================================================================================
# .zip 압축파일 내 .jpg 이미지 찾기

import zipfile

my_archive_zip = '/Users/leejunho/git/sample_files/eg/Parsley/Picture/jpg-imgset.zip'
my_archive_rar = '/Users/leejunho/git/sample_files/eg/Parsley/Picture/jpg-imgset.rar'
my_archive_7z = '/Users/leejunho/git/sample_files/eg/Parsley/Picture/jpg-imgset.7z'

def find_images_in_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as myzip:
        for file in myzip.namelist():
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                print(f"Found image: {file}")

# 사용 예
find_images_in_zip(my_archive_zip)

# .rar 비표준 라이브러리 사용
import rarfile

def find_images_in_rar(rar_path):
    with rarfile.RarFile(rar_path, 'r') as myrar:
        for file in myrar.namelist():
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                print(f"Found image: {file}")

# 사용 예
find_images_in_rar(my_archive_rar)

# .7z 비표준 라이브러리 사용

import py7zr

def find_images_in_7z(sevenz_path):
    with py7zr.SevenZipFile(sevenz_path, mode='r') as z:
        for file in z.getnames():
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                print(f"Found image: {file}")

# 사용 예
find_images_in_7z(my_archive_7z)

# json 파일 읽기
import json

# JSON 파일 열기
with open('data.json', 'r') as f:
    data = json.load(f)

# 데이터 출력
print(data)

#json 파일 쓰기
import json

# 데이터 정의
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# JSON 파일 쓰기
with open('data.json', 'w') as f:
    json.dump(data, f)

# iso8601 시간
from datetime import datetime

# 현재 날짜와 시간 가져오기
now = datetime.now()

# ISO 8601 형식의 문자열로 변환
iso_format = now.isoformat()

print(iso_format)  # 출력: 2022-01-01T15:45:30

from datetime import datetime

# 현재 날짜와 시간 가져오기
now = datetime.now()

# 마이크로초 제거
now = now.replace(microsecond=0)

# ISO 8601 형식의 문자열로 변환
iso_format = now.isoformat()

print(iso_format)  # 출력: 2022-01-01T15:45:30

# 현재 날짜와 시간 가져오기
now = datetime.now()

# 마이크로초 제거
now = now.replace(microsecond=0)
# 현재 날짜와 시간 가져오기
now = datetime.now()

# 마이크로초 제거
now = now.replace(microsecond=0)

# ISO 8601 형식의 문자열로 변환
iso_format = now.isoformat()

# ':' 문자를 '_' 문자로 바꾸기
iso_format = iso_format.replace(':', '_')

print(iso_format)  # 출력: 2022-01-01T15_45_30
'''

# 로그 파일과 터미널에 동시에 출력
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())
        log_file.write(output)
