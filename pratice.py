#11-1 모듈

# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인인 영화 보러 갔을 때

#import theater_module as mv
#mv.price(3)
#mv.price_morning(4)
#mv.price_soldier(5)

#from theater_module import *
# from random import *
#price(3)
#price_morning(4)
#price_soldier(5)

#from theater_module import price, price_morning
#price(5)
#price_morning(6)
#price_soldier(7)

#from theater_module import price_soldier as price
#price(5)

# 11-2 패키지 : 모듈들을 모아 놓은 집합

#import travel.thailand # 모듈이나 패키지만 임포트 가능(클래스나 함수는 불가)
#trip_to = travel.thailand.ThailandPackage()
#trip_to.detail()

#from travel.thailand import ThailandPackage # 클래스, 함수도 임포트 가능
#trip_to = ThailandPackage()
#trip_to.detail()

#from travel import vietnam
#trip_to = vietnam.VietnamPackage()
#trip_to.detail()

# 11-3 __all__

#from travel import *
#trip_to = vietnam.VietnamPackage()
#trip_to = thailand.ThailandPackage()
#trip_to.detail()

# 11-4 모듈 직접 실행

# 11-5 패키지, 모듈 위치
#import inspect
#import random
#print(inspect.getfile(random))
#print(inspect.getfile(thailand))

#11-6 pip install : pip로 패키지 설치하기

#from bs4 import BeautifulSoup
#soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
#print(soup.prettify())

#11-7 내장함수

# input : 사용자 입력을 받는 함수
#language = input("무슨 언어를 좋아하세요?")
#print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
#print(dir())
#import random # 외장합수
#print(dir())
#import pickle
#print(dir())

#print(dir(random))

#lst = [1, 2, 3]
#print(dir(lst))

#name = "Jim"
#print(dir(name))

# 11-8 외장 함수 : 직접 입력하여 사용하는 함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
#import glob
#print(glob.glob("*.py")) #확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
#import os
#print(os.getcwd()) # 현재 디렉토리

#folder = "sample_dir"

#if os.path.exists(folder):
#    print("이미 존재하는 폴더입니다.")
#    os.rmdir(folder) # 폴더 삭제(remove)
#    print(folder, "폴더를 삭제하였습니다.")
# else:
#    os.makedirs(folder) # makedirs() : 폴더 생성
#    print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

#import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후


# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py로 작성

#(모듈 사용 예제)
import byme
byme.sign()

#(출력 예제)
#이 프로그램은 나도 코딩에 의해 만들어졌습니다.
#유튜브 : http://youtube.com
#이메일 : nadocoding@gmail.com

###