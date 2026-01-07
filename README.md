# Clinic FAQ RAG System

## How to Run

1. Create virtual environment (optional)
2. Install dependencies:
   pip install -r requirements.txt

3. Set OpenAI API Key:
   export OPENAI_API_KEY=your_key_here

4. Ingest data:
   python app/rag/ingest.py

5. Run server:
   uvicorn app.main:app --reload
