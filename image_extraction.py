def image_extraction(path):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    import requests
    import time
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    pdf_path = path

    image_caption_list = []
    driver.get("https://www.eecis.udel.edu/~compbio/PDFigCapX")
    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(pdf_path)
    upload_button = driver.find_element(
        By.CLASS_NAME, "fileinput-upload-button")
    upload_button.click()
    time.sleep(3)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    for i in soup.find_all("div", class_="thumbnail clearfix"):
        image_data = i.find("img", class_="img-responsive")['src']
        caption = i.find("textarea").text.strip()
        if caption != '':
            content = {'image': image_data, 'caption': caption}
            image_caption_list.append(content)

    for n in range(len(image_caption_list)):
        img_data = requests.get(image_caption_list[n]['image']).content
        with open('images/'+str(n)+'.jpg', 'wb') as handler:
            handler.write(img_data)
    return image_caption_list
