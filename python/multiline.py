# 문자열 "" , '' , """ """ , ''' '''
food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he says.'
print(say)

# 이스케이프 코드 \
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food)
print(say)

#여러줄인 문자열을 변수에 대입하는 경우
# Life is too short
# You need Python
multiline = "Life is too short \nYou need Python"

print(multiline)
#''' / """ 사용하기

multiline = '''
Life is too short
You need python
'''
print


# 코드  	설명
# \n	문자열 안에서 줄을 바꿀 때 사용
# \t	문자열 사이에 탭 간격을 줄 때 사용
# \\	문자 \를 그대로 표현할 때 사용
# \'	작은따옴표(')를 그대로 표현할 때 사용
# \"	큰따옴표(")를 그대로 표현할 때 사용
# \r	캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f	폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
# \b	백 스페이스
# \000	널 문자

#문자열 더해서 연결하기

head = "Python"
tail = "is fun!"

print(head + tail)

#문자열 곱하기
a = 'python'
print(a * 2)
print("=" * 50)
print("My Program")
print("=" * 50)

#문자열 길이 구하기
a = "Life is too short"
print(len(a))

#문자열 인덱싱과 슬라이싱
#인덱싱은 자바의 인덱스와 같지만
# a[0] = "L"
# a[-1] = "n"
# 이와같이 - 를 이용해 뒤에서 부터 찾을수 있다.
# 슬라이싱은 문자를 자르는 작업이다.
# a[0] + a[1] + a[2] + a[3] = Life 이런식의 접근도 가능하지만
# a[0:4] = Life 와 같은 접근도 가능
# 문자열[시작인덱스 : 끝 인덱스]
# 만약 끝번호를 지정하지 않는 경우 문자열의 마지막 까지 출력한다
# a[0:] = "Life is too short"
# 시작 번호 와 끝 번호를 지정하지 않는 경우도 마찬가지
# a[:] = "Life is too short"
# 슬라이싱도 인덱싱과 마찬가지로 -기호 사용이 가능하다.
# a[0:-7] = "Life is to"
# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

#문자열 바꾸기
a = "pithon"
print(a)
# 문자열의 요소 값은 바꿀수 없다.
# a[1] = 'y'
#문자열을 잘라서 수정할 문자를 붙여 준다.
a = a[:1] + 'y' + a[2:]
print(a)
