from langchain_community.vectorstores import FAISS
from common.logger import get_logger
from common.custom_exception import CustomException
from config.config import DB_FAISS_PATH
from components.embeddings import get_embedding_model
import os
import os

logger = get_logger(__name__)

def load_vector_store():
    try:
        logger.info("Loading vector store...")
        
        embedding_model = get_embedding_model()
        
        if os.path.exists(DB_FAISS_PATH):
            return FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
        else:
            logger.info("Vector store not found.")

    except Exception as e:
        raise CustomException(f"Failed to load vector store: {str(e)}")
        
        
def save_vector_store(text_chunks):
    try:
        logger.info("Saving vector store...")
        
        vector_store = FAISS.from_documents(text_chunks, get_embedding_model())
        
        vector_store.save_local(DB_FAISS_PATH)
        
        logger.info("Vector store saved successfully.")

        return vector_store
        
    except Exception as e:
        raise CustomException(f"Failed to save vector store: {str(e)}")