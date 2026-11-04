from pathlib import Path
from src.ingestion.loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_file(Path("data/raw/Machine Learning Principles.pdf"))

print(type(documents))
print("Total pages:", len(documents))
print(type(documents[0]))
print("First page metadata:", documents[0].metadata)
print("First page content:", documents[0].page_content[:500])