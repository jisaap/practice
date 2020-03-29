# 숫자 바로 삽입
print("I eat %d apples." % 3)

#문자열 바로 삽입
print("I eat %s apples" % "five")

#숫자값을 나타내는 변수로 대입
number = 3
print("I eat %d apples" % number)

#2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day))

#문자열 포맷 코드
# 코드	   설명
# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %	16진수# , %% Literal % (문자 % 자체)

#%s 포맷 코드의 경우 어떤 형태의 값이든 변환해 넣을 수 있다.

print("I have %s apples" %3)
print("rate is %s" % 3.234)

#만약 %를 문자로 사용하는 경우 %%를 사용한다.
# print("error %d%." % 98) << 이렇게 사용하면 안됨
print("error %d%%." % 98)

#포맷 코드와 숫자 사용
# 전체 길이가 10인 문자열 중 대입되는 값을 오른쪽 정렬하고 나머지를 공백으로 남겨두라는 의미
print("%10s" % "hi")
# 왼쪽 정렬은 -기호 이용
print("%-10sjane." % "hi")

#소수점 표현하기
# 소수점 4자리 까지만 표현
print("%0.4f" % 3.42134234)

#format 함수를 이용한 Formatting
#숫자
print("I eat {0} apples".format(3))
#문자열
print("I eat {0} apples".format("five"))
#변수
number = 3
print("I eat {0} apples".format(number))
#2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days".format(number, day))
# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days".format(number = 10, day = "three"))
# 인덱스와 이름 혼용하기
print("I ate {0} apples. so I was sick for {day} days".format(10, day = "three"))
