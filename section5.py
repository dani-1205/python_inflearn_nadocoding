# if
weather = "비"
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")

weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요. 나가지 마세요.")
elif temp >= 10 and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")



# for
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{}님, 커피가 준비되었습니다.".format(customer))



# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1
# # 무한 루프를 빠져나오는 법은 ctrl + c

customer = "토르"
person = "Unknown"

while person != "토르":
    print("{}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")



# continue와 break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue        # 계속해서 다음 반복을 진행
    elif student in no_book:
        print("오늘 수업 여기까지.{0}는 교무실로 따라와.".format(student))
        break           # 지금 상황에서 바로 반복문을 종료
    print("{0}, 책을 읽어봐.".format(student))



# 한 줄 for
# 원래 출석 번호가 1, 2, 3, 4인데, 앞에 100을 붙이기로 함. -> 101, 102, 103, 104 . . .
students = [1, 2, 3, 4, 5]
students = [i + 100 for i in students]
print(students)

# 학생들의 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)



# Quiz 1) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *
count = 0       # 총 탑승 승객

for i in range(1, 51):
    time = randrange(5, 51)         # 조건 1
    if 5 <= time <= 15:    # 조건 2
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {}분".format(count))