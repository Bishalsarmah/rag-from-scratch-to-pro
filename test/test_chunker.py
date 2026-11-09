from src.ingestion.document import Document
from src.chunking.chunker import TextChunker

# doc1 = Document(
#     page_content="ABCDEFGHIJKLMNO",
#     metadata={"source": "a.pdf", "page": 1}
# )

# doc2 = Document(
#     page_content="1234567890",
#     metadata={"source": "b.pdf", "page": 2}
# )

documents = [
    Document("ABCDEFGHIJKLMNO", {"source": "a.pdf", "page": 1}),
    Document("AB", {"source": "b.pdf", "page": 2})
]
# documents = [doc1, doc2]

chunker = TextChunker(chunk_size=6, chunk_overlap=2)

chunks = chunker.chunk_text(documents)

for chunk in chunks:
    print(chunk.page_content, chunk.metadata)