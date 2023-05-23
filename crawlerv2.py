import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re


def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    base_url = urlparse(url).scheme + "://" + urlparse(url).netloc
    links = []
    for anchor in soup.find_all("a"):
        href = anchor.get("href")
        if href and href.startswith(("http://", "https://")):
            links.append(href)
        else:
            links.append(urljoin(base_url, href))
    return links


def take_screenshot(url):
    options = Options()
    options.headless = True  # Arka planda çalışacak şekilde ayarlanmıştır. Eğer pencerede görüntü almak isterseniz `False` olarak değiştirin.
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe", options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)

    # URL'deki geçersiz karakterleri kaldırarak dosya adını oluştur
    file_name = re.sub(r"\W+", "", url) + ".png"
    driver.save_screenshot(file_name)
    driver.quit()


def crawl(url):
    visited_urls = set()
    queue = [url]

    while queue:
        current_url = queue.pop(0)
        if current_url in visited_urls:
            continue
        visited_urls.add(current_url)

        print("Crawling:", current_url)

        links = get_all_links(current_url)
        for link in links:
            queue.append(link)

        take_screenshot(current_url)


# Ana başlangıç noktası
starting_url = (
    "https://www.ebay.com"  # Tarayıcıya başlayacağımız URL'yi burada belirtin
)
crawl(starting_url)
