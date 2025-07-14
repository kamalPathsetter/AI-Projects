from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vector_store import load_vector_store

from app.config.config import GROQ_API_KEY
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """
You are a medical assistant AI. Answer the following medical question using the provided context and chat history.

Context: {context}

Chat History:
{chat_history}

Current Question: {question}

Answer: 

"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question", "chat_history"])


def create_chain():
    try:
        logger.info("Creating LLM chain")

        custom_prompt = set_custom_prompt()
        llm = load_llm()

        chain = LLMChain(
            llm=llm,
            prompt=custom_prompt
        )

        logger.info("LLM chain created successfully")

        return chain

    except Exception as e:
        logger.error(f"Error creating LLM chain: {e}")
        raise CustomException("Error creating LLM chain")

def get_context_from_query(query):
    try:
        vector_store = load_vector_store()
        if not vector_store:
            raise CustomException("Vector store not found")
        
        docs = vector_store.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        return context
    except Exception as e:
        logger.error(f"Error getting context: {e}")
        return ""