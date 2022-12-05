import requests
import re

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
#引入 headers

url=input("请输入MISS VIDEO 链接：")
r=requests.get(url,headers=headers)
html=r.text

result=re.search('<a href="https://mypikpak.com/drive/.*?;__add_url=(.*?)" target=".*?" rel=".*?" class=".*?">',html,re.S)
url_pt=[]
url_pt=result.group()

print('请使用下载软件，视频文件地址：',url_pt)