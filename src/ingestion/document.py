""" 
Document ingenstion loader for .md, .txt and .pdf files
"""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    """
    Represents a document and its metadata
    page_content is actual text extracted from the document
    metadata : additional information like from where the content is retrieved
    """
    page_content : str
    metadata : dict[str,Any] = field(default_factory=dict)
#combining the content and metadata into one object

