import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;96m' # 

H = '\033[1;94m' # 

K = '\x1b[1;93m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

        

def main_apv():

    imt="110Y=="

    ak="AKASH_0BDT"

    os.system('clear')

    print(logo)

  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$
 /$$__  $$| $$  /$$/ /$$__  $$ /$$__  $$| $$  | $$
| $$  \ $$| $$ /$$/ | $$  \ $$| $$  \__/| $$  | $$
| $$$$$$$$| $$$$$/  | $$$$$$$$|  $$$$$$ | $$$$$$$$
| $$__  $$| $$  $$  | $$__  $$ \____  $$| $$__  $$
| $$  | $$| $$\  $$ | $$  | $$ /$$  \ $$| $$  | $$
| $$  | $$| $$ \  $$| $$  | $$|  $$$$$$/| $$  | $$
|__/  |__/|__/  \__/|__/  |__/ \______/ |__/  |__/
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()

    except IOError:

        os.system("clear")

        print(logo)

        print ("༄Akash᭄•───────────────────────────────────────•༄𝑘st᭄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄Akash᭄•───────────────────────────────────────•༄𝑘st᭄")

        print ("")

        myid=uuid.uuid4().hex[:10].upper()

        print ("          YOUR KEY : "+ak+myid+imt)

        print ("༄Akash᭄•───────────────────────────────────────•༄𝑘st᭄")

        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')

        kok.write(myid+imt)

        kok.close()

        print ("")

        print ("")

        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")

        print ("༄Akash᭄•───────────────────────────────────────•༄𝑘st᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+92188049915?text=' + tks)

        

    r1=requests.get("https://raw.githubusercontent.com/Red-Mafia/fiile/main/Sm.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄Akash᭄•───────────────────────────────────────•༄𝑘st᭄")
        print ("             \033[1;94mGIVE ME 0 BDT FOR APROVAL AKASH")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄Akash᭄•────────────
