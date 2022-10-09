import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res = requests.getd(url)
res.raise_for_status()
# 첫번째 인자로 html문서값를 lxml를 통해서 객체로 만든것. soup이 모든 정보를 가지고 있다.
soup = BeautifulSoup(res.text, "lxml")


# 네이버 웹툰 전체 목록 가져오기

# find만 하면 그 해당하는 첫번째만 가져오는것이고 all을 하면 전체를 다 가져온다.
# class 속성이 title 인 모든 "a" element 를 반환
cartoons = soup.find_all("a", attrs={"class": "title"})
# 태그명이 a이고 class가title인걸 가져온다.
for cartoon in cartoons:
    print(cartoon.get_text())
