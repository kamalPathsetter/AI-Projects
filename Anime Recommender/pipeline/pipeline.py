from src.vector_store import VectorStore
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, GROQ_MODEL_NAME

from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_directory: str = 'chroma_db'):
        try:
            logger.info("Initializing AnimeRecommenderPipeline...")

            vector_store = VectorStore(csv_path="data/anime.csv", persist_directory=persist_directory)
            
            retriever = vector_store.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=GROQ_MODEL_NAME)

            logger.info("AnimeRecommenderPipeline initialized successfully.")
        
        except Exception as e:
            logger.error(f"Failed to initialize AnimeRecommenderPipeline: {str(e)}")
            raise CustomException(f"Failed to initialize AnimeRecommenderPipeline: {str(e)}")

    def recommend(self, query: str):
        try:
            logger.info("Recommendation request received.")
            return self.recommender.get_recommendation(query)   
        except Exception as e:
            logger.error(f"Failed to get recommendation: {str(e)}")
            raise CustomException(f"Failed to get recommendation: {str(e)}")
        