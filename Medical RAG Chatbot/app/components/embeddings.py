from langchain_huggingface import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def get_embedding_model():
    try:
        logger.info("Initializing HuggingFace embedding model")
        
        model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        logger.info("HuggingFace embedding model initialized successfully")

        return model

    except Exception as e:
        logger.error(f"Error initializing embedding model: {e}")
        raise CustomException("Error initializing embedding model")  