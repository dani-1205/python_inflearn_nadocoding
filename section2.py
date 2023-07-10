# 연산자
print(10/4)
print(10%4)     #나머지
print(13//4)    # 몫

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))



# 숫자 처리 함수
print(abs(-5))      # 절댓값
print(pow(4, 2))    # 제곱
print(max(5, 12))
print(min(5, 12))
print(round(3.14))  # 반올림
print(round(4.99))

from math import *
print(floor(4.99))  # 내림
print(ceil(3.14))   # 올림
print(sqrt(16))     # 제곱근



# 랜덤 함수
from random import *
print(random())         # 0.0 이상 1.0 미만의 임의의 값을 생성
print(random() * 10)    # 0.0 이상 10.0 미만의 임의의 값을 생성
print(int(random() * 10))   # 0 이상 10 미만의 임의의 값을 생성
print(int(random() * 10) + 1)   # 1 이상 10 이하의 임의의 값을 생성

print(randrange(1, 46))     # 1이상 46미만의 임의의 값을 생성

print(randint(1, 45))       # 1이상 45이하의 임의의 값을 생성



# Quiz 1) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#         월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
#         아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3 : 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외

# 출력문 예제 : 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")