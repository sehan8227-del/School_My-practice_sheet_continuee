#튜플의 개념을 이해하기위한 예제

# 1.튜플만들기  
colors = ("red", "blue", "green")
print(colors)

# 2.값꺼내기 (인덱싱)
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[2])

# 3.값을 바꾸려고 한다면?
numbers = (1, 2, 3)
numbers[0] = 100

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

