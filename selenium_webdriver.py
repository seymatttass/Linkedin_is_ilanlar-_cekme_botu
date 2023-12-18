import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




# İstisnaları yönetmek için try-except bloğu kullan
try:
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
  
    driver.get("https://www.forbes.com/the-worlds-most-valuable-brands/#340b1b42119c") # Websitesine git.

    print(driver.page_source) # Sayfa kaynağı

    print(driver.title) # Başlık

    driver.fullscreen_window()  # Tam ekranı kaydet.
    time.sleep(2)
    driver.set_window_size(600, 400) # Sayfa boyutu
    time.sleep(3)
    driver.refresh() # Sayfayı yenile
    time.sleep(4)
    driver.save_screenshot("C:\\Users\\MSI\\OneDrive\\Masaüstü\\image.png")  # Ekran görüntüsü al ve kaydet.

    driver.get("https://www.forbes.com/the-worlds-most-valuable-brands/#340b1b42119c")
    time.sleep(3)
    driver.back()    # Önceki URL'e geri dön.
    time.sleep(3)

    # browser.close() # Açık sekmeleri kapat.
    driver.quit()   # Tarayıcıyı kapat.

except Exception as e:
    print("Bir hata oluştu:", e)
