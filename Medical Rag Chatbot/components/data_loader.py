from components.pdf_loader import load_pdf_documents, create_text_chunks
from components.vector_store import save_vector_store
from common.logger import get_logger
from common.custom_exception import CustomException
from config.config import DB_FAISS_PATH

logger = get_logger(__name__)


def process_data():
    try:
        logger.info("Processing data...")
        
        documents = load_pdf_documents()
        
        text_chunks = create_text_chunks(documents)
        
        vector_store = save_vector_store(text_chunks)
        
        logger.info("Data processed successfully.")
        
        return vector_store
    except Exception as e:
        raise CustomException(f"Failed to process data: {str(e)}")


if __name__ == "__main__":
    process_data()