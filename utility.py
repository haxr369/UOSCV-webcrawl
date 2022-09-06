import shutil
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import urllib.request
import urllib.parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
import json
from PIL import Image
import tarfile
import os

    
    
    
class make_dir():
    #원하는 디렉토리 만들기
    
    
    def __init__(self, directory): 
        try: 
            if not os.path.exists(directory): 
                os.makedirs(directory) 
        except OSError: 
            print ('Error: Creating directory. ' + directory)

class make_tarfile():
    def __init__(self, output_filename, source_dir):
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
            
            
def download_im(main_keyword, sub_keyword, img_numb,output_path="/home/dir_v"):
    
    keywords = sub_keyword #검색키워드 만들기
    
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')

    options.add_argument('--no-sandbox')

    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(executable_path="/home/dir_v/flaskapp/chromedriver",options=options)
    
    driver.implicitly_wait(3)
    


    print(sub_keyword, '검색') 
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl") # 구글 이미지 검색 url
    elem = driver.find_element_by_name("q") #구글 검색창 선택
    elem.send_keys(sub_keyword)
    elem = driver.find_element_by_name("q") 
    elem.send_keys(Keys.ENTER) #검색 엔터키 입력

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:

                driver.find_element_by_css_selector(".mye4qd").click() 
                driver.find_element_by_css_selector(".r0zKGf").click() 

            except:
                print("로딩중...")
                break
        last_height = new_height

    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rg_i.Q4LuWd")))
    
    path = os.path.join(output_path,"images",main_keyword)
    make_dir(path)
    print(path,"로 저장")
    
    main_long = len(os.listdir(path))
    print("메인 키워드의 길이는",main_long)
    count = 1
    for img in imgs:
        
        try:

            img.click()
            #img.send_keys(Keys.ENTER)
            time.sleep(3)
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute(
                "src")

            time.sleep(0.5)

            domain=imgUrl[:5]
            if domain == 'http:':
                imgUrl='https:'+imgUrl[5:] #continue 대신 http를 https로 바꾸어줬음

                
            ff= ".jpg"
            save_posi = os.path.join(path, main_keyword+'{0:04d}'.format(count+main_long)+ff)

            urllib.request.urlretrieve(imgUrl, save_posi)

            img = Image.open(save_posi)
            if img.format != "JPEG":
                now_for = img.format

                if now_for == "PNG":
                    ff = ".PNG"
                elif now_for == "GIF":
                    ff = ".GIF"
                elif now_for == "BMP":
                    ff = ".RLE"
                else:
                    ff = ".jpg"

                now_path = os.path.join(path, main_keyword+'{0:04d}'.format(count+main_long)+ff)
                os.rename(save_posi, now_path)

            print(main_keyword+'{0:04d}'.format(count+main_long)+ff+"를 저장했음")


            count = count + 1
            if count > img_numb:
                break
        except:
            print("문제 발생")
            pass
    driver.close()
    
    make_tarfile(path+".tar.gz", path)
    
    
            