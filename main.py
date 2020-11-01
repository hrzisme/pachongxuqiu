#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020-10-20
# @Author : Rasor_H
# @Version：V 0.1
# @File : main.py
# @desc :

from bs4 import BeautifulSoup
import requests
import lxml
import csv
import time
import base64
import json
import re
import random
import http.client
http.client._MAXLINE = 655360

def get_ip_list():
    """
    得到ip代理列表
    :return:
    """
    url = 'http://api.wandoudl.com/api/ip?app_key=e917dd9f384759cb5cf4dde0c05493dc&pack=216550&num=20&xy=1&type=2&lb=\r\n&mr=2&'
    resp = requests.get(url)
#     提取页面数据
    resp_json = resp.text
#     转变字典
    resp_dict = json.loads(resp_json)
#     取出data键
    ip_dict_list = resp_dict.get('data')

    return ip_dict_list

# 验证密码
def base_code(username, password):

    str = '%s:%s' % (username, password)
    encodestr = base64.b64encode(str.encode('utf-8'))
    return '%s' % encodestr.decode()




#解析网页搞soup
def getsoup(url):

    global ip_list
    global ip_port
    global waitingtime

    user_Agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)'
    ]
    username = '878822589@qq.com'
    password = 'HZT123hrz'
    authorization = 'Basic %s' % (base_code(username, password))
    header = {

        'Proxy-Authorization': authorization,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/'+str(random.randint(2,999))+' (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/'+str(random.randint(2,999)),

    }
    if ip_list == []:
        ip_list = getiplist()

    # ua = random.choice(user_Agent)
    # header ['User_Agent'] = ua

    # waitingtime = 1.5

        # cookies = {}
        # for line in cookie.split(';'):  # 浏览器伪装
        #     name, value = line.strip().split('=', 1)
        #     cookies[name] = value

    while True:
        ip_port = random.choice(ip_list)
        proxy = {
            'http': 'http://{}'.format(ip_port)
        }
        time.sleep(waitingtime)
        try:
            check_ip(ip_port)
            rsp = requests.get(url,headers = header, proxies =proxy,verify=False)

            html = rsp.text
            soup = BeautifulSoup(html,'lxml')
            return soup

        except Exception as e:
            print(e)
            ip_list.remove(ip_port)
            waitingtime += 0.1
            if len(ip_list) <= 10:
                ip_list = getiplist()
                waitingtime = 1.5
                print('补充ip，并重置')
            continue


def check_ip(ip_port):
    url = "http://myip.ipip.net/"

    username = '878822589@qq.com'
    password = 'HZT123hrz'

    authorization = 'Basic %s' % (base_code(username, password))
    header = {

        'Proxy-Authorization': authorization,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/' + str(
            random.randint(2, 999)) + ' (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',

    }
    proxy = {
        'http': 'http://{}'.format(ip_port)
    }
    r = requests.get(url, proxies=proxy, headers=header)
    print(r.text)

# 搞下一页的链接
def getnextpage(soup):
    nextpage = soup.find_all('div',attrs={'class':'pagerbar'})
    keyurl = ''
    count = 0
    for i in nextpage:
        keyurl = i.select('a')[-2].get('href')
        print(i.select('a')[-2].text+i.select('a')[-2].get('href'))
    return keyurl

