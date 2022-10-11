import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
filename = "시가총액1-200.csv"
# newline이 없으면csv에 들어갈때 각 열마다 띄어쓰기가됨
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
# split함수는 구분자를 기준으로 리스트로 만든다.
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))
writer.writerow(title)

for page in range(1, 3):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 의미 없는 데이터는 skip
            continue
        # data에는 각 td들이 가지고 있는 text가 저장
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)  # 리스트 형태로 넣어줘야한다.
