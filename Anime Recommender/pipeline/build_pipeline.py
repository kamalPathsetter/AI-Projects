from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStore
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

load_dotenv()

def main():
    try:
        logger.info("Starting pipeline build process...")

        data_loader = AnimeDataLoader(original_csv="data/anime_with_synopsis.csv", processed_csv="data/processed_anime.csv")
        data_loader.load_and_process()

        vector_store = VectorStore(csv_path="data/processed_anime.csv", persist_directory="chroma_db")
        vector_store.build_and_save_vector_store()

        logger.info("Pipeline build process completed successfully.")
    except Exception as e:
        logger.error(f"Failed to build pipeline: {str(e)}")
        raise CustomException(f"Failed to build pipeline: {str(e)}")

if __name__ == "__main__":
    main()