#튜플의 개념을 이해하기위한 예제

# 1.튜플만들기  
# 
# 익숙치 않지만 리스트랑은 약간 다르네? 
# 리스트는 print시 ()가 없는데 얘는 ()를 넣네?
colors = ("red", "blue", "green")
print(colors)
colors = ("red", "blue", "green")
print(colors)
colors = ("red", "blue", "green")
print(colors)
colors = ("red", "blue", "green")
print(colors)
colors = ("red", "blue", "green")
print(colors)
colors = ("red", "blue", "green")
print(colors)
colors = ("red", "blue", "green")
print(colors)
colors = ("red", "blue", "green")
print(colors)



# 2.값꺼내기 (인덱싱)
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
# 인덱싱의 값을 꺼낸다?
#   일단 4줄 정도 연습해보니 생각나는건 인덱스의 번호를 꺼내는건 알겠지만
#   아직 잘 와닿진 않는데 인덱스를 꺼내는것도 아직 익숙치 않아 살짝 헷갈리는듯?
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2]) # nubers라는 명칭을 가진 10,20,30이 들어간 리스트를 만들어 인덱스를 꺼내는 작업을 하는 것이지만 튜플 문법이기에 리스트안 내용물이 변치 않는 값을 내놓는다 라는게 맞겠지?
numbers = (10, 20, 30)  
print(numbers[0]) # 10이 나올꺼고,
print(numbers[2]) # 30이 나오겠지?
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = (10, 20, 30) # 기호넣는것도 아직 익숙치 않네ㅋㅋ
# 한글과 영타를 연달아 바꾸는것도 의식으로 해야하니 더 서투른것 같기도?
print(numbers[0]) # number과 numbers로 따로 인식을 해야하는데 같이 해버리네? 
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0]) # print도 쓸때 나도 모르게 s를 넣게되니 이것또한 연습이 필요한것 같음
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0]) #나도 모르게 헷갈려서 리스트를 두번 기입했네ㅋㅋ 
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
numbers = 10, 20, 30 # 괄호를 깜빡 잊었네
numbers = (10, 20, 30)
prints(numbers[0]) # 또 s를 넣었네
print(numbers[2])
numbers = (10, 20, 30) #띄어쓰기도 익숙치 않아 흠..
print(numbers[0])
print(numbers{2}) # 묶은 채로 프린트를 하려하네ㅋㅋ
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])
# 쓰는것도 좀 버겁네? 여기서 멈추고 넘어가자

# 3.값을 바꾸려고 한다면?
numbers = (1, 2, 3)
numbers[0] = 100 # ? 인덱스 0번에 100을 할당하면 들어가지나?
numbers = (1, 2, 3) #띄어쓰기가 은근 헷갈리네?
numbers[0] = 100
numbers =(1, 2, 3)
numbers[0] = 100
numbers = (1, 2, 3)
numbers[0] = 100 # 조금씩 연습을 해보니 나에게 절실한건 객체 부터 써버릇하는 연습이 필요하긴 하네ㅋㅋ
numbers = (1,2,3)
numbers[0] = 100
numbers = (1, 2, 3)
numbers[0] = 100 #뜨어쓰기 헷갈려ㅋㅋㅋ
numbers = (1,2,3)
numbers[0] = 100
numbers = (1, 2, 3)
numbers = 100
# 사실 더 연습 하고 싶지만 여기서 그만하고 모든 개념 훓어보는걸 먼저 하자 그리고 연습하는게 순서가 맞는것 같아.
# 4.실수 방지용 데이터?
birth = (1995, 3, 21)
print("태어난 해:", birth[0])
# 생년월일은 바뀌면 안되기에 튜플이 어울린다.

# 5.여러 값 한번에 담기
person = ("이름", 25, "학생")
name = person[0]
age = person[1]

print(name, age)
# 서로 관련있는 값을 묶어보기 
# 예제 5번까지는 튜플 전용 예제 그 뒤는 심화 

