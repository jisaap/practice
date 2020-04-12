# python에서 사용하는 변수는 객체를 가리키는 것이라고도 말할수 있다.
a = [1,2,3]
# 위의 a리스트 자료형은 [1,2,3]의 값을 가지는 리스트 자료형이 자동으로 메모리에 생성되고
#  변수 a 는 [1,2,3]리스트가 저장된 메모리의 주소를 가리키게 된다.
# 변수 a가 가리키는 주소값
print(id(a))

# 리스트를 복사 할때
# a 변수가 가지고 있는 주소값을 변수 b 에 대입
#  두 변수가 참조하는 객체의 주소값은 일치하기 때문에 서로 변수의 값을 수정 삭제 할수 있다.
a = [1,2,3]
b = a
a[1] = 4
print(b)
# :이용하기
# :를 이용하는 경우 a 리스트의 값을 바꾸더라도 b 리스트에는 영향을 끼치지 않는다.
a = [1,2,3]
b = a[:]
a[1] = 4
print(b)

# copy 모듈 이용
# copy 함수를 쓰기 위해 import 해줌
from copy import copy
# copy함수를 사용하는 경우 b = a[:]와 같이 값을 직접 대입한다.
b = copy(a)
# a 와 b를 비교해도 주소값이 다르다는 것을 알수있다.
print(a is b)

# 변수를 만드는 방법

# 튜플로 a,b에 값을 대입
a,b = ('python','life')
# python
print(a)
# life
print(b)
# 튜플은 괄호 생략이 가능
(a,b) = 'python','life'
# python
print(a)
# life
print(b)

# 리스트 변수 만들기
[a,b] = ['python','life']
print(a)
print(b)
# 여러개의 변수에 같은값 대입하기
a = b = 'python'
print(a)
print(b)

# 값 자유롭게 바꾸기
a = 3
b = 5
print(a)
print(b)
a,b = b,a
print(a)
print(b)