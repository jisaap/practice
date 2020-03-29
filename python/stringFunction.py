# 문자 개수 세기(count)
a = "hobby"
# 문자열.count(찾을 문자)
print(a.count("b"))
#위치 알려주기 (find)
a = "Python is the best choice"
#문자열중 찾는 문자가 처음나온 위치를 반환한다.
# 만약 찾는 문자나 문자열이 존재하지 않는다면 -1 을 반환한다.
print(a.find('b'))
print(a.find('k')) # << 없어도 -1 반환

#위치 알려주기2 (index)
#문자열중 찾는 문자가 처음으로 나온 위치를 반환한다.
# find 와 다른점은 찾는 문자나 문자열이 존재하지 않는다면 에러를 발생시킨다.
a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) << 없으면 에러 발생

#문자열 삽입(join)
# 문자열의 각각의 문자사이에 지정하는 값을 삽입한다.
print(",".join("abcd"))
#join 함수로 리스트를 사용하는 예제
print(",".join(['a', 'b', 'c', 'd']))
#소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())
#대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower())
#왼쪽 공백 지우기 (lstrip)
a = '     hi      '
print(a.lstrip())
#오른쪽 공백 지우기 (rstrip)
a = '     hi      '
print(a.rstrip())
#양쪽 공백 지우기 (strip)
a = '     hi      '
print(a.strip())

#문자열 바꾸기 (replace)
# replace(바뀌게 될 문자열, 바꿀 문자열) 처럼 사용해서 문자열 간의 특정한 값을 다른 값으로 치환해 준다.
a = "Life is too short"
print(a.replace("Life","Your leg"))
# 문자열 나누기(split)
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(":"))