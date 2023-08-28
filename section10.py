# 모듈
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning
price(5)
price_morning(6)
price_soldier(7)

from theater_module import price_soldier as price
price(5)



# 패키지
# = 모듈들을 모아둔 집합
# import만 쓸 땐, thailand 부분은 모듈이나 패키지만 가능. 클래스나 함수는 불가.
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from import를 사용하면 모듈, 패키지, 클래스, 함수 모두 가능
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()



# __all__
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()



# 패키지, 모듈 위치
import inspect
import random
print(inspect.getfile(random))      # random 모듈이 어느 위치에 있는지 파일 정보를 알려줌
print(inspect.getfile(thailand))



# pip install
# 구글에 pypi 검색
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list -> 현재 설치되어 있는 패키지 내용을 볼 수 있음
# pip beautifulsoup4 -> 패키지에 대한 정보
# pip install --upgrade 패키지 이름 -> 업그레이드
# pip uninstall beautifulsoup4 -> 패키지 삭제



# 내장함수
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다 !".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random       # 외장 함수
print(dir())
import pickle
print(dir())

print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))

# 구글에 list of python builtins 검색하면 파이썬 내장함수 검색 가능



# 외장함수
# 직접 import를 해서 사용해야 함
# 구글에 list of python modules 검색
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py"))    # 확장자가 py인 모든 파일


# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())    # 현재 디렉토리 표시

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)     # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())


# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%m:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())


# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()   # 오늘 날짜 저장
td = datetime.timedelta(days=100)   # 100일 저장
print("우리가 만난지 100일은", today+td)



# Quiz 1) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 황다은에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : hde7759@naver.com

import byme
byme.sign()