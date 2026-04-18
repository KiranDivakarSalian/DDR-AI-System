import pdfplumber
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

# 👉 IMPORTANT: Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        # 🔹 Step 1: Try normal text extraction
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

        # 🔹 Step 2: If no text → use OCR
        if text.strip() == "":
            print("⚠️ No text found, using OCR...")

            images = convert_from_path(pdf_path)

            for img in images:
                text += pytesseract.image_to_string(img)

        return text

    except Exception as e:
        return f"Error: {str(e)}"


# 👉 TEST FILE PATH (change if needed)
pdf_file = r"C:\Users\dilan\OneDrive\Desktop\Main DDR.pdf"

result = extract_text_from_pdf(pdf_file)

print("\n===== EXTRACTED TEXT =====\n")
print(result[:1000])  # print first 1000 characters