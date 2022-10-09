import requests
url = requests.get("https://moca9012.tistory.com/manage/posts/")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)  # url주소로 이동할때 user-Agent 값을 준다.
res.raise_for_status()

with open("moca.html", "w", encoding="utf8") as f:
    f.write(res.text)
