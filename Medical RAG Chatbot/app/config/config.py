import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HUGGINGFACE_REPO_ID="MiniMaxAI/MiniMax-M1-80k"
DB_FAISS_PATH = "vectorstore/db_faiss"
DATA_PATH = "data/"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
GROQ_API_KEY = os.getenv("GROQ_API_KEY")