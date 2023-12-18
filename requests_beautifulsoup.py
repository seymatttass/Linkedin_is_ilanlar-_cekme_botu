import requests
from bs4 import BeautifulSoup

headers_param ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
glasdor=requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm" ,headers=headers_param)
print(glasdor.status_code)   #200 sonucu gelirse tüm verileri alabiliriz demektir.400 lü bir değer gelirse alamayız.bir user egent eklemeliyiz.

#        print(glasdor.content)   ---->    #content kısmı sayfanın kaynak kod kısmını alır.

jobs= glasdor.content

soup = BeautifulSoup(jobs,"html.parser")    #beautifulsoup içerisindeki veriyi yani jobsu pars ederiz parçalarız yani çözümleriz.

print(soup.title)      #sitenin başlığını aldık.

print(soup.find,"h1")       #h1 etiketi içerisindekileri  getir demektir.sonuna(.text()) ekleyerek de sadece metinleri alabiliriz.

print(soup.find_all,"h1")        #all gelince sayfadaki tüm h1 etiketlerini getir demektir.


all_jobs = (soup.find_all,"p" ,{"class" :"h2 m-0 entry-Winner pb-std pb-md-0"})  

  #p etiketinin altındaki bu class.for ile de bu classın da içindeli a etil-ketlerine ulaşırız.

for job in all_jobs:
   print(job.a).text()