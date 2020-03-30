#  리스트 관련 함수들

# 리스트에 요소 추가 (append)
a = [1,2,3]
a.append(4)
# 1,2,3,4 출력
print(a)
# 리스트에 리스트를 추가하는 경우
a.append([5,6])
# 1,2,3,4,[5,6] 출력
print(a)

# 리스트 정럴 (sort)
a = [1,4,3,2]
a.sort()
print(a)
#  문자 (알파벳 정렬)
a = ['a','c','b']
a.sort()
print(a)

# 리스트 뒤집기 (reverse)
a = ['a','c','b']
a.reverse()
print(a)

# 위치 반환(index)
# index 함수는 리스트에 x 값이 있으면 x의 인덱스 값을 반환
a = [1,2,3]
# 2 출력
print(a.index(3))
# a.index(0)
#  위의 a 리스트에는 0이라는 값이 존재하지 않기 때문에 ValueError 가 발생한다.

# 리스트에 요소 삽입 (insert)
a = [1,2,3]
a.insert(0,4)
# 4,1,2,3 출력
print(a)
# insert(인덱스 , 값)

# 리스토 요소 제거 (remove)
a = [1,2,3,1,2,3]
a.remove(3)
# 1,2,1,2,3 출력
print(a)
# 리스트에 3이라는 값을 2개 가지고 있지만 앞의 값만 삭제

# 리스트의 요소 빼내기 (pop)
a = [1,2,3]
#  3 출력
print(a.pop())
# 1,2 출력
print(a)
# 2 출력
print(a.pop(1))
#  1 출력
print(a)

# 리스트에 포함된 요소 x 의 개수 세기 (count)
a = [1,2,3,1]
# 2 출력
print(a.count(1))

#  리스트 확장 (extend)
# extend(x) 에서 x 에는 리스트만 올수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.
a = [1,2,3]
a.extend([4,5])
# 1,2,3,4,5 출력
print(a)

b = [6,7]
a.extend(b)
# 1,2,3,4,5,6,7 출력 
print(a)
# a.extend([4,5]) 는 a += [4,5] 와 동일하다