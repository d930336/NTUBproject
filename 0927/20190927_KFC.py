import requests
from bs4 import BeautifulSoup
import shutil
import pandas as pd

url = "https://www.kfcclub.com.tw/tw/Coupon/"
respond = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
html = BeautifulSoup(respond.text)
main = html.find_all('div',attrs={'style': 'cursor:pointer;text-align:center'})

# 準備空的 dataFrame
df = pd.DataFrame(columns=['id', 'title', 'note', 'notice'])

for item in main:
    img_src = item.find("img")['src']
    img_name = item.find("img")['code']

    # 網頁內容
    title = item.find("img")['t']
    note = item.find_all("p")
    expire_date = ""
    for expire in note:
        expire_date = expire_date + expire.text
    print(expire_date)
    notice = item.find("img")['onclick'].split(',')[3]

    #------------轉成excel--------------
    # 將資料存入DataFrame
    s = pd.Series([img_name, title, expire_date, notice],
                  index=['id', 'title', 'note', 'notice'])
    df = df.append(s, ignore_index=True)

    #------------儲存圖片--------------
    r = requests.get(img_src, stream=True, headers={'User-agent': 'Mozilla/5.0'})  # stream=True 则会推迟响应内容的下载

    if r.status_code == 200:
        with open("C:/Users/case-pc/Desktop/KFC/"+ img_name + ".jpg", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

print(df)
df.to_excel("KFC.xlsx", encoding='utf-8', index=False)

