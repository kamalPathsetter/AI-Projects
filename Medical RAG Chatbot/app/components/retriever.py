from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vector_store import load_vector_store

from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """
Answer the following medical question in 4-5 lines maximum using only the information provided in the context.

Context: {context}

Question: {question}

Answer: 

"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"])


def create_qa_chain():
    try:
        logger.info("Creating QA chain")

        vector_store = load_vector_store()

        if not vector_store:
            raise CustomException("Vector store not found")

        custom_prompt = set_custom_prompt()

        llm = load_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID, hf_token=HF_TOKEN)

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=False,
            chain_type_kwargs={
                "prompt": custom_prompt
            }
        )

        logger.info("QA chain created successfully")

        return qa_chain

    except Exception as e:
        logger.error(f"Error creating QA chain: {e}")
        raise CustomException("Error creating QA chain")