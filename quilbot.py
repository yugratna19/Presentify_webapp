def bullet_point(text):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    import pyperclip
    import time

    # options = Options()
    # options.add_argument("--headless")    
    
    driver = webdriver.Chrome()#options=options
    driver.get('https://quillbot.com/summarize')
    
    # Wait until the 'bullet points' button is clickable
    by_bullet_points_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root-client"]/div/div[3]/section[1]/div/div/div/section/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/button[2]'))
    )
    by_bullet_points_button.click()
    
    # Wait until the input box is visible and send text
    input_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'inputBoxSummarizer'))
    )
    pyperclip.copy(text)
    input_box.send_keys(pyperclip.paste())

    # Wait until the summarize button is clickable and click it
    time.sleep(10)
    summarize_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root-client"]/div/div[3]/section[1]/div/div/div/section/div[2]/div/div/div[2]/div[2]/div[3]/div[1]/div/div/div/div[2]/div/div/span/div/button'))
    )
    summarize_button.click()
    
    # Wait for the output to be generated
    time.sleep(10)
    
    # Read the output
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    output = soup.find('div', id='outputBoxSummarizer').text.strip()
    
    real_output = ''
    for char in output:
        if char != '•':
            real_output += char
    
    print("Output:", output)  # Debugging statement
    print("Real Output:", real_output)  # Debugging statement
    
    driver.quit()  # Close the browser
    
    return real_output