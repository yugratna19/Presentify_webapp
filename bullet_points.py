from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pyperclip
import time

# options = Options
# options.add_argument("--window-size=1,1")
driver = webdriver.Chrome()
driver.set_window_size(1920,1080)
driver.get('https://quillbot.com/summarize')
text = '''Transformer comprises encoder and decoder composed of stacked identical layers , each consisting of multi-head self-attention mechanism and position-wise fully connected feed-forward network with residual connections and layer normalization . Multi-head attention involves projecting queries , keys , and values linearly several times to different subspaces , performing attention in parallel on these projected versions , and concatenating and projecting results . Additionally , positional encodings are injected to incorporate sequence order information , using sine and cosine functions of different frequencies .'''
pyperclip.copy(text)
by_bullet_points_button = driver.find_element(By.XPATH, '//*[@id="root-client"]/div/div[3]/section[1]/div/div/div/section/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/button[2]')
by_bullet_points_button.click()
driver.find_element(By.ID, 'inputBoxSummarizer').send_keys(pyperclip.paste())
summarize_button = driver.find_element(By.XPATH, '//*[@id="root-client"]/div/div[3]/section[1]/div/div/div/section/div[2]/div/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div[2]/div/div/span/div/button')
summarize_button.click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
output = soup.find('div',id='outputBoxSummarizer').text.strip()
print(output)