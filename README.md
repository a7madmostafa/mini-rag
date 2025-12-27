# mini-rag
A minimalistic implementation of Retrieval-Augmented Generation (RAG) using LangChain and OpenAI.

## How to Use
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file (refer to `.env.example` for guidance).
4. Run the main application:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 5000
   ```