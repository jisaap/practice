# 들여쓰기
# if문을 만들때 바로 아래문장부터 if문에 속하는 모든 문장에 들여쓰기를 해주어야 한다.

if 'a' == 'a':
    print('a')

money = True
if money :
    print('택시를')
# print('타고') 에러
        # print('가라') 에러
#  조건문 다음에 꼭 : 콜론을 붙여줘야한다.
#  비교 연산자 and / or / not
money = 2000
card = True
if money >= 3000 or card:
    print("충분")
else:
    print('모자라')

# in / not in 특이한 조건문
print(1 in [1,2,3])
print('j' not in 'python')

pocket = ['paper','cellphone', 'money']
if 'money' in pocket:
    print('있다!!')
else:
    print('없다!!')

# 조건문에서 아무일도 하지 않게 설정
pocket = ['paper','cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print('없어!')

# 다양한 조건을 판단하는 elif
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
# ------------------------- elif로 바꾸기 else if
pocket = ['paper', 'cellphone', 'money']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card: 
    print("택시를 타고가라")
else:
    print("걸어가라")

# if문 한줄로 작성하기
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print('카드 꺼내')

# 조건부 표현식
#  삼항 연산자 처럼 사용 가능
#  가독성이 좋고 한줄로 작성할수 있다.
score = 60
if score >= 60:
    message = 'success'
else:
    message = 'failure'
# -----------------------
message = 'success' if score >= 60 else 'failure'
