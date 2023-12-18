import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys       #python yazdıktan sonra enter yapabilmek için ekledik
import requests


headers_param ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
glasdor=requests.get("https://www.linkedin.com/home" ,headers=headers_param)
print(glasdor.status_code)   #200 sonucu gelirse tüm verileri alabiliriz demektir.400 lü bir değer gelirse alamayız.bir user egent eklemeliyiz.

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com/home")  # Websitesine git.


login = driver.find_element("xpath","/html/body/nav/div/a[2]")
login.click()
time.sleep(2)


email = driver.find_element("xpath","/html/body/div/main/div[2]/div[1]/form/div[1]/input")            #username,password gibi alanları tek tırnak içinde yazmalıyız.
password = driver.find_element("xpath","/html/body/div/main/div[2]/div[1]/form/div[2]/input")

email.send_keys("******@*****.com")   #login işlemlerini yapıyoruz.
password.send_keys("******")


login_button = driver.find_element("xpath","/html/body/div/main/div[2]/div[1]/form/div[3]/button")
login_button.click()
time.sleep(6)

search_bar = driver.find_element("xpath","/html/body/div[5]/header/div/div/div/div[1]/input")
search_bar.send_keys("#python")        #arama motorundan python aratabiliyoruz.
search_bar.send_keys(Keys.RETURN)     #return enter tuşumuz gibi
time.sleep(4)

advertisement = driver.find_element("xpath","/html/body/div[5]/header/div/nav/ul/li[3]/a/span")
advertisement.click()
time.sleep(2)

for i in range(1,3): 
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

jobs = driver.find_elements("xpath","/html/body/div[5]/div[3]/div/div[3]/div/div/main/div")
jobsList=[]

for job in jobs:
     jobsList.append(job.text)
     print(job.text)  # Her bir iş ilanını yazdırarak kontrol edin
     print("----------------------")

     
     
with open ("job.txt","w",encoding="UTF-8") as file :  
     for job in jobsList:
          file.write(job+"/n")

time.sleep(5)

driver.quit()