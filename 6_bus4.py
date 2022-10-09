import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()
# 첫번째 인자로 html문서값를 lxml를 통해서 객체로 만든것. soup이 모든 정보를 가지고 있다.
soup = BeautifulSoup(res.text, "lxml")


# print(soup.title)
# print(soup.title.get_text())  # 문자만 빼올 수 있다.
# print(soup.a)  # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs)  # a element 의 속성 정보를 출력
# print(soup.a["href"])  # a element 의 href 속성 '값' 정보를 출력


# print(soup.find("a", attrs={"class": "Nbtn_upload"}))     # class="Nbtn_upload" 인 a element 를 찾아줘

# print(soup.find(attrs={"class": "Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

#print(soup.find("li", attrs={"class": "rank01"}))
#rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())


# print(rank1.next_sibling)  # 아마 줄바꿈(개행) 이 있어서 next_sibling을 한번 더 해줘야함
# print(rank1.next_sibling.next_sibling)


# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# 개행이 있어 두번적는걸 방지하지 위해  rank1 li기준으로 "li"인것만 찾는다.
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))  # rank1 기준으로 모든 형제들을 가져온다.


#  text가 저거에 해당하는 a태그를 가져온다.
webtoon = soup.find("a", text="퀘스트지상주의-51화 원래 그렇게 문란하냐고")
print(webtoon)
