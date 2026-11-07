from src.ingestion.document import Document
from src.chunking.chunker import TextChunker

documents = [
    Document(
        page_content="ABCDEFGHIJKLMNO",
        metadata={"source": "guide.pdf", "page": 1}
    )
]

chunker = TextChunker(chunk_size=6, chunk_overlap=2)

result = chunker.chunk_text(documents)

for doc in result:
    print(doc.page_content, doc.metadata)