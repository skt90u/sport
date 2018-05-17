import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

col01 = [] # 隊伍
col02 = [] # 勝
col03 = [] # 負
col04 = [] # 勝率
col05 = [] # 勝差
col06 = [] # 主場
col07 = [] # 客場
col08 = [] # 分區
col09 = [] # 分組
col10 = [] # 近10場
col11 = [] # 連勝或連負

res = requests.get('https://www.msn.com/zh-tw/sports/nba/standings/sp-vw-lge')
soup = BeautifulSoup(res.text, 'html.parser')
divs = soup.find_all('div', 'tablegroupbytitle')

for div in divs:
    area = div.find('h3').text # 東區, 西區
    tables = div.find_all('table', 'tableview')
    for table in tables:
        trs = table.find('tbody').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            col01.append(tds[1].find('a').text)
            col02.append(tds[3].text)
            col03.append(tds[4].text)
            col04.append(tds[5].text)
            col05.append(tds[6].text)
            col06.append(tds[7].text)
            col07.append(tds[8].text)
            col08.append(tds[9].text)
            col09.append(tds[10].text)
            col10.append(tds[11].text)
            col11.append(tds[12].text)
   
df = pd.DataFrame({
 		'隊伍': col01,
 		'勝': col02,
 		'負': col03,
 		'勝率': col04,
 		'勝差': col05,
 		'主場': col06,
 		'客場': col07,
 		'分區': col08,
 		'分組': col09,
 		'近10場': col10,
 		'連勝或連負': col11
         })

file_name = 'C:\\NBA聯盟排名-' + datetime.datetime.today().strftime('%Y-%m-%d') +'.csv'
df.to_csv(file_name , sep=',')    
