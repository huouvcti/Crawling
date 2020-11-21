import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from tkinter import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("lang=ko_KR")


window = Tk()
window.title("뉴스 제목 가져오기")
window.config(bg="#FFD8D8")


def search():
    keyword = keyword_input.get()

    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)

    base_url = ("https://www.google.com/search?q=" + keyword + "&tbm=nws&start={}")

    # 10, 20, 30, ...
    for i in range(10):
        url = base_url.format(i * 10)
        driver.get(url)
        html = driver.page_source
        soup = bs(html, "html.parser")
        title_list = soup.find_all("div", {"class": "JheGif nDgy9d"})

        for title in title_list:
            print(title.text)
    driver.close()


# 뉴스 제목
keyword_label = Label(window, text="키워드를 입력하세요", bg="#FFD8D8", font="맑은고딕")
keyword_input = Entry(window,  width=20, font="15")
keyword_btn = Button(window, text="입력", width=15, command=search)
keyword_label.grid(row=0, column=0, columnspan=2, pady="30")
keyword_input.grid(row=1, column=0, ipadx=10, ipady=5, padx=10, pady=10)
keyword_btn.grid(row=1, column=1,  ipady=5, padx=10, pady=10)

window.mainloop()