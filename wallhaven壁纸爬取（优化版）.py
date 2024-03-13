# 优化版：1.增加了异步爬取壁纸的功能
#       2.增加了对照片有无的判断
#       3.增加了一个爬取时长的限制（爬取时间大于20s，停止爬取）
#       4.优化了爬取的照片数量
#       5.优化了部分流程

import requests
import re
import os
import time
from multiprocessing.dummy import Pool
from lxml import etree
all_img_numbers=0
#创建一个文件夹来保存图片
if not os.path.exists('./wallhaven壁纸'):
    os.mkdir('./wallhaven壁纸')
for i in range(3,5):
    urls = []  # 储存当前i 页面的所有壁纸 and 名称
    url = 'https://wallhaven.cc/hot?page=' + str(i)
    # headers = {'User-Agent':
	# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    #text（字符串）content(二进制）json（对象）
    #使用通用爬虫对url对应的页面进行全面爬取
    page_text = requests.get(url=url,headers=headers)
    print('sdada sdsad as dadsasd sadada -----------------')
    print(page_text.status_code)
    #print(page_text)
    #使用聚焦爬虫将页面中所有的壁纸进行解析/提取
    #ex ='<li><figure class=".*?".*?><img alt.*?"><a>class="preview" href="(.*?)target.*?"</a>.*?</figure></li>'
    ex = '<a class="preview" href="(.*?)"  target="_blank"  ></a>'
    img_src_list = re.findall(ex,page_text.text,re.S)
    print(page_text)
    for href in img_src_list:
        page_text2 = requests.get(url=href, headers=headers).text
        #print(page_text2)
        ax = '<div class="scrollbox"><img id="wallpaper" src="(.*?)" alt.*/></div>'
        #print(page_text2)
        try:
            img_src = re.findall(ax, page_text2)[0]
        except IndexError:
            break
        print(img_src)
        # print(page_text2)
        # 生成图片名称
        img_name = img_src.split('/')[-1]
        print(img_name)
        # 加一个判定，看是否之前下载完成了该图片
        folder_list = os.listdir('wallhaven壁纸')
        # print(folder_list)
        if img_name in folder_list:
            continue

        dic = {
            'name':img_name,
            'url':img_src
        }
        all_img_numbers += 1
        urls.append(dic)

    def get_img(dic):
        url = dic['url']
        img_name = dic['name']
        # 加一个判定，看是否之前下载完成了该图片
        folder_list = os.listdir('wallhaven壁纸')
        # print(folder_list)
        if img_name in folder_list:
            pass
        else:
            print(dic['name'],"正在下载.....")
            img_data=requests.get(url=url ,headers=headers).content
            #print(img_data)
             #图片最终储存的路径
            imPath = './wallhaven壁纸/'+img_name
            with open(imPath,"ab") as f:
                f.write(img_data)
                global img_numbers
                img_numbers += 1
                print(img_numbers,dic['name'],"下载成功！！！")


    img_numbers = 0
    pool = Pool(4)
    pool.map(get_img, urls)
    pool.close()
    pool.join()
    print('总计共下载{}张照片'.format(all_img_numbers))


