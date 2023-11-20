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
