# 리스트
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨가 유재석씨와 조세호씨 사이에 탐
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형을 함께 사용할 수 있음
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
a_list = [1, 2, 3]
b_list= ["어제", "오늘", "내일", 3]
a_list.extend(b_list)
print(a_list)



# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

print(cabinet[5])     # 오류가 발생하고 뒤로는 실행이 안 됨
print(cabinet.get(5))   # None 출력
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)



# 튜플
# 리스트와는 다르게 내용 변경이나 추가가 불가능함
# 속도가 리스트보다 빨라서 변경되지 않는 목록을 사용할 때 튜플을 활용함
menu = ("돈까스", "치킨까스", "돈까스")
print(menu[0])
print(menu[1])
print(menu)

name = "김종국"
age = 20
hobby = "여행"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "여행")
print(name, age, hobby)



# 집합 (set)
# 중복이 안되고, 순서가 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "나영석"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합 (java는 가능하지만 python은 불가능한 사람)
print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김태호")
print(java)



# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))



# Quiz 1) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


from random import *
id_list = list(range(1, 21))

shuffle(id_list)
print(id_list)

winners = sample(id_list, 4)
print(winners)

chicken_winners = winners[0]
coffee_winners = winners[1:]

print("-- 당첨자 발표 --")
print("치킨 당첨자 : %s" % chicken_winners)
print("커피 당첨자 : %s" % coffee_winners)
print("-- 축하합니다 --")