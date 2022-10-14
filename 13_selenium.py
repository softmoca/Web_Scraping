from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)


# 1. 네이버 이동
browser.get("http://naver.com")
elem = browser.find_element_by_class_name("link_login")
