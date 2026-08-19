from pypdf import PdfReader

def read_pdf(file_path):

    try:
        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()
            pages.append(text)

        return pages

    except Exception as e:
        print("Something went wrong:", e)