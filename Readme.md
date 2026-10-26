# RAG from Scratch to Pro: Zero-Abstraction Architecture & Evaluation

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A first-principles engineering implementation of a **Retrieval-Augmented Generation (RAG)** pipeline. This project starts from a bare-metal, pure-Python baseline and systematically scales to a production-grade, hybrid-search, reranked, and empirically evaluated system.

---

## 🎯 Architecture Philosophy

Most RAG tutorials rely on black-box wrappers (`RetrievalQA`, `VectorStoreIndex`) that mask fundamental retrieval failures. In this repository:
1. **Zero Framework Magic Early On:** Chunking algorithms, vector indexing, cosine similarity, and prompt serialization are built from scratch using `numpy` and core Python.
2. **Tradeoff-Driven Design:** Every architectural decision (e.g., chunk window size, overlap ratios, dense vs. sparse indexing, cross-encoder reranking) is justified by concrete latency, cost, and retrieval recall trade-offs.
3. **Rigorous LLM Evaluation:** We treat RAG as an information retrieval and verification problem. Every phase is quantitatively benchmarked against synthetic and curated test sets using exact metrics (Hit Rate@K, MRR, Context Precision, Faithfulness).

---

## 🗺️ Progressive Roadmap

Phase 1: Naive Baseline (From Scratch) [CURRENT]
├── Document Ingestion: Raw .txt, .md, and .pdf via PyMuPDF
├── Chunking Engine: Sliding-window token/character splitting with overlap
├── Dense Embeddings: Local bi-encoder (sentence-transformers/all-MiniLM-L6-v2)
├── Vector Store: In-memory matrix operations with pure NumPy cosine similarity
└── Prompt Assembler & Generator: Grounded zero-shot context injection
│
▼
Phase 2: Pre-Retrieval Optimization
├── Structural & Hierarchical Chunking (Parent-Child / Small-to-Big)
├── Metadata Extraction & Structural Header Tagging
└── Query Transformations (HyDE - Hypothetical Document Embeddings, Multi-Query)
│
▼
Phase 3: Hybrid Retrieval & Cross-Encoder Reranking
├── Sparse Lexical Search (BM25 from scratch)
├── Hybrid Fusion via Reciprocal Rank Fusion (RRF)
└── Deep Reranking via Cross-Encoder (e.g., bge-reranker-base)
│
▼
Phase 4: Synthesis Hardening & Hallucination Mitigation
├── Lost-in-the-Middle Attention Mitigation
├── Structured Citation Extraction
└── Rejection Fallbacks (Refusal when context confidence is below threshold)
│
▼
Phase 5: End-to-End LLM Evaluation Pipeline
├── Retrieval Benchmarks: Hit Rate@K, MRR, NDCG@K
└── Generation Benchmarks: Faithfulness, Answer Relevance, Context Recall


---

## 📂 Repository Layout

```text
.
├── data/
│   ├── sample_docs/         # Raw source PDFs, markdown files, technical docs
│   └── ground_truth/        # Evaluation test sets (queries + ground truth chunks)
├── src/
│   ├── ingestion/           # Document loader interfaces (TXT, MD, PDF)
│   ├── chunking/            # Sliding-window, recursive, and semantic splitters
│   ├── embeddings/          # Embedding model wrappers
│   ├── vector_store/        # In-memory NumPy vector index
│   ├── retrieval/           # Dense top-K, BM25, and hybrid fusion
│   ├── reranking/           # Cross-encoder scoring modules
│   ├── generation/          # Context injection, citation parsing, LLM clients
│   └── evaluation/          # Retrieval & generation benchmark scripts
├── tests/                   # Unit and integration test suites
├── requirements.txt         # Project dependencies
└── README.md