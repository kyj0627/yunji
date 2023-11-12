#입력 암호화
""" import getpass

pw = input("Pass :") #입력 문자가 안 보임 > 엔터치면 출력됨
#pw = getpass.getpass("Pass : ") # 입력 문자 보임
print(pw) """

#해시 함수
""" import hashlib

hl = hashlib.sha256()
target = "hello"
# target = "hi"
# target = "world"
# target = "to be or not to be, That is a question!"
# target = "python"
# target = "배고파"
# target = "1234567890" 
# target = "media program"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())
#print(hl.digest())
print("=======================================") """

#keccak256
""" import Crypto.Hash.keccak as kek

target = "to be or not to be, That is a question!"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest()) """

#입력키 변환
""" import getpass
import hashlib

pw = getpass.getpass("Pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest())
 """
 
#암호화 파일 저장
""" import hashlib
import os
 
def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass : ')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True

if pwInsert():
    pw = input('new pass : ')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password") """
    
#시스템 정보 확인
""" import platform as pf

print("uname==================")
pn = pf.uname()
print(pn)
print("machine==================")
pm = pf.machine()
print(pm)
print("processor==================")
pp = pf.processor()
print(pp)
print("system==================")
ps = pf.system()
print(ps)
print("==================") """

#웹 정보 읽기
""" import urllib.request as ur

#url = 'https://www.google.com'
url = 'https://daum.net'

#res = urllib.request.urlopen(url)
res = ur.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
print(web) """

#웹 정보 읽기2  <<<< url 확인
""" import http.client as hc

#url = 'https://www.google.com'
#url = "v.daum.net"

conn = hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulrp.html", "wb") as fp:
    fp.write(r.read())
    
conn.close()

print(r) """
            
#웹 정보 읽기3
""" import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web) """
    
#싱글스레드 / 각각 처리
""" import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()

for i in range(3) :
    counter(f"num{i}")
    
end = time.time()

#print("single end")
print("single end", end - start)
 """

#멀티스레드 / 동시에 동작 == 동시성 ㅇ
""" import threading as td
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

start = time.time()

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

end = time.time()

print("multi end", end- start) """

#병렬처리(멀티프로세싱) 
""" import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
 
if __name__ == "__main__":       
    process1 = mp.Process(target=counter, args=("1num",))
    process2 = mp.Process(target=counter, args=("2num",))
    process3 = mp.Process(target=counter, args=("3num",))

    start = time.time()

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

    end = time.time()

    print("process end", end- start)
 """
 
#main 실행
""" def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run() """
    
#===================1110수업===============================

#비동기 처리 1
""" import asyncio
import random as rd

async def tester(name):
    snum = rd.randint(10,20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
        
    print(f"end of {name}")
    
async def main():
    task_1 = asyncio.create_task(tester("1test"))
    task_2 = asyncio.create_task(tester("2test"))
    task_3 = asyncio.create_task(tester("3test"))
    
    print("start")
    await task_1
    await task_2
    await task_3
    print("end")


if __name__ == '__main__':
    asyncio.run(main()) """
    
# 비동기 처리 2
"""
import asyncio

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)

async def worker2():
    for i in range(1, 4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)

async def main():
    task1 = asyncio.create_task(worker1())
    task2 = asyncio.create_task(worker2())

    print("start task")
    await task1
    await task2
    print("end task")

if __name__ == '__main__':
    asyncio.run(main())
"""

#스케줄
##1
""" 
import sched
import time

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
        
    print(f"end of {name}")


s = sched.scheduler()
s.enter(5, 1, tester, ('1num',))
s.enter(3, 1, tester, ('2num',))
s.enter(7, 1, tester, ('3num',))
s.run()
# enter(지연시간, 우선순위, 실행함수, 전달인자)
 """
  
##2
""" 
import sched
import time

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
        
    print(f"end of {name}")

def run():
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(5, 1, tester, ('4num',))
    s.enter(3, 1, tester, ('2num',))
    s.enter(7, 1, tester, ('3num',))
    s.run()
    # enter(지연시간, 우선순위, 실행함수, 전달인자)

if __name__ == "__main__":
    run()
    print("end") """
    
#문자열 비교
""" import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, This is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d) """
    
#faker 임의 데이터
""" from faker import Faker as fk

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

print(temp.name() + "\n" + 
	temp.address() + "\n" + 
	temp.postcode() + "\n" + 
	temp.company() + "\n" + 
	temp.job() + "\n" + 
	temp.phone_number() + "\n" + 
	temp.email() + "\n" + 
	temp.user_name() + "\n" + 
	temp.ipv4_private() + "\n" + 
	temp.ipv4_public() + "\n" + 
	temp.catch_phrase() + "\n" + 
	temp.color_name()) """
 
# faker 파일 저장 - .cvs(엑셀)

""" from faker import Faker as fk

temp = fk("ko-KR")
print(temp.name())

#with open("fktemp.csv","w",newline='') as f:
with open("fktemp.txt","w",newline='') as f:
    for i in range(30):
        f.write(temp.name() + "," + 
        temp.address() + "," + 
        temp.postcode() + "," + 
        temp.company() + "," + 
        temp.job() + "," + 
        temp.phone_number() + "," + 
        temp.email() + "," + 
        temp.user_name() + "," + 
        temp.ipv4_private() + "," + 
        temp.ipv4_public() + "," + 
        temp.catch_phrase() + "," + 
        temp.color_name() + "\n") """
        
#시스템명령어 사용
""" import subprocess as sp

#res = sp.run(["cmd", "/c", "dir"], capture_output=True)
#res = sp.run(["cmd", "/c", "iconfig", "/all"], capture_output=True) / True, False 바꿔보기

print(res) """

#
""" import traceback as tb

def tester():
    return 1/0

def caller():
    tester()
    
def main():
    try:
        caller()
        
    # except ZeroDivisionError:
    #     print("zde error")

    except ValueError:
        print("ve error")
        
    except Exception as ex:
        print("ex error", ex)
        
    else:
        print("ok")
        
    finally:
        print("end") """
        
        
#웹크롤링

#import bs4.BeautifulSoup
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

#pres = res_html.find("h1")
pres = res_html.find("h2")
print(pres)
print("\n1-------------------------------\n")
print(pres.get_text().strip())
print("\n2-------------------------------\n")
print(pres.next_element.get_text().strip())
print("\n6-------------------------------\n")
print(pres.get_text())


tres = res_html.find("title")
print(tres)
print("\n3-------------------------------\n")
print(tres.next_element)
print("\n4-------------------------------\n")
print(tres.get_text().strip()) 

fares = res_html.findAll("a")
for i in fares:
    print(i.get_text())
    
#print(fares)
print("\n5-------------------------------\n")
clres = res_html.findAll(class_ = "doc-title")
print(clres)

print("\n6-------------------------------\n")
clrs = res_html.find(class_ = "head_top")
print(clrs)
print(clrs.get_text()) """

#셀렉터로 찾기
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("body > div.container-doc > main > section > div > div.content-article > div.box_g.box_news_issue > ul > li:nth-child(1) > div > div > strong > a")

print(item)
print(item.get_text()) """

#
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")
print(item)
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_text()) """

#select
from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news9.daum.net"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
print("\n----------------------------------\n")

for i in iss:
    issue = i.get_text()
    print(issue)

print("\n----------------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct:
    c = j.attrs["data-tiara-custom"]
    print(c+"\n")
