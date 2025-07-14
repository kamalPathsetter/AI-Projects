from langchain.llms import HuggingFaceHub
from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN

from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

def load_llm(huggingface_repo_id: str = HUGGINGFACE_REPO_ID, hf_token: str = HF_TOKEN):
    try:
        logger.info("Loading LLM from HuggingFace")

        llm = HuggingFaceHub(
            repo_id = huggingface_repo_id,
            model_kwargs = {
                "temperature" : 0.3,
                "max_length" : 256,
                "return_full_text": False
            },
            huggingfacehub_api_token = hf_token
        )

        logger.info("LLM loaded successfully")

        return llm
    
    except Exception as e:
        logger.error(f"Error loading LLM: {e}")
        raise CustomException("Error loading LLM")