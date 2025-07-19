from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY, GROQ_MODEL_NAME
from common.logger import get_logger
from common.custom_exception import CustomException

logger = get_logger(__name__)


def load_llm():
    try:
        logger.info("Initializing LLM...")
        
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name=GROQ_MODEL_NAME,
            temperature=0.3
        )

        logger.info("LLM initialized successfully.")

        return llm
    
    except Exception as e:
        raise CustomException(f"Failed to initialize LLM: {str(e)}")