import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовые данные
base_url = "http://www.saucedemo.com/"
valid_username = "performance_glitch_user"
valid_password = "secret_sauce"

# Переход на страницу авторизации  и разворачивание окна на весь экран
driver.get(base_url)
driver.maximize_window()

# Ввод логина
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(valid_username)
print("Input login")

# Ввод пароля
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_password)
print("Input password")

# Клик по кнопке "Login"
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click login button")

# Добавление товаров в корзину
time.sleep(5)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
print("Sauce Labs Backpack added in cart")

time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
print("Sauce Labs Bike Light added in cart")

time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
print("Sauce Labs Bolt T-shirt added in cart")

time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
print("Sauce Labs Fleece Jacket added in cart")

time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
print("Sauce Labs Onesie added in cart")

time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
print("Test.allthethings() T-shirt (Red) added in cart")

# Переход в корзину
time.sleep(1)
driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
print("Click to cart button")

# Проскролить коризну до последнего элемента в корзине
time.sleep(1)
actions = ActionChains(driver)
element = driver.find_element(By.ID, "item_3_title_link")
actions.move_to_element(element).perform()
print("Last item in the cart is selected")

# Выход из браузера
driver.quit()
print("Browser is closed")