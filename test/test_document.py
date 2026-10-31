
from src.ingestion.document import Document


doc1 = Document(
    page_content="FastAPI is a Python web framework.",
    metadata={
        "source": "fastapi.pdf",
        "page": 5
    }
)

doc2 = Document(
    page_content="Python supports object-oriented programming."
)

print(doc1)
print(doc2)

# Access individual attributes
print(doc1.page_content)
print(doc1.metadata)

# Add new metadata
doc2.metadata["source"] = "python.txt"

print(doc2.metadata)
