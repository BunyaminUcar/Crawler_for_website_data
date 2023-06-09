import time
from pynput import keyboard
from selenium import webdriver
from pynput.keyboard import Listener

# Chrome web tarayıcısı için sürücüyü başlatma
driver = webdriver.Chrome()
driver.get("https://www.google.com.tr")
# Chrome'u tam ekran yapma
driver.maximize_window()

# Web sayfasını açma
# Kullanmak istediğiniz web sitesinin URL'sini buraya girin
driver.get("C:\chromewebdriver\chromedriver.exe")

# Ekran görüntüsü alma fonksiyonu


def take_screenshot():
    # Ekran görüntüsüne tarih ve saat eklemek için zaman damgası oluşturma
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # Ekran görüntüsü dosyasının adı ve formatı
    screenshot_file = f"screenshot_{timestamp}.png"

    # Yan sekmedeki sayfaya geçmek için
    default_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != default_handle:
            driver.switch_to.window(handle)
            break

    # Yan sekmeden ekran görüntüsü almak için geçerli sekmeye odaklanın
    driver.switch_to.window(driver.current_window_handle)
    driver.save_screenshot(screenshot_file)

    print(f"Ekran görüntüsü kaydedildi: {screenshot_file}")

# Klavye tuşu dinleyicisi


def on_press(key):
    if hasattr(key, 'char') and key.char == 'f':
        take_screenshot()
    elif key == keyboard.Key.esc:
        # Listener'ı durdur
        return False


# Klavye tuşlarını dinleme
with Listener(on_press=on_press) as listener:
    listener.join()
