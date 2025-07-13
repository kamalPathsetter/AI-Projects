import os
from langchain_community.vectorstores import FAISS

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.components.embeddings import get_embedding_model
from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)


def load_vector_store():
    try:
        embedding_model = get_embedding_model()

        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading vector store from existing database")
            return FAISS.load_local(
                DB_FAISS_PATH,
                embedding_model,
                allow_dangerous_deserialization=True
            )
        else:
            logger.warning("Vector store not found")
            return None

    except Exception as e:
        logger.error(f"Error loading vector store: {e}")
        raise CustomException("Error loading vector store")


def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("Text chunks are empty")
        
        logger.info("Generating your new vector store")
        
        embedding_model = get_embedding_model()
        
        vector_store = FAISS.from_documents(text_chunks, embedding_model)
        
        vector_store.save_local(DB_FAISS_PATH)
        
        logger.info("Vector store saved successfully")

        return vector_store
        
    except Exception as e:
        logger.error(f"Error saving vector store: {e}")
        raise CustomException("Error saving vector store")