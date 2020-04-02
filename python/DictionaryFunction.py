#   딕셔너리 관련 함수들

# Key리스트 만들기 (Keys)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
b = a.keys()
#  a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다.
# dict_keys(['name', 'phone', 'birth'])
print(b)

# for in 문 이용 방법
for k in a.keys():
    print(k)

# dict_keys 객체를 리스트로 변환
print(list(a.keys()))

# value 리스트 만들기(values)
b = a.values()
print(b)

# 딕셔너리 key , value 쌍 얻기(items)
b = a.items()
print(b)

# key , value 쌍 모두 지우기 (clear)
a.clear()
print(a)

# key로 value 값 얻기
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
b = a.get('name')
print(b)
b = a.get('phone')
print(b)
# None << (거짓) 없는 key 값으로 value 를 얻으려 할때 나온다
b = a.get('nokey')
print(b)
# 딕셔너리안에 찾으려는 key 값이 없을 경우 미리 정해둔 디폴드 값을 대신 가져오게 할수 있다.
#  get(x,'디폴트 값')
b = a.get('foo','bar')
print(b)

# 해당 key가 딕셔너리 안에 있는지 조사하기 (in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)
# 'name' 문자열은 a 딕셔너리의 Key 중 하나이다. 따라서 'name' in a를 호출하면 참(True)을 돌려준다. 반대로 
# 'email'은 a 딕셔너리 안에 존재하지 않는 Key이므로 거짓(False)을 돌려준다.
