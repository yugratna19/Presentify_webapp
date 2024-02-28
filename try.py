import fitz

def read_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path, filetype="pdf")
    text = ''
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text

path = r"C:\Users\ACER\Desktop\pdfs for presentify\Analytical Model and Experimental Testing of the SoftFoot an Adaptive Robot Foot for Walking over Obstacles and Irregular Terrains.pdf"
hello = read_pdf(path)
print(hello)