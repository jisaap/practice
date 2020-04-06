# 집합 자료형은 집합에 관련한 것을 쉽게 처리하기 위해 만든 자료형이다.
#  집합 자료형은 set 키워드를 사용해 만들수 있다.
s1 = set([1,2,3])
# 1,2,3 출력
print(s1)
s2 = set('hello')
# e,h,l,o 출력(순서 없음)
print(s2)
#  비어있는 집합 자료형
s = set()

# 집합 자료형은 중복을 허용하지 않고 순서가 없다.
#  자바의 set 이랑 비슷함
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을수 있지만 
# set 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을수 없다.

# 집합을 리스트 / 튜플로 변환해 인덱싱 사용하기
s1 = set([1,2,3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[1])

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
# 교집합
sum = s1 & s2
# 4,5,6 출력
print(sum)

sum = s1.intersection(s2)
# 4,5,6 출력
print(sum)

# 합집합
num = s1 | s2
# 1,2,3,4,5,6,7,8,9 출력
print(num)

num = s1.union(s2)
# 1,2,3,4,5,6,7,8,9 출력
print(num)

# 차집합
num = s1 - s2
# 1,2,3 출력
print(num)
num = s2 - s1
# 7,8,9 출력
print(num)

num = s1.difference(s2)
# 1,2,3 출력
print(num)
num = s2.difference(s1)
# 7,8,9 출력
print(num)

# 집합 자료형의 함수

# 값 1개 추가하기 (add)
s1 = set([1,2,3])
s1.add(4)
# 1,2,3,4 출력
print(s1)

# 값 여러개 추가하기 (update)
s1 = set([1,2,3])
s1.add([4,5,6])
# 1,2,3,4,5,6 출력
print(s1)

# 특정값 제거하기 (remove)
s1 = set([1,2,3])
s1.remove(2)
# 1,3 출력
print(s1)