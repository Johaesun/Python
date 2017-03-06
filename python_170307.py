#파이썬 크롤링 루리웹 1페이지부터 19페이지까지 게시판 글제목받아오기
from bs4 import BeautifulSoup
import urllib.request

for i in range(1, 20):
    response=urllib.request.urlopen('http://bbs.ruliweb.com/ps/board/300416/list?page={0}'.format(i))
    page = response.read().decode('utf-8','ignore')
    soup = BeautifulSoup(page, 'html5lib')
    list = soup.findAll('div',attrs={'class':'relative'})
    for item in list:
        title = item.find('a').text
        print(title)
