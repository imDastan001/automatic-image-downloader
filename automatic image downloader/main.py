import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
chrome_driver_path="C:\development\chromedriver"
option=Options()
option.add_experimental_option('excludeSwitches',["enable-logging"])
serv = Service(chrome_driver_path)
headers={
   " User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
# cd d/dastan/Python\ class/python\ project/

def automate(name,i):
    driver=webdriver.Chrome(service=serv,options=option)
    driver.set_window_position(0, 0)
    driver.set_window_size(500, 500)
    driver.get(url=f"https://www.google.com/search?q={name}&tbm=isch&ved=2ahUKEwiTjefjvcz2AhVKzqACHQ0VDYIQ2-cCegQIABAA&oq=Avengers+Endgame+poster&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIHCAAQsQMQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEUMIZWMIZYPEcaABwAHgAgAGPAogBiwSSAQMyLTKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=Z9AyYtO9CMqcg8UPjaq0kAg&bih=713&biw=697&rlz=1C1CHBD_enIN964IN964")
    preview_xpath=f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img'
    image_xpath = '//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img'
    driver.find_element(By.XPATH,preview_xpath).click()
    time.sleep(1)
    preview_src = driver.find_element(By.XPATH, preview_xpath).get_attribute("src")
    src= driver.find_element(By.XPATH,image_xpath).get_attribute("src")
    count = 0
    while True:
        count+=1
        if preview_src==src:
            src=(driver.find_element(By.XPATH,image_xpath).get_attribute("src"))
            if count==200:
                driver.quit()
                print("[-] Can't download this low quality images")
                return src
        else:
            driver.quit()
            print('[-] Image download sucessfully')
            return src
        

while True:
    name = input("Enter the name of the image: ")
    size=int(input("Enter the number of image you want: "))
    for i in range (0,size):
        src=automate(name.replace(' ',"+").replace(":","+"),i+1)
        try:
            responsed=requests.get(url=src)
            if responsed.status_code==200:
                    new_name = name.replace(":","")
                    with open(os.path.join("images",f"{new_name}{i}.jpg"),mode="wb")as file:
                        file.write(responsed.content)
        except:
            continue 



