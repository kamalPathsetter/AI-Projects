import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from common.logger import get_logger
from common.custom_exception import CustomException
from config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_documents():
    try:
        logger.info("Loading PDF documents...")
        
        loader = DirectoryLoader(
            DATA_PATH,
            glob="*.pdf",
            loader_cls=PyPDFLoader
        )

        documents = loader.load()

        if not documents:
            raise CustomException("No documents found in the specified directory.")

        logger.info("Documents loaded successfully.")

        return documents
    except Exception as e:
        raise CustomException(f"Failed to load PDF documents: {str(e)}")

def create_text_chunks(documents):
    try:
        logger.info("Generating text chunks...")
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len,
            is_separator_regex=False,
        )

        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(text_chunks)} text chunks successfully.")

        return text_chunks

    except Exception as e:
        raise CustomException(f"Failed to generate text chunks: {str(e)}")
    