# 爬当前筛选条件下所有详情的url,并保存到csv
def getdetailsurl(url,name):
    """
    爬当前筛选条件下所有详情的url,并保存到csv
    :param url:
    :rtype: null
    """
    global counter
    global ip_list
    global ip_port
    global waitingtime

    soup1 = getsoup(url)


    details_soup = soup1.find_all('div', attrs={'class': 'job-info'})
    url_list = []
    name_list = []

    for i in details_soup:
        url_list.append(i.select('a')[0].get('href').replace('/a','https://www.liepin.com/a'))
        name_list.append(i.select('a')[0].text.replace('\r', '').replace('\n', '').replace('\t', ''))
    print(name)

    path = name+'.csv'

    with open(path, "a", encoding='utf-8', newline="") as f:

        k = csv.writer(f, dialect="excel")
        with open(path, "r", encoding='utf-8', newline="") as f:
            reader = csv.reader(f)
            if not [row for row in reader]:
                k.writerow(["name", "url"])
                for i, j in zip(name_list, url_list):
                    k.writerow([i, j])
            else:
                for i, j in zip(name_list, url_list):
                    k.writerow([i, j])
        print('正在爬取第'+str(counter)+'页')
        counter  = counter + 1

    for i in url_list:
        try:
            paxiangqing(i, name)
        except:
            ip_list.remove(ip_port)
            waitingtime += 0.1
            if len(ip_list) <= 10:
                ip_list = getiplist()
                waitingtime = 1.5
                print('补充ip，并重置')
            paxiangqing(i, name)
            continue

    try:
        nexturl = getnextpage(soup1)
        newurl = 'https://www.liepin.com'+nexturl
        getdetailsurl(newurl,name)

    except Exception as e:
        print('爬取链接完毕或出错')


def paxiangqing(xiangqing_url, fname):
    try:
        soup2 = getsoup(xiangqing_url)
        # 职位名称
        name = soup2.select('.title-info')[0].select('h1')[0].text
        print(soup2.select('.title-info')[0].select('h1')[0].text)
        # 公司名称
        cpy = soup2.select('div[class="title-info"] h3 a')[0].text
        print(soup2.select('div[class="title-info"] h3 a')[0].text)


        xuqiu = soup2.select('div[class="content content-word"]')[0].text.strip()
        print(soup2.select('div[class="content content-word"]')[0].text.strip())

        path0 = fname + '详情信息' + '.csv'

        with open(path0, "a", encoding='utf-8', newline="") as f:

            k = csv.writer(f, dialect="excel")
            with open(path0, "r", encoding='utf-8', newline="") as f:
                reader = csv.reader(f)
                if not [row for row in reader]:
                     k.writerow(["jobname", "dqs_name", "job_req"])
                     k.writerow([name, cpy,xuqiu])
                else:
                     k.writerow([name, cpy,xuqiu])

    except Exception as e:
        print('失败，重连中'+e)
        print(soup2)
        paxiangqing(xiangqing_url, fname)



def getiplist():

    ip_dict_list = get_ip_list()
    ip_list = []
    path='ip.csv'
    for ip_dict in ip_dict_list:
        # 获取每次的ip代理和拼接
        ip_port = '{ip}:{port}'.format(ip = ip_dict.get('ip'),
                                       port = str(ip_dict.get('port')) )
        ip_list.append(ip_port)

        with open(path, "a", encoding='utf-8', newline="") as f:

            k = csv.writer(f, dialect="excel")
            with open(path, "r", encoding='utf-8', newline="") as f:
                reader = csv.reader(f)
                if not [row for row in reader]:
                    k.writerow(["ip"])
                    k.writerow([ip_port])
                else:
                    k.writerow([ip_port])

    return ip_list



counter = 1
beixuanname_list = ['图像算法工程师','数据挖掘','java后端','互联网产品经理']
beixuanurl_list = [
                   'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=c09e023578279b9b7ac8b7acdc4c89e9&d_ckId=c09e023578279b9b7ac8b7acdc4c89e9&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=LiAE77uh7ygbLjiB5afMYg%7EfA9rXquZc5IkJpXC-Ycixw&key=%E5%9B%BE%E5%83%8F%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88',
                    'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=86a85dffc430ab12da15c3abd19a281c&d_ckId=86a85dffc430ab12da15c3abd19a281c&d_sfrom=search_fp_nvbar&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EfA9rXquZc5IkJpXC-Ycixw&key=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98',
                   'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=3c96153f853907433796b96033ff35cf&d_ckId=3c96153f853907433796b96033ff35cf&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=sxHtUexZZBACO2d-7LKJ3g%7EfA9rXquZc5IkJpXC-Ycixw&key=java%E5%90%8E%E7%AB%AF',
                   'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=1faa1c53155d626f56dd2f493e8d2809&d_ckId=1faa1c53155d626f56dd2f493e8d2809&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=0xT8wOTfyfMLe3Y3h0Of5g%7EfA9rXquZc5IkJpXC-Ycixw&key=%E4%BA%92%E8%81%94%E7%BD%91%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86']
