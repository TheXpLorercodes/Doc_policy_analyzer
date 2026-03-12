# Doc_policy_analyzer

📚 RAG Knowledge Assistant using Vector Database

A Retrieval Augmented Generation (RAG) system that allows users to query documents and receive accurate answers by combining vector search with LLM reasoning.

Instead of relying only on a language model, this system retrieves relevant context from documents stored in a vector database and sends it to the LLM to generate grounded responses.

This project demonstrates how to build a document-based AI assistant using embeddings, semantic search, and generative AI.

🚀 Features

📄 Upload and process PDF / documents

🔎 Semantic search using vector embeddings

🧠 LLM-powered answers grounded in document data

📊 Metadata filtering for better retrieval

⚡ Fast similarity search using a vector database

💬 Question-answering over custom knowledge base

🧠 System Architecture
User Query
    │
    ▼
Query Embedding
    │
    ▼
Vector Database Search
    │
    ▼
Retrieve Top-K Relevant Chunks
    │
    ▼
Combine Context + User Query
    │
    ▼
Large Language Model
    │
    ▼
Generated Answer
🔄 Full RAG Pipeline Diagram
                ┌──────────────────────┐
                │     Source PDFs      │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Document Loader      │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Text Chunking        │
                │ (Split Documents)    │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Generate Embeddings  │
                │ (Embedding Model)    │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Vector Database      │
                │ (Store Embeddings)   │
                └─────────┬────────────┘
                          │
                          │
        User Query        │
             │            │
             ▼            │
      ┌──────────────────────┐
      │ Query Embedding      │
      └─────────┬────────────┘
                │
                ▼
      ┌──────────────────────┐
      │ Similarity Search    │
      │ Retrieve Top-K Docs  │
      └─────────┬────────────┘
                │
                ▼
      ┌──────────────────────┐
      │ Context + Query      │
      │ Prompt Construction  │
      └─────────┬────────────┘
                │
                ▼
      ┌──────────────────────┐
      │ Large Language Model │
      │ (Gemini / OpenAI)    │
      └─────────┬────────────┘
                │
                ▼
         Final AI Answer
🛠️ Tech Stack
Component	Technology
Programming Language	Python
LLM	Gemini / OpenAI
Framework	LangChain
Vector Database	FAISS / Pinecone / Chroma
Embedding Model	Gemini Embeddings / OpenAI Embeddings
Document Loader	PyPDF
UI (optional)	Streamlit
📂 Project Structure
rag-vector-assistant
│
├── data
│

