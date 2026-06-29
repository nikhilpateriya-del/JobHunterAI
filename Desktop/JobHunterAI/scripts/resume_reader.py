import fitz  # PyMuPDF

def read_resume():
    pdf_path = "resume/Nikhil CV v1.pdf"

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    print("=" * 50)
    print("RESUME TEXT")
    print("=" * 50)

    print(text[:1000])   # Sirf pehle 1000 characters dikhayega