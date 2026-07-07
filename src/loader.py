import fitz


class PDFLoader:

    def __init__(self, pdf_path):

        self.pdf_path = pdf_path

    def load(self):

        document = fitz.open(self.pdf_path)

        text = ""

        for page in document:

            text += page.get_text()

        document.close()

        return text