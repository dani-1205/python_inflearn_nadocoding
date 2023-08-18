# 표준 입출력
print("Python", "Java", sep = ", ", end = "?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":")
    # ljust -> 총 8칸을 확보한 상태에서 왼쪽으로 정렬
    # rjust -> 총 4칸을 확보한 상태에서 오른쪽으로 정렬

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill -> 3 크기만큼의 공간을 확보하고 값을 집어 넣는데, 값이 없는 빈공간은 0으로 채움

# 사용자 입력을 통해 값을 받게 되면 항상 문자열 형태로 저장됨
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

answer = 10
print(type(answer))
print("입력하신 값은 " + str(answer) + "입니다.")



# 다양한 출력포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))



# 파일 입출력
# 파일 만들기
score_file = open("score.txt", "w", encoding = "utf8")
# w -> 파일을 쓰기 위한 목적으로 열겠다고 정의
# encoding = "utf8" -> 한글을 사용하기 위해 항상 쓰는 것을 추천
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()    # 파일을 열었으면 꼭 닫아주기

score_file = open("score.txt", "a", encoding = "utf8")
# a -> 파일을 이어서 쓰겠다는 의미
score_file.write("과학 : 30")
score_file.write("\n코딩 : 100")
score_file.close()



# 파일 읽어오기
score_file = open("score.txt", "r", encoding = "utf8")
# r -> 파일을 읽어오는 용도로 사용
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())    # 줄바꿈을 하고 싶지 않다면 뒤에 end="" 적으면 됨
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close



# pickle
# 프로그램에서 사용하고 있는 데이터를 파일 형태로 저장하는 것
import pickle
profile_file = open("profile.pickle", "wb")     # b -> binary로 pickle을 사용하기 위해서 항상 정의해야 함
profile = {"이름":"박명수", "나이":"30", "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)      # profile에 있는 정보를 file에 저장
                                        # 가장 중요 ! pickle을 이용해서 이 정보를 파일에 작성하는 것
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)     # file에 있는 정보를 profile에 불러오기
                                        # 파일에 있는 내용을 그대로 가지고 와서 데이터 형태로 불러옴
print(profile)
profile_file.close()



# with
# 마지막에 close를 사용할 필요가 없음
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())



# Quiz 1) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
#         보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as week_file:
        week_file.write("- {0} 주차 주간보고 - ".format(i))
        week_file.write("\n부서 : ")
        week_file.write("\n이름 : ")
        week_file.write("\n업무 요약 : ")