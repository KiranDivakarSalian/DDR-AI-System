import streamlit as st
import fitz
import pdfplumber
import pytesseract
from PIL import Image

# ------------------ CONFIG ------------------
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# ------------------ FUNCTION ------------------

def extract_text_from_pdf(file):
    text = ""

    # Open PDF
    pdf = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf:
        # Convert page to image
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # OCR
        ocr_text = pytesseract.image_to_string(img)

        text += ocr_text + "\n"

    return text

def generate_summary(inspection_text, thermal_text):

    inspection_summary = inspection_text[:1000] if inspection_text else "No inspection data"
    thermal_summary = thermal_text[:1000] if thermal_text else "No thermal data"

    report = f"""
================= DDR REPORT =================

📌 INSPECTION SUMMARY:
{inspection_summary}

📌 THERMAL SUMMARY:
{thermal_summary}

📌 OBSERVATIONS:
- Structural conditions derived from inspection report
- Thermal patterns analyzed using OCR extraction
- Possible anomalies should be manually verified

📌 RECOMMENDATIONS:
- Conduct detailed inspection if defects found
- Re-scan thermal areas if unclear
- Schedule maintenance for affected zones

📌 CONCLUSION:
System-generated report using text extraction + OCR (no external AI).

================================================
"""

    return report


# ------------------ UI ------------------

st.title("🏗️ DDR Report Generator (OCR Enabled)")

inspection_file = st.file_uploader("Upload Inspection PDF", type=["pdf"])
thermal_file = st.file_uploader("Upload Thermal PDF", type=["pdf"])

inspection_text = ""
thermal_text = ""

if inspection_file:
    inspection_text = extract_text_from_pdf(inspection_file)

if thermal_file:
    thermal_text = extract_text_from_pdf(thermal_file)


# ------------------ BUTTON ------------------

if st.button("🚀 Generate DDR Report"):

    if not inspection_text and not thermal_text:
        st.warning("Please upload at least one file")
    else:
        report = generate_summary(inspection_text, thermal_text)
        st.text_area("📊 Final DDR Report", report, height=500)