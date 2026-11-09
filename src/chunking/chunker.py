from src.ingestion.document import Document
from src.ingestion.loader import DocumentLoader

class TextChunker:
    def __init__(self,chunk_size, chunk_overlap):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        if self.chunk_size <= 0 or self.chunk_overlap <= 0:
            raise ValueError("Chunk size and chunk overlap should be more than 0")
        elif self.chunk_overlap > self.chunk_size:
            raise ValueError("Chunk size should be greater than chunk overlap")
    def chunk_text(self,documents): 
        n = len(documents)   
        chunks = []
        for i in range(0,n):
            text = documents[i].page_content
            start = 0
            n1 = len(documents[i].page_content)
            while start < n1:
                remaining = n1 - start
                if remaining <= self.chunk_overlap and start > 0:
                    break
                else:
                    text_chunk = text[start:start+self.chunk_size]
                    start = start + self.chunk_size - self.chunk_overlap
                    chunks.append(
                        Document(page_content = text_chunk,
                                metadata  = documents[i].metadata.copy())
                    )
        return chunks



             


        
            