cookie = '__uuid=1601176616705.65; __s_bid=f6bc3d31fbccf6a93cc6cd4bb629ae2a736e; need_bind_tel=false; c_flag=b1da82a67c74984c3e24360af1d0f03c; gr_user_id=7b95461d-0bcd-4e9f-9a15-db1db512ecaa; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_cs1=b5ed1a8ad92150f41a667e00ad0d9493; grwng_uid=d310a28b-4ece-4ad8-867e-bcf878c7e1a2; new_user=false; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1601191803,1603457612,1603523997,1603590853; inited_user=3c819d6ea05ba87148b1f6ee46a2322e; user_roles=0; user_photo=5d5513d34ebeb1284dfc774e07u.png; user_name=%E9%BB%84%E6%B6%A6%E6%B3%BD; fe_se=-1603592041628; imApp_0=1; imClientId=f6c5bef7712427cdd2e48272083c9039; imId=f6c5bef7712427cdd891144c14c9cb2b; imClientId_0=f6c5bef7712427cdd2e48272083c9039; imId_0=f6c5bef7712427cdd891144c14c9cb2b; JSESSIONID=1A325F714354E36DCCA1F2B65AA24BFF; fe_im_socketSequence_0=11_11_11; __tlog=1603590853104.45%7C00000000%7CR000000075%7C00000000%7C00000000; UniqueKey=b5ed1a8ad92150f41a667e00ad0d9493; lt_auth=uL4POXMHzVX54HTcjGZf4q9Jhtn5V2rM%2FHsKhx9Wit%2FtXv3i4PblQwyHqrYExAMhkkt2dMULN7D9M%2BH9ynZM6UIRwGmnlIC1uuW71nkeTuxmHuyflMXuqs7QQJslrXg6ykpgn2si; access_system=C; __session_seq=84; __uv_seq=19; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id=622f3fcc-f1a3-4b74-80aa-9823bb3b5230; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_sid_with_cs1=622f3fcc-f1a3-4b74-80aa-9823bb3b5230; bad1b2d9162fab1f80dde1897f7a2972_gr_cs1=b5ed1a8ad92150f41a667e00ad0d9493; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1603693356; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id_622f3fcc-f1a3-4b74-80aa-9823bb3b5230=true'
ip_list = []
ip_port = ''
waitingtime = 1.5



for i, j in zip(beixuanname_list, beixuanurl_list):
    getdetailsurl(j, i)




#
# # 爬城市列表
# cities_soup = soup.find_all('dd',attrs={'data-param':'city'})
# # print(cities_soup)
# citiesurl_list = []
# citiesname_list = []
#
# for i in cities_soup:
#     citiesurl_list.append(i.select('a')[0].get('href'))
#     citiesname_list.append(i.select('a')[0].text)


# print(citiesurl_list)

# url1 = 'https://www.liepin.com'+citiesurl_list[0]
# getdetailsurl(url1)

'''2ceshi'''
# 默认职位列表
# occupation_soup = soup.find_all(attrs={'class':'sub-industry'})
#
# occupationurl_list = []
# occupationname_list = []
#
# for i in occupation_soup:
#     occupationurl_list.append(i.select('a')[0].get('href'))
#     occupationname_list.append(i.select('a')[0].text.replace('/','或'))
#
# print(occupationurl_list)
# print(occupationname_list)
#




'''123ceshi'''
# xiangqing_url = 'https://www.liepin.com/job/1932882159.shtml?imscid=R000000075&siTag=LiAE77uh7ygbLjiB5afMYg%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp_bar&d_ckId=3c10ae1f9409209a8edd59307cba2e55&d_curPage=0&d_pageSize=40&d_headId=3c10ae1f9409209a8edd59307cba2e55&d_posi=1'
# paxiangqing(xiangqing_url,'123')



