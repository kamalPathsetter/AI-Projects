from langchain_huggingface import HuggingFaceEmbeddings
from config.config import HUGGINGFACE_MODEL_NAME
from common.logger import get_logger
from common.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)


def get_embedding_model():
    try:
        logger.info("Initializing embedding model...")
        
        model = HuggingFaceEmbeddings(model_name=HUGGINGFACE_MODEL_NAME)

        logger.info("Embedding model initialized successfully.")

        return model
    except Exception as e:
        raise CustomException(f"Failed to initialize embedding model: {str(e)}")