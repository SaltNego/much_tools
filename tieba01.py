# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         tieba01
# python3!!!
# Date:         2020/2/11
__Author__ = 'Negoo_wen'
#-------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

print('''
 _____ _      _               ____                      _     
|_   _(_) ___| |__   __ _    / ___|  ___  __ _ _ __ ___| |__  
  | | | |/ _ \ '_ \ / _` |   \___ \ / _ \/ _` | '__/ __| '_ \ 
  | | | |  __/ |_) | (_| |    ___) |  __/ (_| | | | (__| | | |
  |_| |_|\___|_.__/ \__,_|   |____/ \___|\__,_|_|  \___|_| |_|  from Negoo_wen
''')

def main():
    while True:
        url = input('Please input index url:\n')
        if url == 'exit':
            exit()
        #url = 'http://tieba.baidu.com/home/main?un=' + url
        #url = 'http://tieba.baidu.com/home/main?un=%E5%AD%A9%E5%AD%90%E6%B0%94%E5%A4%A9%E7%84%B6%E5%91%86&ie=utf-8&id=tb.1.a84c0d02.LG92Eg-zR8cHFzxwmbN0sQ&fr=pb&ie=utf-8'
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            demo = r.text
            soup = BeautifulSoup(demo, 'html.parser')

            for link in soup.find_all('a', 'btn-send-gift j-send-gift'):
                print('\n\n-------------------------------------------------------------------------------\n')
                print('[+] Id 和 用户名为：' + link.get('data-gift'))
                print('\n-------------------------------------------------------------------------------\n\n')
        except:
            print("环境错误!请重试 ^_^")

if __name__ == '__main__':
    main()
