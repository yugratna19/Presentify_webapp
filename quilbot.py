# def bullet_point(text):
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.chrome.options import Options
#     from selenium.webdriver.support import expected_conditions as EC
#     from bs4 import BeautifulSoup
#     import pyperclip
#     import time

#     # options = Options()
#     # options.add_argument("--headless")    
    
#     driver = webdriver.Chrome()#options=options
#     driver.get('https://quillbot.com/summarize')
    
#     # Wait until the 'bullet points' button is clickable
#     by_bullet_points_button = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="root-client"]/div/div[3]/section[1]/div/div/div/section/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/button[2]'))
#     )
#     by_bullet_points_button.click()
    
#     # Wait until the input box is visible and send text
#     input_box = WebDriverWait(driver, 30).until(
#         EC.visibility_of_element_located((By.ID, 'inputBoxSummarizer'))
#     )
#     pyperclip.copy(text)
#     input_box.send_keys(pyperclip.paste())

#     # Wait until the summarize button is clickable and click it
#     time.sleep(10)
#     summarize_button = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="root-client"]/div/div[3]/section[1]/div/div/div/section/div[2]/div/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div[2]/div/div/span/div/button'))
#     )
#     summarize_button.click()
    
#     # Wait for the output to be generated
#     time.sleep(10)
    
#     # Read the output
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     output = soup.find('div', id='outputBoxSummarizer').text.strip()
    
#     real_output = ''
#     for char in output:
#         if char != '•':
#             real_output += char
    
#     print("Output:", output)  # Debugging statement
#     print("Real Output:", real_output)  # Debugging statement
    
#     driver.quit()  # Close the browser
    
#     return real_output


def bullet_point(text):
  from openai import OpenAI
  import os
  client = OpenAI(
      api_key=os.getenv("OPENAI_API_KEY"),
  )
  # text = '''Transformer comprises encoder and decoder composed of stacked identical layers , each consisting of multi-head self-attention mechanism and position-wise fully connected feed-forward network with residual connections and layer normalization . Multi-head attention involves projecting queries , keys , and values linearly several times to different subspaces , performing attention in parallel on these projected versions , and concatenating and projecting results . Additionally , positional encodings are injected to incorporate sequence order information , using sine and cosine functions of different frequencies .'''
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an expert paragraph to bullet point converter"},
      {"role": "user", "content": f"Convert {text} into bullet points. Limit the bullet points to 5 or less points."},
    ]
  )
  output =  completion.choices[0].message.content
  real_output = ''
  for char in output:
      if char != '-':
          real_output += char
    
  print(output) 
    
  return real_output