#  반복해서 문장을 수행해야 할 경우 반복문을 사용한다.
#  while문은 조건이 True 인 동안에 내부의 문장을 반복 한다.

treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다.')


# while문 만들기

prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """

number = 0
while number != 4:
    print(prompt)
    # number = int(input())
    number = 4
# while문 강제로 빠져 나가기
# while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다.
# 하지만 강제로 while문을 빠져나가고 싶을때가 있다. 이때 사용 할수 있는 것이 break문이다.

coffe = 10
money = 300

while money:
    print('커피')
    coffe = coffe - 1
    print('남은 커피의 양은 %d개 입니다.' % coffe)
    if coffe == 0:
        print('커피가 다 떨어졌습니다.')
        break

#  money가 300으로 고정 되어 있으므로 money가 0이 아니기 때문에 항상 참이기 때문에 무한반복문이지만
#  coffe가 0이 되면 빠져나오는 탈출문을 작성하였기 때문에 무한 반복문에 빠지지 않는다.

# while문의 맨 처음으로 돌아가기
# while문 안의 문장을 수행할 때 입력조건을 검사해서 조건에 맞지 않으면 while문을 빠져나간다.
#  while문의 맨처음 조건문으로 다시 돌아게가 만들고 싶은 경우 continue를 사용한다.
a = 0
while a < 10:
    a = a + 1
    if a % 2 ==0: continue
    print(a)

# 무한 루프문 
while True:
    print('Ctrl + c 를 눌러야 while 문을 빠져나갈수 있습니다.')
    #  Ctrl + c :  python 프로그램이 실행되는 동안 python는 KeyboardInterrupt 예외를 발생시킨다.
    