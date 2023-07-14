# 슬라이싱
jumin = "001205-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤부터) : " + jumin[-7:])



# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))

print(python.find("Java"))      # find에서 찾는 것이 없으면 -1을 반환
print(python.index("Java"))     # index에서 찾는 것이 없으면 오류 발생

print(python.count("n"))



# 문자열 포맷
# 방법 1
print("나는 %d살입니다." % 20)              # %d : 정수값
print("나는 %s를 좋아해요." % "파이썬")      # %s : 문자열
print("Apple은 %c로 시작해요." % "A")       # %c : 문자 하나
print("나는 %s색과 %s색을 좋아해요." % ("빨간", "파란"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("빨간", "파란"))
print("나는 {0}색과 {1}색을 좋아해요.".format("빨간", "파란"))  # 순번에 맞게 출력 가능
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 24, color = "하얀"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "하얀", age = 24))



# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \". \' : 문장 내에서 따옴표
print("저는 \"황다은\"입니다.")

# \\ : 문장 내에서 \
print("문장에 \\이 있다")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")



# Quiz 1) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e' 개수 + '!'로 구성
#                   (nav)               (5)           (1)             (!)
# 예) 생성된 비밀번호 : nav51!\

url = "http://naver.com"
n_url = url[7:url.find(".")]

password = n_url[:3] + str(len(n_url)) + str(url.count("e")) + "!"

print(password)


# 규칙 1 조금 더 편리하게 작성하는 법
url = "http://naver.com"
n_url = url.replace("http://", "")
n_url = n_url[:n_url.find(".")]

password = n_url[:3] + str(len(n_url)) + str(url.count("e")) + "!"

print(password)