import chromedriver_binary
from selenium import webdriver
import time 

sleep_time = 2
test_text = ["あいうえお","12345","abcde"," ","????"]

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get('localhost:5000')
print(driver.current_url)
time.sleep(sleep_time)

for i in test_text:
	# 要素を指定する
	element = driver.find_element_by_id('text')
	# テキストを入力する
	element.send_keys(i)
	time.sleep(sleep_time)

	# ボタンをクリックする
	element = driver.find_element_by_id("button")
	element.click()
	time.sleep(sleep_time)

	element = driver.find_element_by_id("button")
	element.click()
	time.sleep(sleep_time)
print("END")
# ブラウザを終了する
driver.quit()