# 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.

# 과목	점수
# 국어	80
# 영어	75
# 수학	55
ran = 80
eng = 75
mat = 55
averge = (ran + eng + mat) / 3
print(averge)

# 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
num = 13
if(num% 2 == 0):
    print('짝수')
else:
    print('홀수')

#     홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# ※ 문자열 슬라이싱 기법을 사용해 보자.
import datetime
id = '881120-1068234'
print(datetime.datetime.strptime(id[:6],'%y%m%d').strftime('%Y-%m-%d'))
print(id[7:])


# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
# >>> pin = "881120-1068234"
# ※ 문자열 인덱싱을 사용해 보자.
id = "881120-1068234"
if(int(id[7]) == 1 or int(id[7]) == 3):
    print('남자')
else:
    print('여자')


# 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

a = "a:b:c:d"
print(a)
a = a.replace(':','#')
print(a)

# [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

# ※ 리스트의 내장 함수를 사용해 보자.
arr = [1, 3, 5, 4, 2]
arr.sort()
print(arr)
arr.reverse()
print(arr)

# ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.

# ※ 문자열의 join 함수를 사용하면 리스트를 문자열로 쉽게 만들 수 있다.

strs = ['Life', 'is', 'too', 'short']
print("".join(strs))

# (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.

# ※ 더하기(+)를 사용해 보자.
tu = 1,2,3
tu = tu + (4,)
print(tu)

# 다음과 같은 딕셔너리 a가 있다.

# >>> a = dict()
# >>> a
# {}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'
# a[250] = 'python'
# 3번 a[[1]] = 'python' 은 값이 아니고 인덱스가 들어 있어서 에러가 나는 것 같다.


# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.

a = {'A':90, 'B':80, 'C':70}
# ※ 딕셔너리의 pop 함수를 사용해 보자.
print(a.pop('B'))

# a 리스트에서 중복 숫자를 제거해 보자.

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# ※ 집합 자료형의 요솟값이 중복될 수 없다는 특징을 사용해 보자.
print(a)
s = set(a)
print(s)

# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)
#  동일한 주솟 값을 참조 하고 있기 때문에 하나의 변수에서 값을 조작해도 다른 변수가 영향을 받는다.
#  하나의 주솟 값이아닌 값을 가지면 이러한 문제를 없앨수 있다. 
c = a[:]
a[1] = 5
print(a)
print(b)
print(c)

