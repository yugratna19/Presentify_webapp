import pdftitle
import pdfplumber
from bs4 import BeautifulSoup

from fastapi import FastAPI, UploadFile, HTTPException
from classobjects import PDF, PresentationData
from pdftools import *
from pptxtools import *
from gemini import gemini_summarize
from presentify_model import summarize
from image_extraction import image_extraction
from cosine_similarity import cosine_similarity
from create_presentation import create_presentation
from image_slides import display_slides

pdf = PDF()
presentation = PresentationData()

app = FastAPI()

MAX_FILE_SIZE = 1024 * 1024 * 12


@app.post('/extract-text')
async def extract_texts(file: UploadFile):
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File is too large")
    pdf_bytes = await file.read()

    # Optionally save the PDF temporarily
    with open('temp_pdf.pdf', 'wb') as f:
        f.write(pdf_bytes)
    pdf.textdata = clean_text(read_pdf('temp_pdf.pdf'))
    try:
        pdf_title = pdftitle.get_title_from_file('temp_pdf.pdf') #ya ho error aayeko
    except:
        pdf_title = 'title'
    try:
        author = pdfplumber.open('temp_pdf.pdf').metadata['Author']
    except:    
        author = 'author name'
        
    presentation.author = author
    presentation.title = pdf_title
    gemini_data = PresentationData()

    try:
        gemini_data = gemini_summarize(pdf.textdata)
        presentation.introduction = clean_text(gemini_data.introduction)
        presentation.literature_review = clean_text(gemini_data.literature_review)
        presentation.methodology = clean_text(gemini_data.methodology)
        presentation.results = clean_text(gemini_data.results)
        presentation.conclusions = clean_text(gemini_data.conclusions)
    except:
        return {'error': 'couldnt extract data'}
    data = PresentationData()
    data = summarize(gemini_data)
    data_dict = {'Introduction': data.introduction,
                 'Literature Review': data.literature_review,
                 'Methodology': data.methodology,
                 'Results': data.results,
                 'Conclusion': data.conclusions}
    image_caption_list = image_extraction(r'C:\Users\ACER\Desktop\Frontend\temp_pdf.pdf')
    if image_caption_list != []:
        similarity = cosine_similarity(data_dict, image_caption_list)
        filtered_similarity = [item for item in similarity if all(value > 0.25 for value in item.values())]
    else:
        filtered_similarity =[]
    create_presentation(data_dict, presentation.title,presentation.author, filtered_similarity)
    display_slides()
    flag = 1
    return {"message": "Slide created successfully!"}, flag


@app.post("/get_data_from_url")
async def get_data_fromI_url(arxiv_url: str):
    response = requests.get(arxiv_url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')

    presentation.title = soup.find('h1', class_='title mathjax').text
    presentation.author = soup.find('div', class_='authors').text
    pdf_link = arxiv_url.replace('abs', 'pdf')
    with open('temp_pdf.pdf', 'wb') as f:
        f.write(requests.get(pdf_link).content)
    pdf.textdata = clean_text(read_pdf_from_url(pdf_link))
    presentation.title = presentation.title.replace('Title:', '')
    presentation.author = presentation.author.replace('Authors:', '')
    gemini_data = PresentationData()

    try:
        gemini_data = gemini_summarize(pdf.textdata)
        presentation.introduction = clean_text(gemini_data.introduction)
        presentation.literature_review = clean_text(gemini_data.literature_review)
        presentation.methodology = clean_text(gemini_data.methodology)
        presentation.results = clean_text(gemini_data.results)
        presentation.conclusions = clean_text(gemini_data.conclusions)
    except:
        return {'error': 'couldnt extract data'}
    data = PresentationData()
    data = summarize(gemini_data)
    data_dict = {'Introduction': data.introduction,
                 'Literature Review': data.literature_review,
                 'Methodology': data.methodology,
                 'Results': data.results,
                 'Conclusion': data.conclusions}
    image_caption_list = image_extraction(r'C:\Users\ACER\Desktop\Frontend\temp_pdf.pdf')
    if image_caption_list != []:
        similarity = cosine_similarity(data_dict, image_caption_list)
        filtered_similarity = [item for item in similarity if all(value > 0.25 for value in item.values())]
    else:
        filtered_similarity =[]
    create_presentation(data_dict, presentation.title,presentation.author, filtered_similarity)
    display_slides()
    return {"message": "Slide created successfully!"}