from pathlib import Path
from typing import List
import pymupdf
from src.ingestion.document import Document

class DocumentLoader:
    def __init__(self):
        pass

    def load_file(self, file_path):
        file_path = Path(file_path)
        if file_path.exists():
            print("file exists")
            extension = file_path.suffix.lower()
            if extension in ['.txt', '.md']:
                return self._load_text_file(file_path)
            elif extension == '.pdf':
                return self._load_pdf_file(file_path)
            else:
                raise FileNotFoundError(f"Unsupported file format : {file_path}")
            print(f"extension of the file is {extension}")
        else:
            raise FileNotFoundError(f"File not found {file_path}")
    def _load_text_file(self,file_path):
        with open(file_path, "r", encoding = "utf-8") as file:
            text = file.read()
            metadata = {"source": str(file_path),
                        "filename": file_path.name}
            document = Document(page_content= text, metadata=metadata)
            return [document]
    def _load_pdf_file(self,file_path):
        with pymupdf.open(file_path) as pdf
        documents = []
        pages = len(pdf)
        for page in range(pages):
            text = pdf[page].get_text()
            metadata = {"source" : str(file_path),
                                "filename": file_path.name,
                                "page" : page + 1,
                                "total_pages" : pages}
            document = Document(page_content=text, metadata=metadata)
            documents.append(document)
        pdf.close()
        return documents
        
        