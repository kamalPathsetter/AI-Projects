from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import CSVLoader
from dotenv import load_dotenv

load_dotenv()

from config.config import HUGGINGFACE_MODEL_NAME

class VectorStore:
    def __init__(self, csv_path: str, persist_directory: str = 'chroma_db'):
        self.csv_path = csv_path
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name=HUGGINGFACE_MODEL_NAME)

    def build_and_save_vector_store(self):
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding="utf-8",
            metadata_columns=[]
        )

        data = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )

        split_data = text_splitter.split_documents(data)

        db = Chroma.from_documents(
            documents=split_data,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
            collection_name="anime",
        )

    def load_vector_store(self):
        return Chroma(
            collection_name="anime",
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
        )
    