# 변수
animal = "강아지"
name = "초코"
age = 2
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

# +를 사용할 경우 str()을 써야 함
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")

# ,를 사용할 경우 str()을 안 써도 됨
print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요")



# Quiz 1) 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : XX 행 열차가 들어오고 있습니다.

print("")
print("Quiz 1")
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")