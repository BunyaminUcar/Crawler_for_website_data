from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome WebDriver'ı başlatma
chrome_options = Options()
chrome_options.add_argument("--headless")  # Arka planda çalıştırmak için
driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe", service_log_path="NUL")
driver.maximize_window()
# E-ticaret sitelerinin URL'lerini içeren bir liste oluşturma
etiket_siteleri = [
    "https://www.amazon.com",
    "https://www.ebay.com",
    "https://www.alibaba.com",
    "https://www.walmart.com",
    "https://www.etsy.com",
    "https://www.target.com",
    "https://www.bestbuy.com",
    "https://www.flipkart.com",
    "https://www.rakuten.com",
    "https://www.asos.com",
    "https://www.zalando.com",
    "https://www.macys.com",
    "https://www.newegg.com",
    "https://www.overstock.com",
    "https://www.aliexpress.com",
    "https://www.costco.com",
    "https://www.homedepot.com",
    "https://www.kohls.com",
    "https://www.jcpenney.com",
    "https://www.nordstrom.com",
    "https://www.sears.com",
    "https://www.wayfair.com",
    "https://www.ikea.com",
    "https://www.bedbathandbeyond.com",
    "https://www.urbanoutfitters.com",
    "https://www.hm.com",
    "https://www.footlocker.com",
    "https://www.sephora.com",
    "https://www.nike.com",
    "https://www.adidas.com",
    "https://www.uniqlo.com",
    "https://www.gap.com",
    "https://www.oldnavy.com",
    "https://www.bananarepublic.com",
    "https://www.bathandbodyworks.com",
    "https://www.cvs.com",
    "https://www.walgreens.com",
    "https://www.ulta.com",
    "https://www.officedepot.com",
    "https://www.staples.com",
    "https://www.gamestop.com",
    "https://store.playstation.com",
    "https://www.microsoft.com/en-us/store/b/xbox",
    "https://store.steampowered.com",
    "https://www.gog.com",
    "https://www.greenmangaming.com",
    "https://www.cdkeys.com",
    "https://www.fanatical.com",
]


# Ziyaret edilen linkleri tutmak için bir küme
ziyaret_edilen_linkler = set()


def alt_linkleri_dolaş(url):
    driver.get(url)

    # Ekran görüntüsü al
    driver.save_screenshot("screenshot.png")  # İstediğiniz yerde screenshot'ı kaydedin

    # Diğer sayfalara geçiş ve ekran görüntüsü alma
    links = driver.find_elements_by_tag_name("a")  # Tüm <a> etiketlerini bulma
    for link in links:
        alt_url = link.get_attribute("href")  # Linkin URL'sini al
        if alt_url and alt_url.startswith("http"):  # Geçerli bir URL ise
            if alt_url not in ziyaret_edilen_linkler:  # Daha önce ziyaret edilmemişse
                ziyaret_edilen_linkler.add(alt_url)  # Ziyaret edilen linklere ekle
                alt_linkleri_dolaş(alt_url)  # Alt linkleri dolaş


# Her bir e-ticaret sitesi için döngü
for site_url in etiket_siteleri:
    # Başlangıç linkini ekle
    ziyaret_edilen_linkler.add(site_url)

    # Alt linkleri dolaşma
    alt_linkleri_dolaş(site_url)

# Alt linkleri dolaşma işlevi


# WebDriver'ı kapatma
driver.quit()
