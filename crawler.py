from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome WebDriver'ı başlatma
chrome_options = Options()
chrome_options.add_argument("--headless")  # Arka planda çalıştırmak için
driver = webdriver.Chrome(
    "C:\chromewebdriver\chromedriver.exe", service_log_path="NUL")
driver.maximize_window()
# E-ticaret sitelerinin URL'lerini içeren bir liste oluşturma
etiket_siteleri = [



    "https://www.boyner.com.tr",


    "https://www.gordion.com",
    "https://www.trendyol.com.tr",
    "https://www.sanalmarket.com.tr",
    "https://www.carrefoursa.com",
    "https://www.penti.com",
    "https://www.gratis.com.tr",
    "https://www.koton.com.tr",
    "https://www.defacto.com.tr",
    "https://www.herry.com.tr",
    "https://www.yvesrocher.com.tr",
    "https://www.rossmann.com.tr",
    "https://www.mediamarkt.com.tr",
    "https://www.tekzen.com.tr",
    "https://www.decathlon.com.tr",
    "https://www.morhipo.com.tr",
    "https://www.lcwaikiki.com.tr",
    "https://www.mavi.com",
    "https://www.koctas.com.tr",
    "https://www.defacto.com",
    "https://www.boyner.com.tr",
    "https://www.yemeksepeti.com.tr",
    "https://www.sahibinden.com",
    "https://www.arcelik.com.tr",
    "https://www.istikbal.com.tr"
]


# Her bir e-ticaret sitesini ziyaret ederek screenshot alın
for site_url in etiket_siteleri:
    driver.get(site_url)  # E-ticaret sitesini açma

    # Sayfanın tam ekran görüntüsünü alın
    screenshot_adı = site_url.replace(
        "https://", "").replace(".", "_") + ".png"
    driver.save_screenshot(screenshot_adı)
    print(f"{site_url} için screenshot alındı: {screenshot_adı}")

# WebDriver'ı kapatma
driver.quit()
